"""Plot screen current vs spot size for both C2 apertures on a log y-axis.

Screen current hits 0 nA at high spot sizes. Clip those to 0.01 nA so the log
plot stays finite; mark them as "< detection limit" via a down-arrow marker.

Data hardcoded from tem_data_sheet_wk2_talos.xlsx. 5,300x magnification, 120 kV,
120 kV accelerating voltage. Data collected by Sangjoon Bob Lee 2026-04-21.
"""
from pathlib import Path
import matplotlib.pyplot as plt

CLIP = 0.01

spot_size = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
i_70um_raw = [5.80, 3.09, 1.82, 0.737, 0.197, 0.200, 0.113, 0.055, 0.030, 0.000, 0.000]
i_50um_raw = [2.87, 1.53, 0.82, 0.355, 0.174, 0.088, 0.050, 0.025, 0.000, 0.000, 0.000]

i_70um = [v if v > 0 else CLIP for v in i_70um_raw]
i_50um = [v if v > 0 else CLIP for v in i_50um_raw]

fig, ax = plt.subplots(figsize=(10, 8))

ax.plot(spot_size, i_70um, 'o-', lw=3, markersize=10, label='70 µm C2')
ax.plot(spot_size, i_50um, 's--', lw=3, markersize=10, label='50 µm C2')

for ss, v_raw in zip(spot_size, i_70um_raw):
    if v_raw == 0:
        ax.annotate('', xy=(ss, CLIP * 0.5), xytext=(ss, CLIP * 2),
                    arrowprops=dict(arrowstyle='->', color='C0', lw=2))
for ss, v_raw in zip(spot_size, i_50um_raw):
    if v_raw == 0:
        ax.annotate('', xy=(ss, CLIP * 0.5), xytext=(ss, CLIP * 2),
                    arrowprops=dict(arrowstyle='->', color='C1', lw=2))

ax.set_yscale('log')
ax.set_xlabel('Spot size', fontsize=20)
ax.set_ylabel('Screen current (nA)', fontsize=20)
ax.set_title('Screen current vs spot size', fontsize=20, fontweight='bold')
ax.tick_params(axis='both', labelsize=16)
ax.legend(fontsize=14)
ax.grid(True, which='both', alpha=0.3)
ax.text(0.98, 0.02, '↓ = below detection limit (read 0 nA)', transform=ax.transAxes,
        ha='right', va='bottom', fontsize=12, style='italic')

plt.tight_layout()
out = Path(__file__).parent / 'screen_current_vs_spot_size.png'
plt.savefig(out, dpi=120, bbox_inches='tight')
print(f'Saved: {out}')
