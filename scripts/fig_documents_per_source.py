"""Stacked bar chart: documents retrieved per source and task category."""
import numpy as np
import matplotlib.pyplot as plt
from style import apply_style, COLORS, TASKS, FIGURES_DIR

apply_style()

ieee =    np.array([443, 466, 1052,  972,  720])
arxiv =   np.array([122, 781,  781,  367, 1134])
scidir =  np.array([  0,   1,    5,    3,    7])

x = np.arange(len(TASKS))
width = 0.55

fig, ax = plt.subplots(figsize=(7, 4))

ax.bar(x, ieee,   width, label='IEEE Xplore',     color=COLORS['ieee'])
ax.bar(x, arxiv,  width, bottom=ieee, label='ArXiv', color=COLORS['arxiv'])
ax.bar(x, scidir, width, bottom=ieee + arxiv,
       label='Science Direct', color=COLORS['scidir'])

for i, total in enumerate(ieee + arxiv + scidir):
    ax.text(i, total + 30, f'{total:,}', ha='center', va='bottom', fontsize=9)

ax.set_xlabel('Task Category')
ax.set_ylabel('Documents Retrieved')
ax.set_xticks(x)
ax.set_xticklabels(TASKS)
ax.set_ylim(0, 2100)
ax.legend(loc='upper left')
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

fig.tight_layout()
fig.savefig(f'{FIGURES_DIR}/fig_documents_per_source.pdf')
fig.savefig(f'{FIGURES_DIR}/fig_documents_per_source.png')
print('Saved: fig_documents_per_source.pdf / .png')
