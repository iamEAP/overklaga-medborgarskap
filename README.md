# Överklaga medborgarskap — Agent Skills

*English below · Svenska längre ned*

> ## ⚠️ Read first · Läs först
>
> **You usually have three to five weeks from being served your decision to appeal — miss it and the refusal is final, so file in time even if your appeal is still rough.** This is general information for refusals caused by the 2026 reform being applied to an application that met the rules when it was filed — not refusals on other grounds, and **not legal advice** ([DISCLAIMER.md](DISCLAIMER.md)).
>
> **Du har oftast tre till fem veckor från delgivningen på dig att överklaga — missar du fristen står avslaget fast, så skicka in i tid även om överklagandet är ofärdigt.** Det här är allmän information om avslag som beror på att 2026 års reform tillämpats på en ansökan som uppfyllde reglerna när den lämnades in — inte avslag på andra grunder, och **inte juridisk rådgivning** ([DISCLAIMER.md](DISCLAIMER.md)).

---

## English

Help for people whose Swedish citizenship application was refused because of the 2026 reform,
for preparing an appeal (*överklagande*) to the migration court (*migrationsdomstolen*).

It comes as two **skills** — plain-text files you hand to an AI assistant like ChatGPT, Claude,
or Gemini. You don't need to install anything: you can paste one into a chat and start. Whatever
language you write in, the appeal it drafts comes out in **Swedish** for you to finish and file.

### Which skill to use

There are two, built around two different strategies. Pick the one that fits your situation.

