import matplotlib.pyplot as plt
import numpy as np
import os
#Top Customer

a = ['Cust1','Cust2','Cust3','Cust4','Cust5']
b = [40,45,49,50,52]
plt.figure(11234)
ax = plt.subplot()
width = 0.75 # the width of the bars
ind = np.arange(len(b))  # the x locations for the groups
ax.barh(ind, b, width, color="#ed7d31")
ax.set_yticks(ind+width/10)
ax.set_yticklabels(a, minor=False)
plt.title('Top Customer',fontweight='bold')
# plt.xlabel('x')
# plt.ylabel('y')
for i, v in enumerate(b):
    ax.text(v + 0.2, i , str(v))
plt.show()
# plt.savefig(os.path.join('TopCustomer.png'), dpi=300, format='png', bbox_inches='tight')