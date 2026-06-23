"""Grouped bar chart: publication year distribution per task (IEEE data only)."""
import numpy as np
import matplotlib.pyplot as plt
from style import apply_style, TASKS, TASK_COLORS, FIGURES_DIR

apply_style()

years = [2020, 2021, 2022, 2023, 2024, 2025]

data = {
    'VQA':        [ 3,  23,  25,  53,  85,  34],
    'Text-Image': [ 1,   5,  10,  47, 104,  43],
    'Image-Text': [ 2,  16,  31, 129, 239, 109],
    'Retrieval':  [ 4,  16,  36, 136, 194,  83],
    'Generate':   [ 7,  34,  62, 228, 276, 113],
}

x = np.arange(len(years))
n_tasks = len(TASKS)
width = 0.15
offsets = np.arange(n_tasks) - (n_tasks - 1) / 2

fig, ax = plt.subplots(figsize=(8, 4))

for i, task in enumerate(TASKS):
    bars = ax.bar(x + offsets[i] * width, data[task], width,
                  label=task, color=TASK_COLORS[i], edgecolor='white',
                  linewidth=0.3)

ax.set_xlabel('Publication Year')
ax.set_ylabel('Documents Retrieved')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(loc='upper left', ncol=3)
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

fig.tight_layout()
fig.savefig(f'{FIGURES_DIR}/fig_year_distribution.pdf')
fig.savefig(f'{FIGURES_DIR}/fig_year_distribution.png')
print('Saved: fig_year_distribution.pdf / .png')
