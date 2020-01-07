import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Pie chart ------ Customer Type  ----------------------
CustomerType1 = 40
CustomerType2 = 35
CustomerType3 = 25
sizes = [CustomerType1, CustomerType2, CustomerType3]
# colors
colors = ['#7be158', '#ecdd2b', '#cec7c7']

legend_element = [Patch(facecolor='#7be158', label='Customer Type1'),
                  Patch(facecolor='#ecdd2b', label='Customer Type2'),
                  Patch(facecolor='#cec7c7', label='Customer Type3')]


fig1, ax1 = plt.subplots()
wedges, labels, autopct = ax1.pie(sizes, colors=colors, autopct='%.1f%%', startangle=90, pctdistance=.7)
plt.setp(autopct, fontsize=18)
# draw circle
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
fig = plt.gcf()


fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Customer Type', fontsize=16)
ax1.axis('equal')
plt.tight_layout()
plt.legend(handles=legend_element, loc='best')


# plt.show()
plt.savefig('customer_type.png')


