"""Plot C1 and C2 lens values vs spot size for both C2 apertures.

Data hardcoded from tem_data_sheet_wk2_talos.xlsx (sheets '1A - 70um C2' and '1A - 50um C2').
Taken at 5,300x magnification, 120 kV. Data collected by Sangjoon Bob Lee on 2026-04-21
during Week 3 TEM lab with Andrew B.
"""
from pathlib import Path
import matplotlib.pyplot as plt

spot_size = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

c1_70um = [16.64, 18.18, 20.12, 23.60, 27.47, 32.11, 36.76, 44.11, 58.15, 63.84, 93.24]
c2_70um = [44.52, 43.18, 42.16, 41.10, 40.53, 40.14, 39.837, 39.639, 39.435, 39.233, 38.991]

c1_50um = [16.64, 18.18, 20.12, 23.60, 27.74, 32.11, 36.76, 44.11, 51.85, 63.84, 93.24]
c2_50um = [44.55, 43.16, 42.18, 41.11, 40.73, 40.146, 39.87, 39.604, 39.47, 39.22, 39.02]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.plot(spot_size, c1_70um, 'o-', lw=3, markersize=10, label='70 µm C2')
ax1.plot(spot_size, c1_50um, 's--', lw=3, markersize=10, label='50 µm C2')
ax1.set_xlabel('Spot size', fontsize=20)
ax1.set_ylabel('C1 value (%)', fontsize=20)
ax1.set_title('C1 vs spot size', fontsize=20, fontweight='bold')
ax1.tick_params(axis='both', labelsize=16)
ax1.legend(fontsize=14)
ax1.grid(True, alpha=0.3)

ax2.plot(spot_size, c2_70um, 'o-', lw=3, markersize=10, label='70 µm C2')
ax2.plot(spot_size, c2_50um, 's--', lw=3, markersize=10, label='50 µm C2')
ax2.set_xlabel('Spot size', fontsize=20)
ax2.set_ylabel('C2 value (%)', fontsize=20)
ax2.set_title('C2 vs spot size', fontsize=20, fontweight='bold')
ax2.tick_params(axis='both', labelsize=16)
ax2.legend(fontsize=14)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
out = Path(__file__).parent / 'c1_c2_vs_spot_size.png'
plt.savefig(out, dpi=120, bbox_inches='tight')
print(f'Saved: {out}')
