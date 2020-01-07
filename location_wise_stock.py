import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Pie chart ------ Customer Type  ----------------------
commercial = 40
on_hold = 25
damage = 15
quarantine = 20
sizes = [commercial, on_hold, damage, quarantine]
# colors
colors = ['#7be158', '#d6571f', '#cec7c7', '#ecdd2b']

legend_element = [Patch(facecolor='#7be158', label='Commercial'),
                  Patch(facecolor='#d6571f', label='On-Hold'),
                  Patch(facecolor='#cec7c7', label='Damage'),
                  Patch(facecolor='#ecdd2b', label='Quarantine')]


fig1, ax1 = plt.subplots()
wedges, labels, autopct = ax1.pie(sizes, colors=colors, autopct='%.1f%%', startangle=90, pctdistance=.7)
plt.setp(autopct, fontsize=18)
# draw circle
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
fig = plt.gcf()


fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Location Wise Stock', fontsize=16)
ax1.axis('equal')
plt.tight_layout()
plt.legend(handles=legend_element, loc='best')


# plt.show()
plt.savefig('location_stock.png')


