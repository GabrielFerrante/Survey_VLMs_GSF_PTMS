"""Bar chart: number of papers addressing each research question."""
import numpy as np
import matplotlib.pyplot as plt
from style import apply_style, COLORS, FIGURES_DIR

apply_style()

questions = ['QP1', 'QP2', 'QP3', 'QP4', 'QP5', 'QP6', 'QP7',
             'QS1', 'QS2', 'QS3', 'QS4']

counts = [589, 163, 119, 18, 332, 589, 389,
          233, 334, 189, 117]

labels = [
    'Learning\nmethods',
    'Graph-based\nrelationships',
    'Semi-supervised\nlearning',
    'Active\nlearning',
    'Explainability\nmodules',
    'Dataset\ndocumentation',
    'Multimodal\nevaluation',
    'Open\nrepositories',
    'Public dataset\naccess',
    'Limited data\nmentioned',
    'Medical imaging\nbenchmarks',
]

is_primary = [i < 7 for i in range(len(questions))]
bar_colors = [COLORS['primary'] if p else COLORS['secondary'] for p in is_primary]

fig, ax = plt.subplots(figsize=(8, 4.5))

x = np.arange(len(questions))
bars = ax.bar(x, counts, color=bar_colors, width=0.65, edgecolor='white',
              linewidth=0.5)

for i, (bar, count) in enumerate(zip(bars, counts)):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 8,
            str(count), ha='center', va='bottom', fontsize=8.5)

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=7.5, ha='center')

sec_x = [x[i] for i in range(len(questions)) if not is_primary[i]]
for sx in sec_x:
    ax.get_xticklabels()[int(sx)].set_color(COLORS['secondary'])

ax.set_ylabel('Number of Papers')
ax.set_ylim(0, 670)
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=COLORS['primary'], label='Primary (QP)'),
    Patch(facecolor=COLORS['secondary'], label='Secondary (QS)'),
]
ax.legend(handles=legend_elements, loc='upper right')

ax2 = ax.twiny()
ax2.set_xlim(ax.get_xlim())
ax2.set_xticks(x)
ax2.set_xticklabels(questions, fontsize=8.5, fontweight='bold')
ax2.tick_params(length=0)
ax2.spines['top'].set_visible(False)

fig.tight_layout()
fig.savefig(f'{FIGURES_DIR}/fig_research_questions.pdf')
fig.savefig(f'{FIGURES_DIR}/fig_research_questions.png')
print('Saved: fig_research_questions.pdf / .png')
