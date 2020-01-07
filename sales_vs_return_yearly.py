# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.33


# set height of bar
s_2017 = 400
s_2018 = 232
s_2019 = 453

sales_bar = [s_2017, s_2018, s_2019]
avg_sales = (s_2017 + s_2018 + s_2019)/3
r_2017 = 40
r_2018 = 55
r_2019 = 70


return_bar = [r_2017, r_2018, r_2019]
# Set position of bar on X axis
r1 = np.arange(len(sales_bar))
r2 = [x + barWidth for x in r1]

plt.figure(100)
# Make the plot
bar1 = plt.bar(r1, sales_bar, color='#5d5ee6', width=barWidth, edgecolor='white', label='Sales')
bar2 = plt.bar(r2, return_bar, color='#ff8c00', width=barWidth, edgecolor='white', label='Return')
plt.axhline(avg_sales, color='#7f7e7c', linewidth=5, label='Avg. Sales')

x_axis = plt.xticks([r + barWidth for r in range(len(sales_bar))],
        ['2017', '2018', '2019'])

# ----Set legend in the bottom of the chart -------------
ax = plt.subplot()
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
handles, labels = plt.gca().get_legend_handles_labels()
order = [1, 2, 0]
ax.legend([handles[idx] for idx in order], [labels[idx] for idx in order], loc='upper center',
          bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=12)
plt.title('Sales Vs. Return - Yearly')
plt.tight_layout()
plt.savefig('sales_vs_return_yearly.png', bbox_inches='tight')
#
# plt.show()