"""Horizontal bar chart: papers selected in Phase 2 per task category."""
import matplotlib.pyplot as plt
from style import apply_style, TASK_COLORS, FIGURES_DIR

apply_style()

tasks =  ['Generate', 'Retrieval', 'Image-Text', 'Text-Image', 'VQA']
counts = [149, 225, 249, 68, 86]
colors = list(reversed(TASK_COLORS))

fig, ax = plt.subplots(figsize=(6, 3.2))

bars = ax.barh(tasks, counts, color=colors, height=0.6, edgecolor='white',
               linewidth=0.5)

for bar, count in zip(bars, counts):
    ax.text(bar.get_width() + 4, bar.get_y() + bar.get_height() / 2,
            str(count), va='center', fontsize=10)

ax.set_xlabel('Number of Papers')
ax.set_xlim(0, 290)
ax.xaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

ax.annotate('599 unique papers\n775 category assignments',
            xy=(0.97, 0.05), xycoords='axes fraction',
            ha='right', va='bottom', fontsize=8.5,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#F0F0F0',
                      edgecolor='#CCCCCC', alpha=0.9))

fig.tight_layout()
fig.savefig(f'{FIGURES_DIR}/fig_selected_per_category.pdf')
fig.savefig(f'{FIGURES_DIR}/fig_selected_per_category.png')
print('Saved: fig_selected_per_category.pdf / .png')
