"""Combined 1x3 plot: C1, C2, and screen current vs spot size for both C2 apertures.

Fonts are 2x larger than the standalone scripts so the figure stays readable when
the three panels are rendered in a single row.

Data hardcoded from tem_data_sheet_wk2_talos.xlsx (sheets '1A - 70um C2' and
'1A - 50um C2'). 5,300x magnification, 120 kV. Data collected by Sangjoon Bob Lee
on 2026-04-21 during the MATSCI 322 TEM lab session with Andrew B.
"""
from pathlib import Path
import matplotlib.pyplot as plt

CLIP = 0.01

spot_size = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

c1_70um = [16.64, 18.18, 20.12, 23.60, 27.47, 32.11, 36.76, 44.11, 58.15, 63.84, 93.24]
c2_70um = [44.52, 43.18, 42.16, 41.10, 40.53, 40.14, 39.837, 39.639, 39.435, 39.233, 38.991]

c1_50um = [16.64, 18.18, 20.12, 23.60, 27.74, 32.11, 36.76, 44.11, 51.85, 63.84, 93.24]
c2_50um = [44.55, 43.16, 42.18, 41.11, 40.73, 40.146, 39.87, 39.604, 39.47, 39.22, 39.02]

i_70um_raw = [5.80, 3.09, 1.82, 0.737, 0.197, 0.200, 0.113, 0.055, 0.030, 0.000, 0.000]
i_50um_raw = [2.87, 1.53, 0.82, 0.355, 0.174, 0.088, 0.050, 0.025, 0.000, 0.000, 0.000]
i_70um = [v if v > 0 else CLIP for v in i_70um_raw]
i_50um = [v if v > 0 else CLIP for v in i_50um_raw]

# Doubled font sizes vs the standalone scripts
TITLE_FS = 40
LABEL_FS = 40
TICK_FS = 32
LEGEND_FS = 28
ANNOT_FS = 24

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(28, 10))

# C1 panel
ax1.plot(spot_size, c1_70um, 'o-', lw=5, markersize=16, label='70 µm C2')
ax1.plot(spot_size, c1_50um, 's--', lw=5, markersize=16, label='50 µm C2')
ax1.set_xlabel('Spot size', fontsize=LABEL_FS)
ax1.set_ylabel('C1 value (%)', fontsize=LABEL_FS)
ax1.set_title('C1 vs spot size', fontsize=TITLE_FS, fontweight='bold')
ax1.tick_params(axis='both', labelsize=TICK_FS)
ax1.legend(fontsize=LEGEND_FS)
ax1.grid(True, alpha=0.3)
ax1.set_xticks(spot_size)

# C2 panel
ax2.plot(spot_size, c2_70um, 'o-', lw=5, markersize=16, label='70 µm C2')
ax2.plot(spot_size, c2_50um, 's--', lw=5, markersize=16, label='50 µm C2')
ax2.set_xlabel('Spot size', fontsize=LABEL_FS)
ax2.set_ylabel('C2 value (%)', fontsize=LABEL_FS)
ax2.set_title('C2 vs spot size', fontsize=TITLE_FS, fontweight='bold')
ax2.tick_params(axis='both', labelsize=TICK_FS)
ax2.legend(fontsize=LEGEND_FS)
ax2.grid(True, alpha=0.3)
ax2.set_xticks(spot_size)

# Screen current panel (log y)
ax3.plot(spot_size, i_70um, 'o-', lw=5, markersize=16, label='70 µm C2')
ax3.plot(spot_size, i_50um, 's--', lw=5, markersize=16, label='50 µm C2')
for ss, v_raw in zip(spot_size, i_70um_raw):
    if v_raw == 0:
        ax3.annotate('', xy=(ss, CLIP * 0.5), xytext=(ss, CLIP * 2),
                     arrowprops=dict(arrowstyle='->', color='C0', lw=3))
for ss, v_raw in zip(spot_size, i_50um_raw):
    if v_raw == 0:
        ax3.annotate('', xy=(ss, CLIP * 0.5), xytext=(ss, CLIP * 2),
                     arrowprops=dict(arrowstyle='->', color='C1', lw=3))
ax3.set_yscale('log')
ax3.set_xlabel('Spot size', fontsize=LABEL_FS)
ax3.set_ylabel('Screen current (nA)', fontsize=LABEL_FS)
ax3.set_title('Screen current vs spot size', fontsize=TITLE_FS, fontweight='bold')
ax3.tick_params(axis='both', labelsize=TICK_FS)
ax3.legend(fontsize=LEGEND_FS)
ax3.grid(True, which='both', alpha=0.3)
ax3.set_xticks(spot_size)
ax3.text(0.98, 0.02, '↓ = below detection limit (read 0 nA)',
         transform=ax3.transAxes, ha='right', va='bottom',
         fontsize=ANNOT_FS, style='italic')

plt.tight_layout()
out = Path(__file__).parent / 'all_plots_vs_spot_size.png'
plt.savefig(out, dpi=120, bbox_inches='tight')
print(f'Saved: {out}')
