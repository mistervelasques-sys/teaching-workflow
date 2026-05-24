# AGENTS.md — Teaching Workflow

## Tool roles

Obsidian is the didactic source of truth.
ChatGPT Project is used for pedagogical reasoning, critique, audit and design decisions.
GitHub is the versioned workspace.
Codex is used for file operations, scripts, exports, structure checks and technical cleanup.
Google Drive is used only for final shareable exports.

## Codex may

- create folders and files from templates;
- check missing files;
- rename files according to conventions;
- generate scripts;
- compare versions;
- create changelogs;
- prepare exports;
- split and place content into existing files when explicitly instructed.

## Codex must not

- invent vault sources;
- claim a sequence is didactically valid without an audit;
- decide the final task alone;
- modify CEFR level, final task, cultural issue or assessment criteria without explicit instruction;
- generate a full teaching sequence unless a validated design brief exists;
- generate worksheets before lesson plans are validated;
- generate assessment grids before the final task is validated.

## Required project structure

Each project in 03_PROJECTS must contain:

- 00_brief.md
- 01_sources_consultees.md
- 02_design_brief.md
- 03_sequence.md
- 04_lessons/
- 05_worksheets/
- 06_assessment/
- 07_slides/
- 90_audit.md
- 91_revision_plan.md
- exports/

## Workflow order

1. Create or verify project structure.
2. Fill 00_brief.md.
3. Fill 01_sources_consultees.md.
4. Fill 02_design_brief.md.
5. Generate 03_sequence.md only after design brief validation.
6. Audit 03_sequence.md.
7. Generate lesson plans one by one.
8. Generate worksheets only after the corresponding lesson plan is validated.
9. Generate assessment and slides only after sequence architecture is validated.
10. Prepare final exports for Google Drive.
