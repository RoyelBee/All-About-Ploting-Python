import numpy as np
import matplotlib.pyplot as plt
import os
#Top Market

x = ['Mohakhali','Dhanmondi','Gulshan-1','Gulshan-2','Banani']
y = [40,45,49,50,52]
plt.figure(0)
ax = plt.subplot()
width = 0.75 # the width of the bars
ind = np.arange(len(y))  # the x locations for the groups
ax.barh(ind, y, width, color="#70ad47")
ax.set_yticks(ind+width/10)
ax.set_yticklabels(x, minor=False)
plt.title('Top Market',fontweight='bold')
# plt.xlabel('x')
# plt.ylabel('y')
for i, v in enumerate(y):
    ax.text(v + 0.2, i , str(v))
# plt.show()
plt.savefig(os.path.join('TopMarket.png'), dpi=300, format='png', bbox_inches='tight') # use format='svg' or 'pdf' for vectorial picture
