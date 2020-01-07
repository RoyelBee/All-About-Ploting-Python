
import matplotlib.pyplot as plt
import os
import numpy as np
# Customer Wise Sales Vs Outstanding



year4 = ['30 days', '45 days', '60 days', '90 days', '90 days+']
pop_a1 = [3, 3.4, 3, 3.5,2.5]
pop_b1 = [4, 4.4, 3, 4.5,3.5]

plt.figure(9)
plt.plot(year4, pop_a1, color='#ed7d31',linewidth=4,label='item1')
plt.plot(year4, pop_b1, color='#5b9bd5',linewidth=4,label='item2')

for x11, y11 in zip(year4,pop_a1):

    label = y11

    plt.annotate(label, # this is the text
                 (x11,y11), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,8), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x11,y11 in zip(year4,pop_b1):
    label = y11
    plt.annotate(label, # this is the text
                 (x11,y11), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,8), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.title('Customer Wise Sales Vs Outstanding')
ax = plt.subplot()

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
ax.legend(labels=['outstanding', 'sales'], loc='lower center',
          fancybox=True, shadow=True, ncol=2)
plt.tight_layout()
plt.yticks(np.arange(0,8,1))

# plt.legend(loc="upper left")

plt.savefig(os.path.join('CustomerWiseSalesVsOutstanding.png'), dpi=300, format='png', bbox_inches='tight')
# plt.show()