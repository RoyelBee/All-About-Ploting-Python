import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# --------------------------------------------------------
# ----- Pie chart ------ Sales Trg. Vs. Achv. - M --------
# --------------------------------------------------------
target_val = 43
achievement_val = 57
sizes = [target_val, achievement_val]
# colors
colors = ['#e5cc05', '#648799']

legend_element = [Patch(facecolor='#e5cc05', label='Target'),
                  Patch(facecolor='#648799', label='Achievement')]


fig1, ax1 = plt.subplots()
wedges, labels, autopct = ax1.pie(sizes, colors=colors, autopct='%.1f%%', startangle=90, pctdistance=.7)
plt.setp(autopct, fontsize=18)
# draw circle
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
fig = plt.gcf()


fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Sales Trg. Vs. Achv. - M')
ax1.axis('equal')
plt.tight_layout()
plt.legend(handles=legend_element, loc='best')
# plt.show()
plt.savefig('sales_vs_achiv_m.png')