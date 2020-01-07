import matplotlib.pyplot as plt
import numpy as np
import os
# -------Top Brand----------------------------

x1 = ['Brand1','Brand2','Brand3','Brand4','Brand5']
y1 = [40,45,49,50,52]
plt.figure(223)
ax = plt.subplot()
width = 0.75 # the width of the bars
ind = np.arange(len(y1))  # the x locations for the groups
ax.barh(ind, y1, width, color="#5b9bd5")
ax.set_yticks(ind+width/10)
ax.set_yticklabels(x1, minor=False)
plt.xticks(x_pos, labels, fontsize=14)

plt.title('Top Brand',fontweight='bold')
# plt.xlabel('x')
# plt.ylabel('y')
for i, v in enumerate(y1):
    ax.text(v + 0.2, i , str(v))

# plt.savefig(os.path.join('TopBrand.png'), dpi=300, format='png', bbox_inches='tight')
plt.show()