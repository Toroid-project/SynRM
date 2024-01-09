# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:36:09 2023

@author: KAM8BP
"""

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))

plt.plot([-944,0],[0,1.23], linestyle='-', color='#00884A', label='NdFeB (-40°C)')
plt.plot([-877,0],[0,1.15], linestyle='--', color='#00884A', label='NdFeB (20°C)')
plt.plot([-648,-600,0],[0,0.2,1.01], linestyle='-.', color='#00884A', label='NdFeB (120°C)')

plt.plot([-263,-216,0],[0,0.2,0.47], linestyle='-', color='#007BC0', label='Ferrite (-40°C)')
plt.plot([-302,0],[0,0.45], linestyle='--', color='#007BC0', label='Ferrite (20°C)')
plt.plot([-239,0],[0,0.33], linestyle='-.', color='#007BC0', label='Ferrite (120°C)')

plt.plot([-715,0],[0,0.98], linestyle='-', color='#9E2896', label='SmCo (100°C)')
plt.plot([-597,0],[0,0.85], linestyle='--', color='#9E2896', label='SmCo (400°C)')

plt.plot([-80,-80,-30,0],[0,1.16,1.25,1.25], linestyle='-', color='#71767C', label='AlNiCo (20°C)')

plt.xlabel("Magnetic field intensity [kA/m]", fontsize=12)
plt.ylabel("Magnetic flux density [T]", fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', alpha=0.5)

# Increase tick labels font size to 12
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.tick_params(axis='y', direction='in', labelright=True, labelleft=False)
plt.ylabel('Magnetic flux density [T]', labelpad=-370, rotation=-90, fontsize=12)
plt.savefig("magnets.png", dpi=300, bbox_inches="tight")