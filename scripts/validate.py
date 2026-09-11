#!/usr/bin/env python3
"""Structural validation for the skills and plugin manifests in this repo.

Every check here is deterministic — pass or fail, no judgment calls:

  * each skills/<name>/ has a SKILL.md with valid, terminated YAML frontmatter
  * name: present, a valid slug, <=64 characters, and equal to the directory name
  * description: present, non-empty, <=1024 characters
  * metadata (if present): a mapping of string values (per the Agent Skills spec)
  * each skill is self-contained: its folder holds only SKILL.md, and the body
    references no bundled scripts/references/assets or other local files (the
    primary way people use these is copy/paste, so nothing else would travel)
  * .claude-plugin/plugin.json and marketplace.json: valid JSON with required keys

It does not judge the content of a skill — only its shape. Exit status is
non-zero if anything fails. Run locally with:

    python scripts/validate.py

Requires PyYAML (pip install pyyaml).
"""
import glob
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---[ \t]*\r?\n", re.DOTALL)

# OS cruft that isn't skill content and shouldn't fail the self-contained check.
IGNORE_FILES = {".DS_Store", "Thumbs.db"}
# Bundled-resource conventions from the Agent Skills spec — a self-contained
# single-file skill must not reach for any of them.
BUNDLED_PATH = re.compile(r"(?<![\w/])(?:scripts|references|assets)/[\w.\-/]+")
# Markdown link target that is not an absolute URL, mail/tel link, or anchor,
# i.e. a link to a local file that wouldn't survive copy/paste.
MD_LINK = re.compile(r"\]\(([^)]+)\)")
REMOTE_LINK = re.compile(r"(?:https?:|mailto:|tel:|#)")

MANIFESTS = (
    (".claude-plugin/plugin.json", ("name",)),
    (".claude-plugin/marketplace.json", ("name", "owner", "plugins")),
)


def validate():
    errors = []

    dirs = sorted(glob.glob(os.path.join(ROOT, "skills", "*", "")))
    if not dirs:
        errors.append("no skills/ subdirectories found")

    for d in dirs:
        name_dir = os.path.basename(d.rstrip("/"))
        path = os.path.join(d, "SKILL.md")
        rel = os.path.relpath(path, ROOT)

        rel_dir = os.path.relpath(d.rstrip("/"), ROOT)
        extras = sorted(e for e in os.listdir(d) if e != "SKILL.md" and e not in IGNORE_FILES)
        if extras:
            errors.append(
                f"{rel_dir}: a skill must be a single self-contained SKILL.md, "
                f"but the folder also contains: {', '.join(extras)}"
            )

        if not os.path.isfile(path):
            errors.append(f"{rel}: missing SKILL.md")
            continue

        text = open(path, encoding="utf-8").read()
        m = FRONTMATTER.match(text)
        if not m:
            errors.append(f"{rel}: missing or unterminated YAML frontmatter")
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            errors.append(f"{rel}: frontmatter is not valid YAML ({e})")
            continue
        if not isinstance(fm, dict):
            errors.append(f"{rel}: frontmatter is not a mapping")
            continue

        name = fm.get("name")
        if not name:
            errors.append(f"{rel}: missing 'name'")
        else:
            name = str(name)
            if len(name) > 64:
                errors.append(f"{rel}: name is longer than 64 characters")
            if not SLUG.match(name):
                errors.append(
                    f"{rel}: name '{name}' is not a valid slug "
                    "(lowercase letters, digits, single hyphens; "
                    "no leading, trailing, or doubled hyphen)"
                )
            if name != name_dir:
                errors.append(
                    f"{rel}: name '{name}' does not match its directory '{name_dir}'"
                )

        desc = fm.get("description")
        if not desc or not str(desc).strip():
            errors.append(f"{rel}: missing 'description'")
        elif len(str(desc)) > 1024:
            errors.append(f"{rel}: description is {len(str(desc))} characters (max 1024)")

        meta = fm.get("metadata")
        if meta is not None and (
            not isinstance(meta, dict)
            or any(not isinstance(v, str) for v in meta.values())
        ):
            errors.append(f"{rel}: metadata must be a mapping of string values")

        body = text[m.end():]
        for bundled in BUNDLED_PATH.finditer(body):
            errors.append(
                f"{rel}: references a bundled path '{bundled.group(0)}' — "
                "a skill must be self-contained in SKILL.md"
            )
        for link in MD_LINK.finditer(body):
            parts = link.group(1).strip().split()
            if parts and not REMOTE_LINK.match(parts[0]):
                errors.append(
                    f"{rel}: links to a local file '{parts[0]}' — "
                    "a skill must be self-contained in SKILL.md"
                )

    for name, required in MANIFESTS:
        path = os.path.join(ROOT, name)
        if not os.path.isfile(path):
            errors.append(f"{name}: missing")
            continue
        try:
            data = json.load(open(path, encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{name}: invalid JSON ({e})")
            continue
        for key in required:
            if key not in data:
                errors.append(f"{name}: missing required key '{key}'")

    return errors, len(dirs)


def main():
    errors, count = validate()
    if errors:
        print("Validation failed:")
        for e in errors:
            print("  - " + e)
        return 1
    print(f"Validated {count} skill(s) and the plugin manifests: all OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
