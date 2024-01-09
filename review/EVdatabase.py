

import pandas as pd
import matplotlib.pyplot as plt

# define the colors
city_cycle_color = '#007BC0'
rep_cycle_color = '#18837E'

# read data from Excel file into a DataFrame
new_data = pd.read_excel('fig.xlsx')

# delete data after 1355 rows
new_data = new_data.iloc[:1355]

# overwrite Excel file with truncated data
new_data.to_excel('fig.xlsx', index=False)

# define the figure size
plt.figure(figsize=(6, 4))

# plot the two columns of the DataFrame with the specified colors
plt.plot(new_data.iloc[:, 1], color=rep_cycle_color, label='Representative')
plt.plot(new_data.iloc[:, 0], color=city_cycle_color, label='City')

# set the x-axis label and tick marks
plt.xlabel('Time Elapsed [s]', fontsize=12)
plt.xticks(fontsize=12)

# set the y-axis label and tick marks
plt.ylabel('Speed [km/h]', fontsize=12)
plt.yticks(fontsize=12)

# add a legend
plt.legend(fontsize=12)

# show the plot
plt.show()






import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.DataFrame({'x': [139, 163, 145, 146, 161, 165], 
                    'y': [1012, 1208, 1035, 1248, 1095, 1125]})

x = [147, 171, 178, 142, 174, 157, 164, 158, 156, 177, 159, 158, 156, 143, 173, 155, 172, 130, 155, 145, 157, 144, 156, 130]
y = [1760, 1888, 1695, 1365, 1577, 1530, 1440, 1611, 1595, 1577, 1623, 1598, 1530, 1610, 1570, 2000, 1565, 1255, 1625, 1400, 1757, 1405, 1610, 1281]

df2 = pd.DataFrame({'x': x, 'y': y})

plt.figure(figsize=(6, 4))

plt.scatter(df1['y'], df1['x'], label='mini (A)', color = '#9E2896')
plt.scatter(df2['y'], df2['x'], label='small (B)', color = '#007BC0')

plt.ylabel("Rated Consumption [Wh/km]", fontsize=12)
plt.xlabel("Unladen Weight (EU) [kg]", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', alpha=0.5)

# Increase tick labels font size to 12
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)

plt.savefig("wltpcons.png", dpi=300, bbox_inches="tight")





import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.DataFrame({'x': [230, 190, 220, 260, 133, 157], 
                    'y': [1012, 1208, 1035, 1248, 1095, 1125]})

x = [484, 430, 440, 323, 395, 356, 219, 388, 395, 385, 336, 338, 359, 305, 320, 179, 222, 190, 399, 310, 452, 310, 276, 190]
y = [1760, 1888, 1695, 1365, 1577, 1530, 1440, 1611, 1595, 1577, 1623, 1598, 1530, 1610, 1570, 2000, 1565, 1255, 1625, 1400, 1757, 1405, 1610, 1281]

df2 = pd.DataFrame({'x': x, 'y': y})

plt.figure(figsize=(6, 4))

plt.scatter(df1['y'], df1['x'], label='mini (A)', color = '#9E2896')
plt.scatter(df2['y'], df2['x'], label='small (B)', color = '#007BC0')

plt.ylabel("WLTP range [km]", fontsize=12)
plt.xlabel("Unladen Weight (EU) [kg]", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', alpha=0.5)

# Increase tick labels font size to 12
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)

plt.savefig("wltprange.png", dpi=300, bbox_inches="tight")






import pandas as pd
import matplotlib.pyplot as plt

# read Excel file into a pandas DataFrame
df = pd.read_excel('curb.xlsx')

# create a list of the column names to use as y-axes
y_cols = df.columns[1:5]

# define the colors to use
colors = ['#9E2896', '#007BC0', '#6B7F3F', '#00884A']

# create a 2x2 grid of subplots with a 6:4 aspect ratio
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 4))
fig.subplots_adjust(wspace=0.2, hspace=0.3)
fig.set_size_inches(10, 6)

# loop through each subplot and plot the data
for i, ax in enumerate(axes.flatten()):
    if i < len(y_cols):
        # plot the data using the ith column as the y-axis
        ax.plot(df.iloc[:, 0], df.iloc[:, i+1], color=colors[i])
        # set the subplot title and axis labels
        ax.set_title(y_cols[i], fontsize=12)
        ax.set_xlabel('Time elapsed [s]', fontsize=12)
        ax.set_ylabel('Speed [km/h]', fontsize=12)
        ax.tick_params(axis='both', labelsize=12)
        ax.set_ylim(0, 80)
    else:
        # remove any unused subplots
        fig.delaxes(ax)

# adjust the spacing between subplots and save the figure
fig.tight_layout()
plt.savefig('output.png')

import pandas as pd
import matplotlib.pyplot as plt

# read in the CSV file using pandas
df = pd.read_csv('fig.csv', sep=',')

# extract the first and second columns as separate Series
col1 = df.iloc[:, 0]
col2 = df.iloc[:, 1]

# set the figure size and ratio
fig, ax = plt.subplots(figsize=(6, 4))
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)

# create a line plot with col1 and col2 on the y-axis and the index of values on the x-axis
colors = ['#9E2896', '#007BC0', '#6B7F3F', '#00884A']
plt.plot(col2.index, col2, color=colors[1], label='Representative')
plt.plot(col1.index, col1, color=colors[0], label='City')


# set the axis labels and tick label font sizes
plt.xlabel('Speed [km/h]', fontsize=12)
plt.ylabel('Time elapsed [s]', fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', alpha=0.5)

# add a legend and show the plot
plt.legend(fontsize=12)
plt.savefig('drivecycles.png')







