
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------------
# ------- Target VS Achievement Bar and line chart ---------------
# ----------------------------------------------------------------
month1 = [5000]
month2 = [4500]
month3 = [2300]
month4 = [1800]
month5 = [4655]
all_month = month1 + month2 + month3 + month4 + month5
xaxis = ('month1', 'month2', 'month3', 'month4', 'month5')

# - Set line chart Target value
y_val1 = [2323]
y_val2 = [3242]
y_val3 = [4321]
y_val4 = [1232]
y_val5 = [4522]
line_y_value = y_val1 + y_val2 + y_val3 + y_val4 + y_val5

y_pos = np.arange(len(xaxis))

plt.figure(101)

bars = plt.bar(y_pos, all_month, color='#66b3ff')
plt.xticks(y_pos, xaxis)

# --------- Show value in the top for  each bar
for bar in bars:
    y_val = bar.get_height()
    plt.text(bar.get_x() + 0.42, y_val + 100, y_val, horizontalalignment='center', verticalalignment='center',
             fontsize=14)

# -------------------- Line chart------------------------
plt.plot(y_pos, line_y_value, color='orange', marker='o', markersize=12, linewidth=4)
plt.title('Target Vs Achievement', fontsize=14)

# -- Show value in each point
for x, y in zip(y_pos, line_y_value):

    # label = "{:.2f}".format(y)

    plt.annotate(y, (x, y), textcoords="offset points", xytext=(0, -20), fontsize=14, ha='center')

# ----Set legend in the bottom of the chart -------------
ax = plt.subplot()
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
ax.legend(labels=['Target', 'Achievement'], loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=2)
plt.tight_layout()
plt.savefig('target_vs_achivement_bar_line_chart.png', bbox_inches='tight')
# plt.show()