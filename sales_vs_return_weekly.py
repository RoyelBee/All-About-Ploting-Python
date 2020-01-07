# libraries
import numpy as np
import matplotlib.pyplot as plt


# set width of bar
barWidth = 0.33


# set height of bar
sales1 = 12
sales2 = 26
sales3 = 23
sales4 = 24
sales5 = 30
sales6 = 29
sales7 = 12


sales_bar = [sales1, sales2, sales3, sales4, sales5, sales6, sales7]
avg_sales = (sales1 + sales2 + sales3 + sales4 + sales5 + sales6 + sales7)/7

return1 = 4
return2 = 8
return3 = 2
return4 = 8
return5 = 3
return6 = 32
return7 = 12


return_bar = [return1, return2, return3, return4, return5, return6, return7]

# Set position of bar on X axis
r1 = np.arange(len(sales_bar))
r2 = [x + barWidth for x in r1]

plt.figure(200)
# Make the plot
bar1 = plt.bar(r1, sales_bar, color='#5d5ee6', width=barWidth, edgecolor='white', label='Sales')
bar2 = plt.bar(r2, return_bar, color='#ff8c00', width=barWidth, edgecolor='white', label='Return')
plt.axhline(avg_sales, color='#7f7e7c', linewidth=5, label='Avg. Sales')

x_axis = plt.xticks([r + barWidth for r in range(len(sales_bar))],
        ['1', '2', '3', '4', '5', '6', '7'])


# ----Set legend in the bottom of the chart -------------
ax = plt.subplot()
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
handles, labels = plt.gca().get_legend_handles_labels()
order = [1, 2, 0]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc='upper center',
          bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=7)
plt.title('Sales Vs. Return - Weekly')
plt.tight_layout()
plt.savefig('sales_vs_return_weekly.png')