| Skill | Best if… | Open |
|---|---|---|
| **medborgarskap-forvaltningsratt** | you can show you meet — or realistically could meet — the newer requirements (language, income, and so on). It builds a pragmatic appeal on administrative-law grounds, aimed at getting your case sent back to Migrationsverket for a fresh decision. | [Open the skill →](https://raw.githubusercontent.com/iamEAP/overklaga-medborgarskap/main/skills/medborgarskap-forvaltningsratt/SKILL.md) |
| **medborgarskap-rattighetsgrund** | you have no realistic way to prove the requirements added on 6 June 2026 and want to argue on principle — a rights-based, constitutional appeal (legitimate expectations, equal treatment) built on the [Fair Transition Sweden](https://www.fairtransitionsweden.com) template. Read the caution below first. | [Open the skill →](https://raw.githubusercontent.com/iamEAP/overklaga-medborgarskap/main/skills/medborgarskap-rattighetsgrund/SKILL.md) |

**A caution on the rights-based route.** Courts have already applied the new rules to
applications filed under the old ones and rejected appeals built on these arguments
([reported example](https://www.dagensjuridik.se/nyheter/nya-regler-om-medborgarskap-kan-tillampas-pa-aldre-ansokningar/)).
That approach therefore faces long odds and may be dismissed quickly. If you have any way to
show you meet the newer requirements, the administrative route is usually the more practical one.

### How to use it — the simple way

No install, nothing to set up beyond the chat tool you already use.

1. Open the **Open the skill →** link for the one you picked. You'll see a page of plain text.
2. Select all of it and copy it (Ctrl/Cmd-A, then Ctrl/Cmd-C).
3. Start a **new chat** in an AI assistant (ChatGPT, Claude, Gemini, …), paste the whole thing
   in, and send it.
   - The few `name:` / `description:` lines between the `---` lines at the top are just
     metadata. Leave them in; you don't need to understand them.
4. Then, in your own words, describe what happened and paste the relevant parts of your
   decision — you don't need to include your name, personnummer, or address. The assistant
   will ask you a few questions and draft the appeal.
5. **Check it, fill in the blanks, and file it in time.** What you get is a strong starting
   draft, not a finished appeal. If you're not comfortable reviewing Swedish legal text, an hour
   with a migration lawyer could be worth it.

The assistant will try to talk with you in whatever language you write in, but the skills are
written in English, so that isn't guaranteed — the appeal itself is always in Swedish.

### Before you rely on this

**Privacy.** Whatever you paste goes to a third-party AI provider, where it may be logged or
retained. Share only the parts of your decision the skill needs — it never asks for your name,
personnummer, address, or case number, and leaves those as blanks you fill in offline.

**Versioning.** The content is tied to the law as it stands now. Before using a skill, check the
`version` and the as-of date in its metadata (the block at the top of the `SKILL.md`). The law
and the practice on this question will move, and an older copy may be out of date.

**Contributing.** Issues are disabled on this repository. Corrections — especially from
practicing lawyers — are welcome by pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

**License.** [CC BY 4.0](LICENSE). That covers the skill files — share or adapt *them* with
attribution. The appeal you generate is yours to file, and you don't credit this project anywhere
in it.

<details>
<summary><strong>Installing a skill natively (for technical users)</strong></summary>

Installing the skills instead of pasting them is generally a paid-plan feature across these tools,
so for a one-off appeal the free copy-paste path above is all most people need.

- **Web UIs (claude.ai and similar):** download a skill's zip from the
  [latest release](https://github.com/iamEAP/overklaga-medborgarskap/releases/latest) and upload
  it in the tool's skills settings. The release zips put the skill folder at the archive root,
  which is the shape these uploads expect.
- **Claude Code:**
  ```bash
  git clone https://github.com/iamEAP/overklaga-medborgarskap.git
  cp -r overklaga-medborgarskap/skills/* ~/.claude/skills/
  ```
- **Claude Code plugin marketplace:** this repo is also a marketplace.
  ```
  /plugin marketplace add iamEAP/overklaga-medborgarskap
  /plugin install overklaga-medborgarskap@overklaga-medborgarskap
  ```
- **Other tools** read skills in the open [Agent Skills](https://agentskills.io) format from a
  skills directory — a skill is just a folder with a `SKILL.md`. Many now also read a
  vendor-neutral `.agents/skills/` directory, which is the most portable option. Locations change
  and not every tool agrees, so confirm against the tool's own docs. As a guide (late 2026):

  | Tool | Skills directory |
  |---|---|
  | Portable (Codex, Gemini CLI, Cursor) | `.agents/skills/` in a project, or `~/.agents/skills/` for all projects |
  | Claude Code | `~/.claude/skills/` (or `.claude/skills/` per project) |
  | Codex CLI | `~/.codex/skills/` |
  | Gemini CLI | `~/.gemini/skills/` (or `.gemini/skills/` per project) |
  | Cursor | `~/.cursor/skills/` (or `.cursor/skills/` per project) |
  | GitHub Copilot / VS Code | supported; location varies — see the tool's docs or agentskills.io |

</details>

---

## Svenska

Hjälp för dig som fått avslag på din ansökan om svenskt medborgarskap på grund av 2026 års
reform, för att förbereda ett **överklagande** till migrationsdomstolen.

Det består av två **färdigheter** (skills) — textfiler som du ger till en AI-assistent som
ChatGPT, Claude eller Gemini. Du behöver inte installera något: du kan klistra in en av dem i en chatt
och sätta igång. Oavsett vilket språk du skriver på blir själva överklagandet på **svenska**,
som du sedan färdigställer och lämnar in.

### Vilken färdighet ska du välja

Det finns två, byggda kring två olika strategier. Välj den som passar din situation.

| Färdighet | Passar dig om… | Öppna |
|---|---|---|
| **medborgarskap-forvaltningsratt** | du kan visa att du uppfyller — eller realistiskt skulle kunna uppfylla — de nyare kraven (språk, försörjning och så vidare). Den bygger ett pragmatiskt överklagande på förvaltningsrättslig grund som syftar till att få ärendet återförvisat till Migrationsverket för ett nytt beslut. | [Öppna färdigheten →](https://raw.githubusercontent.com/iamEAP/overklaga-medborgarskap/main/skills/medborgarskap-forvaltningsratt/SKILL.md) |
| **medborgarskap-rattighetsgrund** | du inte realistiskt kan bevisa de krav som infördes den 6 juni 2026 och vill föra ett principiellt resonemang — ett rättighetsbaserat, konstitutionellt överklagande (berättigade förväntningar, likhet inför lagen) byggt på [Fair Transition Sweden](https://www.fairtransitionsweden.com)-mallen. Läs varningen nedan först. | [Öppna färdigheten →](https://raw.githubusercontent.com/iamEAP/overklaga-medborgarskap/main/skills/medborgarskap-rattighetsgrund/SKILL.md) |

**En varning om den rättighetsbaserade vägen.** Domstolar har redan tillämpat de nya reglerna på
ansökningar som lämnats in under de gamla och avslagit överklaganden som byggt på dessa argument
([rapporterat exempel](https://www.dagensjuridik.se/nyheter/nya-regler-om-medborgarskap-kan-tillampas-pa-aldre-ansokningar/)).
Den vägen har därför små utsikter att lyckas, och ett överklagande som bygger på den kan avslås
snabbt. Om du på något sätt kan visa att du uppfyller de nyare kraven är den förvaltningsrättsliga
vägen oftast lämpligare.

### Så använder du den — det enkla sättet

Ingen installation, inget att ställa in utöver den chatt du redan använder.

1. Öppna länken **Öppna färdigheten →** för den du valt. Du ser en sida med ren text.
2. Markera allt och kopiera det (Ctrl/Cmd-A, sedan Ctrl/Cmd-C).
3. Starta en **ny chatt** i en AI-assistent (ChatGPT, Claude, Gemini …), klistra in alltihop och
   skicka.
   - De få raderna `name:` / `description:` mellan `---`-raderna högst upp är bara metadata. Låt
     dem vara kvar; du behöver inte förstå dem.
4. Beskriv sedan med egna ord vad som hänt och klistra in de relevanta delarna av ditt beslut —
   du behöver inte ta med namn, personnummer eller adress. Assistenten ställer några frågor och
   tar fram ett utkast till överklagande.
5. **Granska det, fyll i luckorna och lämna in det i tid.** Det du får är ett bra utkast att utgå
   från, inte ett färdigt överklagande. Om du inte känner dig bekväm med att granska svensk
   juridisk text kan en timme hos en migrationsjurist vara väl använd.

Assistenten försöker prata med dig på det språk du skriver på, men färdigheterna är skrivna på
engelska, så det är inte garanterat — själva överklagandet blir alltid på svenska.

### Innan du förlitar dig på detta

**Integritet.** Allt du klistrar in går till en extern AI-leverantör, där det kan
loggas eller sparas. Dela bara de delar av ditt beslut som färdigheten behöver — den frågar
aldrig efter namn, personnummer, adress eller ärendenummer, utan lämnar dem som luckor du fyller
i offline.

**Versionering.** Innehållet är knutet till lagen som den ser ut nu. Kontrollera `version` och
`as-of`-datumet (vilket datum innehållet gäller) i färdighetens metadata (blocket högst upp i
`SKILL.md`) innan du använder den. Lag och praxis i den här frågan kommer att förändras, och en
äldre kopia kan vara inaktuell.

**Bidra.** Ärenden (issues) är avstängda i det här repot. Rättelser — särskilt från praktiserande
jurister — tas emot via pull request. Se [CONTRIBUTING.md](CONTRIBUTING.md).

**Licens.** [CC BY 4.0](LICENSE). Det gäller färdighetsfilerna — dela eller bearbeta *dem* med
angivande av upphovsperson. Överklagandet du tar fram är ditt eget, och du behöver inte ange
projektet någonstans i det.

<details>
<summary><strong>Installera färdigheten i verktyget (för tekniskt vana)</strong></summary>

Att installera färdigheterna i stället för att klistra in dem kräver i regel ett betalabonnemang
hos dessa verktyg, så för ett enstaka överklagande räcker den kostnadsfria kopiera-och-klistra-metoden
ovan för de flesta.

- **Webbgränssnitt (claude.ai med flera):** ladda ner zip-filen för en färdighet från
  [senaste utgåvan](https://github.com/iamEAP/overklaga-medborgarskap/releases/latest) och ladda
  upp den under verktygets skills-inställningar. Zip-filerna lägger färdighetsmappen i arkivets
  rot, vilket är strukturen dessa uppladdningar förväntar sig.
- **Claude Code:**
  ```bash
  git clone https://github.com/iamEAP/overklaga-medborgarskap.git
  cp -r overklaga-medborgarskap/skills/* ~/.claude/skills/
  ```
- **Claude Codes plugin-marknadsplats:** det här repot är även en marknadsplats.
  ```
  /plugin marketplace add iamEAP/overklaga-medborgarskap
  /plugin install overklaga-medborgarskap@overklaga-medborgarskap
  ```
- **Andra verktyg** läser färdigheter i det öppna [Agent Skills](https://agentskills.io)-formatet
  från en skills-katalog — en färdighet är bara en mapp med en `SKILL.md`. Många läser numera även
  en leverantörsneutral katalog `.agents/skills/`, vilket är det mest portabla alternativet.
  Platserna ändras och alla verktyg är inte överens, så kontrollera mot verktygets egen
  dokumentation. Som vägledning (slutet av 2026):

  | Verktyg | Skills-katalog |
  |---|---|
  | Portabelt (Codex, Gemini CLI, Cursor) | `.agents/skills/` i ett projekt, eller `~/.agents/skills/` för alla projekt |
  | Claude Code | `~/.claude/skills/` (eller `.claude/skills/` per projekt) |
  | Codex CLI | `~/.codex/skills/` |
  | Gemini CLI | `~/.gemini/skills/` (eller `.gemini/skills/` per projekt) |
  | Cursor | `~/.cursor/skills/` (eller `.cursor/skills/` per projekt) |
  | GitHub Copilot / VS Code | stöds; plats varierar — se verktygets dokumentation eller agentskills.io |

</details>
