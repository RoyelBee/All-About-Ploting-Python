
import matplotlib.pyplot as plt
import os
import numpy as np

# Periodic Outstanding
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pyodbc as db
import numpy as np


connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=10.168.2.164;'
                        'DATABASE=ARCHND;'
                        'UID=sa;PWD=erp')
cursor = connection.cursor()

query = """
 """

assert cursor.execute(query)



x7= range(0,5)

y7 = [2, 3, 4, 5, 8]

fig, ax = plt.subplots()
plt.title('Periodic Outstanding')
plt.axhline(2,color='#7f7e7c',linewidth = .5)
plt.axhline(4,color='#7f7e7c',linewidth = .5)
plt.axhline(6,color='#7f7e7c',linewidth = .5)
plt.axhline(8,color='#7f7e7c',linewidth = .5)
# Change the color and its transparency
plt.fill_between(x7, y7, color="#70ad47")
plt.xticks(np.arange(5), ('January','February','March','April','May'))


for x7,y7 in zip(x7,y7):

    label = y7

    plt.annotate(label, # this is the text
                 (x7,y7), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,4), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


# plt.savefig('PeriodicOutstanding.png')
plt.show()