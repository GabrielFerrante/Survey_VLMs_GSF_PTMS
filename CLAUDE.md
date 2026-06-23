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

ACM Digital Library, IEEE Xplore, ArXiv, Science Direct — total of 6,854 documents retrieved.

### Task Categories

Papers are organized across five VLM task categories (a paper may appear in more than one category):
- **VQA** (Visual Question Answering) — 84 papers
- **Text-Image** (cross-modal retrieval and alignment) — 68 papers
- **Image-Text** (pre-training and transfer learning) — 249 papers
- **Retrieval** (cross-modal information retrieval) — 225 papers
- **Generate** (image/caption generation, diffusion models) — 149 papers

**Phase 2: 599 unique papers selected** (778 category assignments total;)

### Quality Assessment

11-point scale: unfavorable scenarios (2 pts), theoretical grounding (3 pts), result clarity (3 pts), relevant illustrations (2 pts), accessible repositories (1 pt).

### Inclusion Criteria

Studies must address multimodal text-image models, provide clear architecture descriptions, be conference/journal papers, and answer minimum 2–3 research questions. Non-English/Portuguese works and white papers are excluded.

## Repository Status

This project is being bootstrapped. As the project evolves, update this file with build commands, test commands, dependencies, and architecture details.
