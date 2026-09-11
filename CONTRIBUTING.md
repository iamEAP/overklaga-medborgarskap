# Contributing

> **Om du har fått avslag och söker hjälp med ditt eget ärende: det här är inte rätt plats.**
> Det här repot innehåller allmänt material och kan inte ge råd i enskilda ärenden. Kontakta en
> jurist med erfarenhet av migrationsrätt. Se [DISCLAIMER.md](DISCLAIMER.md). Pull requests som
> gäller ett enskilt ärende kommer att stängas.
>
> **If you have been refused and are looking for help with your own case, this is not the
> place.** This repository holds general material and cannot advise on individual matters.
> Contact a lawyer experienced in Swedish migration law. Pull requests about an individual
> case will be closed.

Issues are disabled. All contributions come through pull requests. Corrections from
practicing lawyers are especially welcome.

## Scope

This repository covers refusals of Swedish citizenship applications that are a **direct result
of the 2026 reform being applied without transitional provisions** — cases where the applicant
would have met the requirements in force when they applied, and was refused because a
requirement introduced or tightened by the reform was applied to them anyway.

The test, not a list of grounds: *would this refusal have happened if the pre-reform rules had
been applied to this application?* If it would have, the case is out of scope, whatever the
ground. If it would not have, it's in scope, whatever the ground.

In practice this currently means residence period, which is the most common case and the one
the existing skills address. It extends on the same reasoning to knowledge requirements,
self-sufficiency, and any other requirement the reform changed. New skills covering those are
welcome.

Out of scope, and will be declined regardless of quality:

- Refusals that would have followed under the previous rules too, where the transitional
  question makes no difference to the outcome
- Commentary on Migrationsverket, the courts, or the reform as policy

Scope creep arrives one reasonable-looking PR at a time. If you think the scope should widen,
open that as its own PR against this file and make a case there, before writing the content.

## Never include personal data

Do not attach, quote, or paste a real decision letter, case number, personal identity number,
name, address, or any other identifying detail — your own or anyone else's. Use synthetic or
fully redacted material.

**Git history is permanent.** A later commit that deletes a file does not remove it from the
repository. Removing it properly means rewriting history and force-pushing, and by then it may
already be cloned, cached, and indexed. Check before you commit, not after.

If you are a lawyer, note that this applies to client material regardless of any consent you
may have obtained.

## Evidence for changes to skill content

Changes to anything under `skills/` need evidence that the change actually improves behavior.
Assertions on their own aren't enough — a wording change that reads better to a human often
changes model behavior not at all, or for the worse.

Test against the shared fixtures in `fixtures/`, not against a real case. They exist so that
results are comparable between contributions and so nobody has to use their own documents.

For each test run, report:

- The model and the interface (e.g. "Claude Sonnet, claude.ai web" / "GPT, ChatGPT free tier")
- **The date you ran it.** Free tiers change the underlying model without announcing it, so an
  undated result is uninterpretable within a few months.
- Which fixture you used
- The exact prompt
- The relevant part of the output, before and after your change
- What specifically improved, in one or two sentences

Two models is a reasonable minimum. More is better, since these skills are used across
Claude, ChatGPT, Gemini, Mistral and others, and an improvement on one can regress another.

Trim outputs to the part that matters. Nobody needs a full appeal draft pasted twice.

## Legal authorities

If your change introduces or relies on a legal authority, cite it precisely enough to be
checked in under a minute:

- Statutes: SFS number, with chapter and paragraph
- Case law: MIG or HFD reference, or the court and case number
- Migrationsverket positions: the rättsligt ställningstagande's designation
- Preparatory works: proposition or SOU number, with page reference

Include a link to a stable public source (riksdagen.se, lagen.nu, domstol.se,
migrationsverket.se).

**Confirm in the PR that you verified the authority against the primary source yourself, not
through a language model.** Fabricated citations are the most likely way bad content enters a
repository like this one, and they arrive looking entirely plausible. A citation that can't be
verified will be removed even if the surrounding point is sound.

Do not paste text from paywalled commentary. Swedish statutes, judgments and authority
decisions are free of copyright protection, but annotations and analysis in Karnov, JUNO,
textbooks and similar are not.

## Disclose AI assistance

Say whether the contribution was drafted or edited with AI help. This isn't grounds for
rejection — most contributions here will be AI-assisted, and that's fine. It tells the
maintainer how closely to scrutinize the citations.

## New skills

A new skill needs: a clear reason the existing skills can't cover it, a `SKILL.md` following
the [Agent Skills specification](https://agentskills.io/specification) with `name` matching its
directory name, and the same evidence and citation standards as above. Keep it self-contained
in a single file — no scripts, no bundled resources.

## Licensing

Contributions are licensed under CC BY 4.0, the same as the rest of the repository. By opening a
pull request, you confirm that you have the right to submit the contribution and to license it
under CC BY 4.0.

You don't need to use your real name. Contribute under a handle or GitHub's noreply email if you
prefer — the confirmation above is what matters, not your identity.

## What to expect

Review may be slow. Substantive legal changes that the maintainer cannot personally verify may
be declined, or held until someone qualified can look at them — this is a limitation, not a
judgment of your work.

Discussion stays on the contribution. Political argument about the reform, Migrationsverket, or
Swedish migration policy will be closed and locked. There is a great deal of legitimate anger
around this subject; this repository is not where it gets processed.
