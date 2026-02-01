"""
Generate STEM training workflow overview diagram.

Shows the three-part structure in a 3x1 vertical layout.

Usage:
    python workflow_overview.py
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(16, 6.5))
ax.set_xlim(0, 16)
ax.set_ylim(1.5, 10.5)
ax.set_aspect('equal')
ax.axis('off')

# Colors (consistent with correction_workflow.py)
COLOR_PART1 = '#BBDEFB'  # Blue
COLOR_PART2 = '#FFE0B2'  # Orange
COLOR_PART3 = '#C8E6C9'  # Green
COLOR_BORDER = '#37474F'
COLOR_ARROW = '#546E7A'

def draw_step_box(x, y, width, height, text, color, fontsize=16):
    """Draw a rounded step box."""
    box = FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.02,rounding_size=0.2",
        facecolor=color,
        edgecolor=COLOR_BORDER,
        linewidth=1.5
    )
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text,
            ha='center', va='center', fontsize=fontsize, fontweight='bold')

def draw_part_header(x, y, width, text, color):
    """Draw a part header box."""
    box = FancyBboxPatch(
        (x, y), width, 1.0,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        facecolor=color,
        edgecolor=COLOR_BORDER,
        linewidth=2.5
    )
    ax.add_patch(box)
    ax.text(x + width/2, y + 0.5, text,
            ha='center', va='center', fontsize=20, fontweight='bold')

def draw_arrow_down(x, y1, y2):
    """Draw a downward arrow."""
    arrow = FancyArrowPatch(
        (x, y1), (x, y2),
        arrowstyle='->,head_width=0.3,head_length=0.2',
        color=COLOR_ARROW,
        linewidth=2,
        mutation_scale=12
    )
    ax.add_patch(arrow)

def draw_arrow_right(x1, x2, y):
    """Draw a rightward arrow."""
    arrow = FancyArrowPatch(
        (x1, y), (x2, y),
        arrowstyle='->,head_width=0.4,head_length=0.3',
        color=COLOR_ARROW,
        linewidth=3,
        mutation_scale=15
    )
    ax.add_patch(arrow)

# Title (with gap below)
ax.text(8, 10.0, 'Spectra 300 STEM Workflow', fontsize=24, fontweight='bold',
        ha='center', va='center')

# Column positions (3 columns side by side)
col1_x, col2_x, col3_x = 0.5, 5.75, 11.0
col_width = 4.5
step_height = 0.8
step_gap = 0.15

# Part 1: Setup & Alignment
draw_part_header(col1_x, 8.2, col_width, 'Part 1: Setup', COLOR_PART1)
steps_part1 = ['1.1 Vacuum', '1.2 Eucentric Height', '1.3 STEM Config',
               '1.4 Alignments', '1.5 Mono Tune', '1.6 HAADF Setup']
y = 7.2
for i, step in enumerate(steps_part1):
    draw_step_box(col1_x, y, col_width, step_height, step, COLOR_PART1)
    if i < len(steps_part1) - 1:
        draw_arrow_down(col1_x + col_width/2, y, y - step_gap)
    y -= (step_height + step_gap)

# Part 2: Correction
draw_part_header(col2_x, 8.2, col_width, 'Part 2: Correction', COLOR_PART2)
steps_part2 = ['2.1 C1A1', '2.2 Tableau']
y = 7.2
for i, step in enumerate(steps_part2):
    draw_step_box(col2_x, y, col_width, step_height, step, COLOR_PART2)
    if i < len(steps_part2) - 1:
        draw_arrow_down(col2_x + col_width/2, y, y - step_gap)
    y -= (step_height + step_gap)

# Part 3: Imaging
draw_part_header(col3_x, 8.2, col_width, 'Part 3: Imaging', COLOR_PART3)
steps_part3 = ['3.1 Acquire Images', '3.2 Sherpa (optional)']
y = 7.2
for i, step in enumerate(steps_part3):
    draw_step_box(col3_x, y, col_width, step_height, step, COLOR_PART3)
    if i < len(steps_part3) - 1:
        draw_arrow_down(col3_x + col_width/2, y, y - step_gap)
    y -= (step_height + step_gap)

# Arrows between parts
arrow_y = 8.7
draw_arrow_right(col1_x + col_width + 0.1, col2_x - 0.1, arrow_y)
draw_arrow_right(col2_x + col_width + 0.1, col3_x - 0.1, arrow_y)

plt.tight_layout()
plt.savefig('workflow_overview.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved: workflow_overview.png")
