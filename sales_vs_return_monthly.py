# libraries
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
# --- Sales VS return Monthly -----------------------------------
# ----------------------------------------------------------------
# set width of bar
barWidth = 0.33

# set height of bar
jan_sales = 12
feb_sales = 26
march_sales = 23
april_sales = 53
may_sales = 60
june_sales = 29
july_sales = 12
aug_sales = 42
sept_sales = 33
oct_sales = 10
nov_sales = 15
dec_sales = 35

sales_bar = [jan_sales, feb_sales, march_sales, april_sales, may_sales, june_sales, july_sales, aug_sales, sept_sales, oct_sales, nov_sales, dec_sales]
avg_sales = (jan_sales + feb_sales + march_sales + april_sales + may_sales + june_sales + july_sales + aug_sales + sept_sales + aug_sales + oct_sales + nov_sales + dec_sales)/12

jan_return = 4
feb_return = 8
march_return = 2
april_return = 8
may_return = 3
june_return = 32
july_return = 12
aug_return = 9
sep_return = 15
oct_return = 20
nov_return = 25
dec_return = 18

return_bar = [jan_return, feb_return, march_return, april_return, may_return, june_return, july_return, aug_return, sep_return, oct_return, nov_return, dec_return]

# Set position of bar on X axis
r1 = np.arange(len(sales_bar))
r2 = [x + barWidth for x in r1]

plt.figure(201)
# Make the plot
bar1 = plt.bar(r1, sales_bar, color='#5d5ee6', width=barWidth, edgecolor='white', label='Sales')
bar2 = plt.bar(r2, return_bar, color='#ff8c00', width=barWidth, edgecolor='white', label='Return')
plt.axhline(avg_sales, color='#7f7e7c', linewidth=5, label='Avg. Sales')

x_axis = plt.xticks([r + barWidth for r in range(len(sales_bar))],
        ['Jan', 'Feb', 'Mar', 'Apr', 'may', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])


# ----Set legend in the bottom of the chart -------------
ax = plt.subplot()
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
handles, labels = plt.gca().get_legend_handles_labels()
order = [1, 2, 0]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc='upper center',
          bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=12)
plt.title('Sales Vs. Return - Monthly')
plt.tight_layout()
plt.savefig('sales_vs_return_monthly.png')
# plt.show()