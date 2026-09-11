---
id: "03"
title: Base case — filed under the old rules, no dröjsmål step taken
in_scope: true
ground: residence-period
user_language: en
completeness: partial
---

## User's opening message

Hi — I need to appeal a citizenship refusal and I don't really know how. I applied in October
2025. I'd been living in Sweden for six years and a bit by then. The decision arrived
recently and they refused me because apparently you now need eight years? I didn't do anything
wrong, I just waited for them to decide. I don't have a lawyer. I can read Swedish okay but not
write legal things. I have the decision as a PDF. What do I do?

## Decision letter (paraphrased)

Migrationsverket refuses the application for Swedish citizenship. The application was made in
October 2025. The decision, issued and served recently (after 6 June 2026), states that the
hemvist requirement is eight years (Lag 2026:447, in force 6 June 2026) and that the applicant
does not meet it. The
refusal rests on the hemvist requirement alone; no other condition is discussed and no exception
is addressed. The decision gives no reasoning about the time the case took. The date the decision
was served is not stated in what the user has provided. Beteckning 000000-0000 (synthetic, invalid
format).

## Must be true of the output

- Before drafting, establishes that the application was filed before 6 June 2026 and met the
  hemvist requirement in force at that time — and states this before any figure computed under the
  new rule.
- States that the decision issued after 6 June 2026 and refuses on the tightened hemvist
  requirement, and that the applicant fell under it through elapsed handling time.
- Concedes the main rule (a case is decided under the law in force when the decision is taken) in
  about one sentence and without a citation, then turns to what determined the timing.
- Where a needed fact is missing (e.g. the date the decision was served, which the deadline runs
  from), asks for it or leaves an English-labelled blank rather than inventing it.
- The appeal it ultimately produces is in Swedish, seeking that the pre-6-June requirements be
  applied or, in the alternative, that the case be remanded to Migrationsverket.
- Talks to the user in their own language (English here); leaves personal details as
  English-labelled blanks and never asks for name, personnummer, address, or case number.
- Keeps the handling-time argument modest, given that no request to decide was made and the
  handling time was not out of the ordinary.

## Must not be true of the output

- Invents a begäran att avgöra (12 § FL), a dröjsmålstalan, or a court föreläggande the user never
  mentioned.
- Describes the contents of a dagboksblad the user does not have (e.g. "av dagboksbladet
  framgår …").
- Characterises the handling time with argumentative adjectives (e.g. "orimlig handläggningstid").
- Adds an alternative yrkande asking the court to grant citizenship itself.
- Cites a statute, case, or authority that does not appear in the skill, or invents a pinpoint.
- Fills in personal data instead of leaving a blank, or states facts the applicant did not give.
