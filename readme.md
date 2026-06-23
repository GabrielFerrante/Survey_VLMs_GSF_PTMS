# Survey: Learning Methods for Vision-Language Models

Systematic literature review on learning methods for Vision-Language Models (VLMs), focusing on scenarios with limited labeled data — including semi-supervised, self-supervised, active, and cross-modal learning approaches.

## Researchers

- Gabriel Souto Ferrante
- Priscila Tiemi Maeda Saito

## Scope

- **Period:** May 2020 – May 2025
- **Sources:** ACM Digital Library, IEEE Xplore, ArXiv, Science Direct
- **Documents retrieved:** 6,854
- **Unique papers selected (Phase 2):** 599

## Research Questions

| Code | Question |
|------|----------|
| QP1 | Which learning methods are explored? |
| QP2 | Does training employ graphs to map text-image relationships? |
| QP3 | Does training leverage semi-supervised learning? |
| QP4 | Does training incorporate active learning? |
| QP5 | Does architecture include vision modules for explainability? |
| QP6 | Are datasets thoroughly documented and appropriate? |
| QP7 | Do evaluation criteria assess multiple multimodal tasks? |
| QS1 | Are open repositories available? |
| QS2 | Is dataset access provided publicly? |
| QS3 | Is limited domain-specific data availability mentioned? |
| QS4 | Do benchmarks include medical imaging data? |

## Task Categories

The selected papers are organized across five VLM task categories:

| Category | Papers | Focus |
|----------|--------|-------|
| VQA | 84 | Visual Question Answering |
| Text-Image | 68 | Cross-modal retrieval and semantic alignment |
| Image-Text | 249 | Pre-training and transfer learning |
| Retrieval | 225 | Cross-modal information retrieval and ranking |
| Generate | 149 | Image/caption generation, diffusion models |

> **Note:** A paper may appear in more than one category. Total unique papers: 599 (778 category assignments total).

## Search Strings

### IEEE Xplore / Science Direct

All queries follow the same template, varying the **task** and **learning method**:

```
("Vision-Language Models" OR "VLM") AND ("<TASK>") AND ("<LEARNING_METHOD>") AND ("Deep Learning")
NOT ("Survey" OR "Review") NOT ("Video" OR "Audio")
```

**Tasks:** VQA, Text-Image, Image-Text, Retrieval, Generate

**Learning methods:** Active Learning, Semi-supervised Learning, Cross-modal Learning, Multimodal Learning, Self-supervised Learning

### ArXiv

Queries use the ArXiv advanced search API with the following template:

```
order: -announced_date_first
size: <50–200>
date_range: from 2020-05-01 to 2025-05-01
classification: Computer Science (cs), Electrical Engineering and Systems Science (eess)
include_cross_list: True
terms: AND all=Vision-Language Models OR VLM
       AND all=<TASK>
       AND all=<LEARNING_METHOD>
       NOT all=Survey OR Review
```

**Tasks:** VQA, Text-Image, Image-Text, Retrieval, Generate

**Learning methods:** Active Learning OR AL, Semi-supervised Learning, Cross-modal Learning, Multimodal Learning, Self-supervised Learning

### Results per task and source

| Task | IEEE | ArXiv | Science Direct | Total |
|------|------|-------|----------------|-------|
| VQA | 443 | 122 | 0 | 565 |
| Text-Image | 466 | 781 | 1 | 1,248 |
| Image-Text | 1,052 | 781 | 5 | 1,838 |
| Retrieval | 972 | 367 | 3 | 1,342 |
| Generate | 720 | 1,134 | 7 | 1,861 |
| **Total** | **3,653** | **3,185** | **16** | **6,854** |

## Quality Assessment

11-point scale evaluating:
- Unfavorable scenarios coverage (2 pts)
- Theoretical grounding (3 pts)
- Result clarity (3 pts)
- Relevant illustrations (2 pts)
- Accessible repositories (1 pt)

