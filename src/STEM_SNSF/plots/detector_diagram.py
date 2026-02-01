"""
Generate detector diagram for STEM guide.

Shows HAADF detector (annular) vs camera (pixelated) geometry.

Usage:
    python detector_diagram.py
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def main():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    # --- Left: HAADF detector shape (top view) ---
    ax1 = axes[0]
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal')
    ax1.set_title('HAADF Detector (top view)\nAnnular = ring-shaped', fontsize=12, fontweight='bold')
    # Outer ring
    outer_circle = patches.Circle((0, 0), 1.2, fill=True, color='orange', alpha=0.7, label='HAADF active area')
    ax1.add_patch(outer_circle)
    # Inner hole (where electrons pass through)
    inner_circle = patches.Circle((0, 0), 0.4, fill=True, color='white')
    ax1.add_patch(inner_circle)
    # Center dot showing beam
    beam = patches.Circle((0, 0), 0.05, fill=True, color='blue')
    ax1.add_patch(beam)
    ax1.annotate('Hole\n(beam passes\nthrough)', (0, 0), ha='center', va='center', fontsize=9)
    ax1.annotate('Active area\n(detects high-angle\nscattered e-)', (0.8, 0.8), ha='center', fontsize=9)
    ax1.set_xlabel('High-angle scattered electrons hit the ring')
    ax1.axis('off')
    # --- Middle: Camera shape (top view) ---
    ax2 = axes[1]
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_aspect('equal')
    ax2.set_title('Camera/CCD (top view)\nPixelated square sensor', fontsize=12, fontweight='bold')
    # Square camera
    camera = patches.Rectangle((-1, -1), 2, 2, fill=True, color='lightblue', alpha=0.7)
    ax2.add_patch(camera)
    # Grid to show pixels
    for i in np.linspace(-1, 1, 9):
        ax2.axhline(i, color='gray', linewidth=0.5, alpha=0.5)
        ax2.axvline(i, color='gray', linewidth=0.5, alpha=0.5)
    ax2.annotate('Pixelated sensor\n(captures full 2D pattern)', (0, 0), ha='center', va='center', fontsize=10)
    ax2.set_xlabel('Captures the entire ronchigram at once')
    ax2.axis('off')
    # --- Right: Side view of detector stack ---
    ax3 = axes[2]
    ax3.set_xlim(-2, 2)
    ax3.set_ylim(-0.5, 4.5)
    ax3.set_title('Side view: Detector positions', fontsize=12, fontweight='bold')
    # Sample
    sample = patches.Rectangle((-1.5, 4), 3, 0.1, fill=True, color='gray')
    ax3.add_patch(sample)
    ax3.annotate('Sample', (1.6, 4), fontsize=10)
    # HAADF (annular)
    haadf_left = patches.Rectangle((-1.2, 2.5), 0.5, 0.2, fill=True, color='orange')
    haadf_right = patches.Rectangle((0.7, 2.5), 0.5, 0.2, fill=True, color='orange')
    ax3.add_patch(haadf_left)
    ax3.add_patch(haadf_right)
    ax3.annotate('HAADF\n(ring with hole)', (1.6, 2.5), fontsize=10)
    # Camera
    camera_side = patches.Rectangle((-1, 0.5), 2, 0.2, fill=True, color='lightblue')
    ax3.add_patch(camera_side)
    ax3.annotate('Camera\n(pixelated)', (1.6, 0.5), fontsize=10)
    # Electron beam paths - Direct beam (through hole)
    ax3.annotate('', xy=(0, 0.7), xytext=(0, 3.9),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax3.annotate('Direct beam\n(passes through hole)', (-1.8, 1.8), fontsize=9, color='blue')
    # High-angle scattered (hits HAADF)
    ax3.annotate('', xy=(-0.9, 2.7), xytext=(0, 3.9),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax3.annotate('', xy=(0.9, 2.7), xytext=(0, 3.9),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax3.annotate('High-angle\nscattered e-', (-1.8, 3.2), fontsize=9, color='red')
    ax3.axis('off')
    plt.tight_layout()
    plt.savefig('detector_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: detector_diagram.png")


if __name__ == "__main__":
    main()
