import pandas as pd
import matplotlib.pyplot as plt
import os

# Expiry Date wise Stock
year = ['10-jan-2019', '10-feb-2019', '10-March-2019', '10-April-2019']
pop_a = [2, 2, 3, 5]
pop_b = [3, 4, 2, 6]
pop_c = [4, 6, 5, 7]
pop_d = [6, 5, 7, 8]

plt.figure(6)
plt.plot(year, pop_a, color='#ffc000',linewidth=4)
plt.plot(year, pop_b, color='#a5a5a5',linewidth=4)
plt.plot(year, pop_c, color='#548235',linewidth=4)
plt.plot(year, pop_d, color='#5b9bd5',linewidth=4)

for x5,y5 in zip(year,pop_a):

    label = "{:.2f}".format(y5)

    plt.annotate(label, # this is the text
                 (x5,y5), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,8), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
for x5,y5 in zip(year,pop_b):

    label = "{:.2f}".format(y5)

    plt.annotate(label, # this is the text
                 (x5,y5), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
for x5,y5 in zip(year,pop_c):

    label = "{:.2f}".format(y5)

    plt.annotate(label, # this is the text
                 (x5,y5), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
for x5,y5 in zip(year,pop_d):

    label = "{:.2f}".format(y5)

    plt.annotate(label, # this is the text
                 (x5,y5), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,8), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.title('Expiry Date wise Stock')
ax = plt.subplot()

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
ax.legend(labels=['item1', 'item2','item3','item4'], loc='upper left',
          fancybox=True, shadow=True, ncol=4)
plt.tight_layout()


# plt.legend(loc="upper left")
plt.savefig(os.path.join('ExpiryDatewiseStock.png'), dpi=300, format='png', bbox_inches='tight')
# plt.show()
