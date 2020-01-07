import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import BoxStyle

# --- First column box configuration
left, width = 0, .16
bottom, height = .5, .5
right = left + width
top = 1
fig = plt.figure(figsize=(16, 4))
ax = fig.add_axes([0, 0, 1, 1])

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )
ax.add_patch(p)


# ---  Target Box ----------
kpi_label = 'Target' + "\n"
target = 16
target = str(target) + " M"

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), target,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Sales Box ------------------------
left, width = .168, .16
bottom, height = .5, .5
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Sales' + " \n"
sales = 20
sales = str(sales) + ' M'

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), sales,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Avg Sales Box ------------------------
left, width = .336, .16
bottom, height = .5, .5
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Avg Sales' + "\n"
avg_sales = 13
avg_sales = str(avg_sales) + " M"

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), avg_sales,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Return % Box ------------------------
left, width = .504, .16
bottom, height = .5, .5
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Return %' + "\n"
target = 2
target = str(target) + ' M'

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), target,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Sales Growth % Box ------------------------
left, width = .672, .16
bottom, height = .5, .5
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Sales Growth %' + "\n"
sales_growth = 3
sales_growth = str(sales_growth) + ' M'

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), sales_growth,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Outstanding Box ------------------------
left, width = .84, .16
bottom, height = .5, .5
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Outstanding' + "\n"
outstanding = 4
outstanding = str(outstanding) + ' M'


ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), outstanding,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------------------------------------------------
# ----------------Row 2 boxes -----------------------
# ---------------------------------------------------

# ------ Row two Boxes configurations ---------------
left, width = 0, .16
bottom, height = 0, .45
right = left + width
top = .4

# ---------- Cust Grwth % Box ------------------------
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Cust Grwth %' + "\n"
cust_growth = 1.6
cust_growth = str(cust_growth) + " M"

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), cust_growth,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Cov. Cust % Box ------------------------

left, width = .168, .16
bottom, height = 0, .45
right = left + width
top = .4

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Cov. Cust %' + "\n"
cov_cust = 56
cov_cust = str(cov_cust) + " M"


ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), cov_cust,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Cov. Item % Box ------------------------
left, width = .336, .16
bottom, height = 0, .45
right = left + width
top = .4

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Cov. Item %' + "\n"
cov_item = 13
cov_cust = str(cov_cust) + " M"

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), cov_item,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Avg. Inv/D Box ------------------------
left, width = .504, .16
bottom, height = 0, .45
right = left + width
top = .4

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Avg. Inv/D' + "\n"
avg_inv = 2
avg_inv = str(avg_inv) + " M"

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), avg_inv,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Stock Box ------------------------
left, width = .672, .16
bottom, height = 0, .45
right = left + width
top = .4

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Stock' "\n"
stock = 3
stock = str(stock) + " M"

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), stock,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# ---------- Total Cust. Box ------------------------
left, width = .84, .16
bottom, height = 0, .45
right = left + width
top = .4

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Total Cust.' + "\n"
cust = 3500
cust = str(cust) + " M"


ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), cust,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

plt.tight_layout()
plt.savefig('kpi.png')
# plt.show()

