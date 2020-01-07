# libraries
import numpy as np
import matplotlib.pyplot as plt

# plt.figure(figsize=(5, 4))
# set width of bar
barWidth = 0.33


# set height of bar
sales_data1 = 12
sales_data2 = 26
sales_data3 = 23

bar2_data1 = 25
bar2_data2 = 15
bar2_data3 = 24

bars1 = [sales_data1, sales_data2, sales_data3]
bars2 = [bar2_data1, bar2_data2, bar2_data3]

avg_sales = (sales_data1 + sales_data2 + sales_data3)/3


# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]


# Make the plot
bar1 = plt.bar(r1, bars1, color='#5d5ee6', width=barWidth, edgecolor='white', label='Sales')
bar2 = plt.bar(r2, bars2, color='#ff8c00', width=barWidth, edgecolor='white', label='Return')
plt.axhline(avg_sales, color='#7f7e7c', linewidth=5, label='Avg. Sales')

x_axis = plt.xticks([r + barWidth for r in range(len(bars1))], ['2017', '2018', '2019'])


# ----Set legend in the bottom of the chart -------------
ax = plt.subplot()
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
handles, labels = plt.gca().get_legend_handles_labels()
order = [1,2,0]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=3)


#plt.legend()


plt.tight_layout()
plt.savefig('group_bar_chart.png', bbox_inches='tight')


# plt.show()
plt.savefig('group_bar_chart.png')