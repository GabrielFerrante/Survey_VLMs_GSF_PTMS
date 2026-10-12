# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Systematic literature review on learning methods for Vision-Language Models (VLMs), with focus on scenarios with limited labeled data. The review investigates semi-supervised, self-supervised, active, and cross-modal learning approaches applied to VLMs.

**Researchers:** Gabriel Souto Ferrante; Priscila Tiemi Maeda Saito

**Period covered:** May 2020 – May 2025

## Systematic Review Data

The review spreadsheet is available at, this link only access for CLAUDE and authors in google_cheat.json.


### Research Questions

**Primary (QP):**
- QP1: Which learning methods are explored?
- QP2: Does training employ graphs to map text-image relationships?
- QP3: Does training leverage semi-supervised learning?
- QP4: Does training incorporate active learning?
- QP5: Does architecture include vision modules for explainability?
- QP6: Are datasets thoroughly documented and appropriate?
- QP7: Do evaluation criteria assess multiple multimodal tasks?

**Secondary (QS):**
- QS1: Are open repositories available?
- QS2: Is dataset access provided publicly?
- QS3: Is limited domain-specific data availability mentioned?
- QS4: Do benchmarks include medical imaging data?

### Search Sources

ACM Digital Library, IEEE Xplore, ArXiv, Science Direct — total of 6,989 documents retrieved (IEEE Xplore 3,653 = 52.3%; ArXiv 3,150 = 45.1%; ACM 170 = 2.4%; Science Direct 16 = 0.2%).

### Task Categories

Papers are organized across five VLM task categories (a paper may appear in more than one category):
- **VQA** (Visual Question Answering) — 89 papers
- **Text-Image** (cross-modal retrieval and alignment) — 71 papers
- **Image-Text** (pre-training and transfer learning) — 259 papers
- **Retrieval** (cross-modal information retrieval) — 226 papers
- **Generate** (image/caption generation, diffusion models) — 146 papers

**Phase 2: 606 unique papers selected** (791 category assignments; the same paper never appears twice in one category). 450 papers appear in one category, 128 in two, 27 in three and 1 in four.

### Selection Flow (PRISMA)

6,989 search results → 1,649 task-level records in the Phase 1 tab (1,145 unique titles; 5,340 results not carried forward, duplicates not itemized) → 852 excluded (CE1: 527 at title/abstract screening, insufficient information, 304 with fewer than 3 questions, 21 other criteria) → 797 retained → 6 repeated entries removed → 791 assignments / 606 unique papers. All 606 are quality-scored; none is excluded by score (Top 10 per category is for presentation only).

### Quality Assessment

13-point scale (maximum 13): unfavorable scenarios (2 pts), theoretical grounding (3 pts), result clarity (3 pts), relevant illustrations (2 pts), accessible repositories (1 pt), answers 4 or more primary questions (2 pts). The sixth criterion is computed from the QP1–QP7 codes listed in Phase 2 (4 or more QPs = 2 pts).

### Inclusion Criteria

Studies must address multimodal text-image models, provide clear architecture descriptions, be conference/journal papers, and answer minimum 2–3 research questions. Non-English/Portuguese works and white papers are excluded.

## Repository Status

This project is being bootstrapped. As the project evolves, update this file with build commands, test commands, dependencies, and architecture details.
