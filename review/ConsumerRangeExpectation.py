# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:33:58 2023

@author: KAM8BP
"""

import matplotlib.pyplot as plt
import numpy as np

# Define the data
countries = ['India', 'China', 'Japan', 'Germany']
distances = ['<200', '200-299', '300-399', '400-499', '500-599', '600+']
data = np.array([
    [7, 22, 30, 24, 9, 8],
    [1, 7, 22, 34, 24, 11],
    [7, 14, 26, 17, 15, 21],
    [2, 6, 13, 26, 23, 30]
])

# Calculate the percentages
totals = data.sum(axis=1)
data_pct = (data / totals[:, None]) * 100

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 4))
index = np.arange(len(distances))
bar_width = 0.14
opacity = 0.8

# Plot the bars
colors = ['#7030A0', '#0070C0', '#00B050', '#002060']
for i in range(len(countries)):
    ax.bar(index + (i * bar_width), data_pct[i], bar_width, alpha=opacity, label=countries[i], color=colors[i])

# Add labels and title
ax.set_ylabel('Percentage of respondents [%]', fontsize=12)
ax.set_xlabel('Consumer expectations on BEV driving range [km]', fontsize=12)
ax.set_xticks(index + bar_width * 2.5)
ax.set_xticklabels(distances, fontsize=12)
ax.set_yticklabels(['{:,.0f}%'.format(x) for x in ax.get_yticks()], fontsize=12)
ax.legend(fontsize=12)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Define the data
countries = ['United States']
distances = ['<100', '100-199', '200-299', '300-399', '400-499', '500+']
data = np.array([
    [6, 9, 16, 22, 18, 29]
])

# Calculate the percentages
totals = data.sum(axis=1)
data_pct = (data / totals[:, None]) * 100

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 4))
index = np.arange(len(distances))
bar_width = 0.8
opacity = 0.8

# Plot the bars
colors = ['#C65911']
for i in range(len(countries)):
    ax.bar(index + (i * bar_width) - ((len(countries)-1)/2 * bar_width), data_pct[i], bar_width, alpha=opacity, label=countries[i], color=colors)

# Add labels and title
ax.set_ylabel('Percentage of respondents [%]', fontsize=12)
ax.set_xlabel('Consumer expectations on BEV driving range [miles]', fontsize=12)
ax.set_xticks(index)
ax.set_xticklabels(distances, fontsize=12)
ax.set_yticklabels(['{:,.0f}%'.format(x) for x in ax.get_yticks()], fontsize=12)
ax.legend(fontsize=12)

plt.tight_layout()
plt.show()