"""
Generate probe correction workflow diagram for STEM guide.

Shows the iterative C1A1 → Tableau → C1A1 correction process with details.

Usage:
    python correction_workflow.py
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(12, 20))
ax.set_xlim(0, 12)
ax.set_ylim(-2, 20)
ax.set_aspect('equal')
ax.axis('off')

# Colors
COLOR_C1A1 = '#BBDEFB'      # Blue for C1A1 steps
COLOR_TABLEAU = '#FFE0B2'   # Orange for Tableau steps
COLOR_CHECK = '#C8E6C9'     # Green for decision
COLOR_BORDER = '#37474F'
COLOR_ARROW = '#546E7A'


def draw_box(x, y, width, height, title, details, color):
    """Draw a rounded box with title and details."""
    box = FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.02,rounding_size=0.3",
        facecolor=color,
        edgecolor=COLOR_BORDER,
        linewidth=2.5
    )
    ax.add_patch(box)
    center_y = y + height / 2
    ax.text(x + width/2, center_y + 0.35, title,
            ha='center', va='center', fontsize=22, fontweight='bold')
    ax.text(x + width/2, center_y - 0.45, details,
            ha='center', va='center', fontsize=18, linespacing=1.1)


def draw_arrow(start, end, color=COLOR_ARROW):
    """Draw an arrow between two points."""
    arrow = FancyArrowPatch(
        start, end,
        arrowstyle='->,head_width=0.5,head_length=0.35',
        color=color,
        linewidth=3,
        mutation_scale=15
    )
    ax.add_patch(arrow)


# Title
ax.text(6, 19, 'Probe Correction Workflow', fontsize=26, fontweight='bold',
        ha='center', va='center')

# Step 1: C1A1 First Pass
draw_box(1.5, 16.0, 9, 2.2, 'C1A1 (100%)',
         'Target: C1 < 1 nm, A1 < 3 nm\nClick 0th-2nd until stable → Stop', COLOR_C1A1)

# Arrow down
draw_arrow((6, 16.0), (6, 15.5))

# Step 2: Tableau Start
draw_box(1.5, 12.8, 9, 2.2, 'Tableau: Start',
         'Beam tilts to multiple angles\nMeasures A2, B2, C3, S3, A3', COLOR_TABLEAU)

# Arrow down
draw_arrow((6, 12.8), (6, 12.3))

# Step 3: Tableau Accept
draw_box(1.5, 9.6, 9, 2.2, 'Tableau: Accept',
         'Validate the measurement\n(confirms data is good)', COLOR_TABLEAU)

# Arrow down
draw_arrow((6, 9.6), (6, 9.1))

# Step 4: Apply Corrections
draw_box(1.5, 6.4, 9, 2.2, 'Tableau: Correct (75%)',
         'Click limiting aberration (yellow)\nTarget: A2 < 40 nm, S3 < 500 nm', COLOR_TABLEAU)

# Arrow down
draw_arrow((6, 6.4), (6, 5.9))

# Step 5: C1A1 Final Pass
draw_box(1.5, 3.2, 9, 2.2, 'C1A1 (75%)',
         'Fine-tune A1 after Tableau\nTarget: A1 < 3 nm', COLOR_C1A1)

# Arrow down to check
draw_arrow((6, 3.2), (6, 2.7))

# Step 6: Check D50
box = FancyBboxPatch(
    (3, 0.8), 6, 1.6,
    boxstyle="round,pad=0.02,rounding_size=0.3",
    facecolor=COLOR_CHECK,
    edgecolor=COLOR_BORDER,
    linewidth=2.5
)
ax.add_patch(box)
ax.text(6, 1.6, 'D50 < 75 pm?', ha='center', va='center', fontsize=22, fontweight='bold')

# Loop back arrow (if No) - L-shaped: left, up, then right into Tableau: Start
# Horizontal line from decision box going left
ax.plot([3, 0.6], [1.6, 1.6], color='#E53935', linewidth=3, solid_capstyle='round')
# Vertical line going up
ax.plot([0.6, 0.6], [1.6, 13.9], color='#E53935', linewidth=3, solid_capstyle='round')
# Horizontal line going right toward box
ax.plot([0.6, 1.5], [13.9, 13.9], color='#E53935', linewidth=3, solid_capstyle='round')
# Arrow head at the end
loop_arrow = FancyArrowPatch(
    (1.2, 13.9), (1.5, 13.9),
    arrowstyle='->,head_width=0.4,head_length=0.3',
    color='#E53935',
    linewidth=3,
    mutation_scale=15
)
ax.add_patch(loop_arrow)
ax.text(-0.1, 8, 'No\n(iterate)', fontsize=20, color='#E53935',
        ha='center', va='center', fontweight='bold')

# Done arrow (if Yes) - arrow to the right
draw_arrow((9, 1.6), (10.5, 1.6), color='#43A047')
ax.text(10.8, 1.9, 'Yes', fontsize=20, color='#43A047',
        ha='left', va='center', fontweight='bold')
ax.text(10.8, 1.3, 'Done!', fontsize=20, color='#43A047',
        ha='left', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('correction_workflow.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved: correction_workflow.png")
