# Fixtures

Synthetic test cases used to check changes to the skills. Contributors test against these
rather than against real cases, so that results are comparable between pull requests and
nobody has to put a real decision letter into a chat interface.

**Everything in this directory is invented.** No fixture contains real personal data, a real
case number, or text from a real decision. Names are fictional and dossier numbers are
deliberately in an invalid format.

## What a fixture contains

Input, plus assertions. **No expected output.**

There is no single correct appeal, so a stored "golden" output would be wrong on arrival and
worse a year later — and it would push contributors toward tuning the skills to reproduce one
particular draft rather than toward behaving well in general. Assertions are the middle ground:
checkable properties the output must have, which stay meaningful as the wording of a good
appeal shifts.

Each fixture is one markdown file:

    fixtures/
    ├── README.md
    ├── 01-<short-slug>.md
    ├── 02-<short-slug>.md
    └── 03-<short-slug>.md

## Format

    ---
    id: "01"
    title: Short description of the situation
    in_scope: true          # false for fixtures that must be declined
    ground: residence-period
    user_language: en       # the language the user writes in
    completeness: partial   # complete | partial — is key information missing?
    ---

    ## User's opening message

    What the person actually types into the chat. Written the way a real person writes:
    incomplete, out of order, sometimes anxious, not a tidy legal summary.

    ## Decision letter (paraphrased)

    A synthetic paraphrase of the refusal — enough for the skill to work with. Include the
    dates, the stated ground, and the reasoning. Never a real letter, and never verbatim text
    from one.

    ## Must be true of the output

    - Concrete, checkable properties.
    - Each one either holds or doesn't when you read the response.

    ## Must not be true of the output

    - Failure modes this fixture exists to catch.

## Writing good fixtures

**Include at least one out-of-scope fixture.** The behavior most worth protecting is the skill
recognizing that a case isn't one it can help with, and stopping. That's the regression nobody
thinks to test for, and it's the one with real cost to a user — a confident appeal aimed at the
wrong target is worse than no appeal.

**Make some of them messy.** Real users omit the delgivning date, paste half the letter, write
in English about a Swedish document, and ask three questions at once. A fixture that's a clean
complete brief only tests the easy path.

**Handle dates so the deadline never looks blown.** The skills compute the appeal deadline (three
to five weeks from service) and lead with it, so a decision pinned to a fixed past date will read
as too late to appeal whenever the fixture is run later — noise these fixtures aren't testing for.
Anchor the historical facts the argument turns on to absolute dates — the application date, the
6 June 2026 entry into force, and any dröjsmål or föreläggande dates (which sit before 6 June
2026) — and keep the decision itself recent and relative: issued and served on the applicant
within the appeal window, never on a fixed calendar month. When a run asks for the delgivning date,
answer with a recent one; treat the decision as served on the day you run the test.

**Cover the grounds separately.** Residence period, knowledge requirements and self-sufficiency
produce different arguments even though they share the same transitional-provisions reasoning,
and a change that helps one can quietly damage another.

**Keep assertions behavioral, not stylistic.** "Establishes the ground of refusal before
drafting anything" is checkable. "Sounds professional" isn't.

## Template

Copy this to start a new fixture.

    ---
    id: "NN"
    title:
    in_scope:
    ground:
    user_language:
    completeness:
    ---

    ## User's opening message

    <!-- FILL IN -->

    ## Decision letter (paraphrased)

    <!-- FILL IN. Synthetic only. -->

    ## Must be true of the output

    - <!-- FILL IN -->

    ## Must not be true of the output

    - Cites a statute, case, or authority that does not appear in the skill
    - <!-- FILL IN -->
