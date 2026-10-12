"""Grouped bar chart: publication year distribution per task (IEEE Xplore + ArXiv documents)."""
import glob
import re
from collections import Counter

import numpy as np
import openpyxl
import matplotlib.pyplot as plt
from style import apply_style, TASKS, TASK_COLORS, FIGURES_DIR

apply_style()

years = [2020, 2021, 2022, 2023, 2024, 2025]

# One sheet per task in the review spreadsheet. Each sheet lists the retrieved documents
# per database: IEEE Xplore (with Publication Year) and ArXiv (title + link). ACM and
# Science Direct have only result counts in the spreadsheet, so they cannot be placed in time.
SHEETS = {'VQA': 'VQA', 'Text-Image': 'TEXT-IMAGE', 'Image-Text': 'IMAGE-TEXT',
          'Retrieval': 'RETRIEVAL', 'Generate': 'GENERATE'}


def yearly_counts(ws):
    """Unique documents per publication year in one task sheet.

    IEEE Xplore: unique titles, year from the 'Publication Year' column.
    ArXiv: unique identifiers, year from the identifier (YYMM.NNNNN).
    Years outside 2020-2025 are ignored.
    """
    rows = [tuple(list(r) + [None] * 30)[:30] for r in ws.iter_rows(values_only=True)]
    header = rows[1]
    year_col, title_col = header.index('Publication Year'), header.index('Document Title')
    arxiv_row = next(i for i, r in enumerate(rows) if r[0] == 'ARXIV')
    scidir_row = next(i for i, r in enumerate(rows) if r[0] == 'SCIENCE DIRECT')

    counts, seen_titles, seen_ids = Counter(), set(), set()
    for r in rows[2:arxiv_row]:
        if not r[title_col]:
            continue
        key = re.sub(r'[^a-z0-9]', '', str(r[title_col]).lower())
        if key in seen_titles:
            continue
        seen_titles.add(key)
        try:
            counts[int(float(r[year_col]))] += 1
        except (TypeError, ValueError):
            pass
    for r in rows[arxiv_row + 1:scidir_row]:
        link = r[1] if isinstance(r[1], str) else ''
        m = re.search(r'arxiv\.org/(?:abs|pdf)/((\d{2})\d{2}\.\d{4,5})', link)
        if m and m.group(1) not in seen_ids:
            seen_ids.add(m.group(1))
            counts[2000 + int(m.group(2))] += 1
    return counts


workbook = glob.glob('../GSF*.xlsx')[0]
wb = openpyxl.load_workbook(workbook, read_only=True, data_only=True)
data = {}
for task in TASKS:
    counts = yearly_counts(wb[SHEETS[task]])
    data[task] = [counts[y] for y in years]
total = sum(sum(v) for v in data.values())

x = np.arange(len(years))
n_tasks = len(TASKS)
width = 0.15
offsets = np.arange(n_tasks) - (n_tasks - 1) / 2

fig, ax = plt.subplots(figsize=(8, 4))

for i, task in enumerate(TASKS):
    bars = ax.bar(x + offsets[i] * width, data[task], width,
                  label=task, color=TASK_COLORS[i], edgecolor='white',
                  linewidth=0.3)

ax.set_xlabel('Ano de publicação')
ax.set_ylabel('Documentos únicos recuperados')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(loc='upper left', ncol=3)
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

fig.tight_layout()
fig.savefig(f'{FIGURES_DIR}/fig_year_distribution_PTBR.pdf')
fig.savefig(f'{FIGURES_DIR}/fig_year_distribution_PTBR.png')
print('Saved: fig_year_distribution_PTBR.pdf / .png')
print({task: sum(v) for task, v in data.items()}, 'total', total)
