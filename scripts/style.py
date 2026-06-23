import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

COLORS = {
    'ieee':    '#2166AC',
    'arxiv':   '#D6604D',
    'scidir':  '#4DAF4A',
    'vqa':     '#4E79A7',
    'textimg': '#F28E2B',
    'imgtxt':  '#E15759',
    'retrieval':'#76B7B2',
    'generate':'#59A14F',
    'primary': '#2166AC',
    'secondary':'#B2182B',
    'accent':  '#762A83',
    'light':   '#F7F7F7',
    'grid':    '#E0E0E0',
}

TASKS = ['VQA', 'Text-Image', 'Image-Text', 'Retrieval', 'Generate']
TASK_COLORS = [COLORS['vqa'], COLORS['textimg'], COLORS['imgtxt'],
               COLORS['retrieval'], COLORS['generate']]


def apply_style():
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif'],
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 13,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 9,
        'legend.frameon': False,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
    })


FIGURES_DIR = '../figures'
