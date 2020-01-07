
import matplotlib.pyplot as plt
import os
import matplotlib.patches as ptc
# Stock Aging
x4 = ['15 Days','30 Days','60 Days','90 Days','120 Days','120+ Days']
energy = [0, 2, 2.5, 3.5, 5, 7]

x_pos = [i for i, _ in enumerate(x4)]
plt.figure(5)
bars =plt.bar(x_pos, energy,width= 0.5)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + 0.22, yval+.12, yval, horizontalalignment='center', verticalalignment='center',
             fontsize=10)

bars[0].set_color('#5b9bd5')
bars[1].set_color('#ed7d31')
bars[2].set_color('#a5a5a5')
bars[3].set_color('#ffc000')
bars[4].set_color('#2f5597')
bars[5].set_color('#548235')
# plt.xlabel("Type Wise Stock")
# plt.ylabel("Energy Output (GJ)")
plt.title("Stock Aging")

red_patch = ptc.Patch(color='#5b9bd5', label='15 Days')
blue_patch = ptc.Patch(color='#ed7d31', label='30 Days')
black_patch = ptc.Patch(color='#a5a5a5', label='60 Days')
white_patch = ptc.Patch(color='#ffc000', label='90 Days')
green_patch = ptc.Patch(color='#2f5597', label='120 Days')
vio_patch = ptc.Patch(color='#548235', label='120+ Days')

plt.legend(handles=[red_patch, blue_patch,black_patch,white_patch,green_patch,vio_patch])

# plt.savefig(os.path.join('StockAging.png'), dpi=300, format='png', bbox_inches='tight')
plt.show()