import matplotlib.pyplot as plt
import numpy as np
import os
#Top Item

x2 = ['Item1','Item2','Item3','Item4','Item5']
y2 = [40,45,49,50,52]
plt.figure(3)
ax = plt.subplot()
width = 0.75 # the width of the bars
ind = np.arange(len(y2))  # the x locations for the groups
ax.barh(ind, y2, width, color="#5b9bd5")
ax.set_yticks(ind+width/10)
ax.set_yticklabels(x2, minor=False)
plt.title('Top Item',fontweight='bold')
# plt.xlabel('x')
# plt.ylabel('y')
for i, v in enumerate(y2):
    ax.text(v + 0.2, i , str(v))
# plt.show()
plt.savefig(os.path.join('TopItem.png'), dpi=300, format='png', bbox_inches='tight') # use format='svg' or 'pdf' for vectorial picture
