"""
Generate detector stack side view diagram for STEM guide.

Shows how HAADF detector blocks high-angle electrons while direct beam
passes through the hole to reach the camera.

Usage:
    python detector_stack.py
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def main():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    # Title
    ax.text(5, 9.5, 'HAADF and CCD Camera Layout', fontsize=20, fontweight='bold',
            ha='center', va='center')
    # Sample (dark gray bar at top) - centered
    sample = FancyBboxPatch((2.5, 8.2), 5, 0.4,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#555555', edgecolor='black', linewidth=2)
    ax.add_patch(sample)
    ax.text(8, 8.4, 'Sample', fontsize=16, va='center', fontweight='bold')
    # Electron source point (convergence point at sample) - centered
    source_x, source_y = 5, 8.2
    # HAADF detector (two orange rectangles with gap) - centered
    haadf_left = FancyBboxPatch((2.5, 4.8), 2, 0.5,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor='#FF8C00', edgecolor='black', linewidth=2)
    haadf_right = FancyBboxPatch((5.5, 4.8), 2, 0.5,
                                  boxstyle="round,pad=0.02,rounding_size=0.05",
                                  facecolor='#FF8C00', edgecolor='black', linewidth=2)
    ax.add_patch(haadf_left)
    ax.add_patch(haadf_right)
    ax.text(8, 5.05, 'HAADF', fontsize=16, va='center', fontweight='bold')
    ax.text(8, 4.55, '(annular detector)', fontsize=14, va='center', color='#555555')
    # Camera (blue bar at bottom) - centered
    camera = FancyBboxPatch((2.5, 1.8), 5, 0.5,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#4FC3F7', edgecolor='black', linewidth=2)
    ax.add_patch(camera)
    ax.text(8, 2.05, 'CCD Camera', fontsize=16, va='center', fontweight='bold')
    # Direct beam (blue arrow from sample through hole to camera)
    ax.annotate('', xy=(5, 2.3), xytext=(source_x, source_y),
                arrowprops=dict(arrowstyle='->,head_width=0.4,head_length=0.3',
                               color='#1565C0', lw=3, shrinkA=0, shrinkB=0))
    # High-angle scattered electrons (red arrows from sample to HAADF)
    ax.annotate('', xy=(3.5, 5.3), xytext=(source_x, source_y),
                arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.25',
                               color='#D32F2F', lw=3, shrinkA=0, shrinkB=0))
    ax.annotate('', xy=(6.5, 5.3), xytext=(source_x, source_y),
                arrowprops=dict(arrowstyle='->,head_width=0.3,head_length=0.25',
                               color='#D32F2F', lw=3, shrinkA=0, shrinkB=0))
    # Labels for electron paths
    ax.text(1.0, 6.8, 'High-angle\nelectrons', fontsize=16, color='#D32F2F',
            va='center', fontweight='bold')
    ax.text(1.0, 6.0, '(detected by HAADF)', fontsize=14, color='#D32F2F', va='center')
    ax.text(1.0, 3.5, 'Direct beam', fontsize=16, color='#1565C0',
            va='center', fontweight='bold')
    ax.text(1.0, 2.9, '(passes to CCD)', fontsize=14, color='#1565C0', va='center')
    # Angle indicators (dashed lines showing collection angles)
    ax.plot([source_x, 2.5], [source_y, 4.8], 'k--', lw=1.5, alpha=0.4)
    ax.plot([source_x, 7.5], [source_y, 4.8], 'k--', lw=1.5, alpha=0.4)
    plt.tight_layout()
    plt.savefig('detector_stack.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: detector_stack.png")


if __name__ == "__main__":
    main()
