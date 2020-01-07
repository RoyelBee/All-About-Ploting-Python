import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# ---------------------------------------------------------
# ---- Pie chart ------ Sales Trg. Vs. Achv. - D ----------
# ---------------------------------------------------------

target_val = 55
achievement_val = 45
sizes = [target_val, achievement_val]
# colors
colors = ['#ff9999', '#66b3ff']

legend_element = [Patch(facecolor='#ff9999', label='Target'),
                  Patch(facecolor='#66b3ff', label='Achievement')]


fig1, ax1 = plt.subplots()
wedges, labels, autopct = ax1.pie(sizes, colors=colors, autopct='%.1f%%', startangle=90, pctdistance=.7)
plt.setp(autopct, fontsize=18)
# draw circle
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
fig = plt.gcf()


fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Sales Trg. Vs. Achv. - D')
ax1.axis('equal')
plt.tight_layout()
plt.legend(handles=legend_element, loc='best')


# plt.show()
plt.savefig('sales_vs_achiv_d.png')