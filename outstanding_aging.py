import matplotlib.pyplot as plt
import os
import numpy as np

# Outstanding Aging
year1 = ['30 days', '45 days', '60 days', '90 days', '90 days+']
pop_a = [2, 2.4, 3, 3.5,4]
plt.figure(8)
plt.plot(year1, pop_a, color='#ffc000',linewidth=4,label='item1')

for x9,y9 in zip(year1,pop_a):

    label = y9

    plt.annotate(label, # this is the text
                 (x9,y9), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,8), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.title('Outstanding Aging')
ax = plt.subplot()
# fig, ax = plt.subplot()
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
ax.legend(labels=['item1'], loc='upper left',
          fancybox=True, shadow=True, ncol=1)
plt.tight_layout()
plt.yticks(np.arange(0,8,1))

# plt.legend(loc="upper left")

plt.savefig(os.path.join('OutstandingAging.png'), dpi=300, format='png', bbox_inches='tight')
# plt.show()
