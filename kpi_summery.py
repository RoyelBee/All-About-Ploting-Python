import matplotlib.patches as patches
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pyodbc as db
import numpy as np

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=10.168.2.241;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp')
cursor = connection.cursor()

sales_target_df = pd.read_sql_query("""Select [TARGET] from [dbo].[TDCL_BranchTarget]
        where YEARMONTH = 201912 and AUDTORG = 'COXSKF'
    """, connection)
return_df = pd.read_sql_query(""" Declare @CurrentMonth NVARCHAR(MAX);
            SET @CurrentMonth = convert(varchar(6), GETDATE(),112);
            select Sum(Case when transtype<>1 then EXTINVMISC end )*-1/Sum(Case when transtype=1 then EXTINVMISC end )*100 as  ReturnP from OESalesDetails  
                where LEFT(TRANSDATE,6) = @CurrentMonth and AUDTORG='BSLSKF'
    """, connection)


# ----------------------------------------
# -----------  KPI summery Start ---------
# ----------------------------------------
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


# --------------------  Target Box --------------------------------
target_data = sales_target_df['TARGET']
target = int(target_data)
print('Target is =', target)
target_data = int(round(target_data / 1000000))

kpi_label = 'Target' + "\n"
target_data = str(target_data) + " M"

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), target_data,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)
#
# # ---------- Sales Box ------------------------
sales_df = pd.read_sql_query("""Declare @CurrentMonth NVARCHAR(MAX);
DECLARE @date DATETIME = GETDATE();
        SET @CurrentMonth = convert(varchar(6), GETDATE(),112);

        select CONVERT(VARCHAR(2), getdate(), 106)-1 as 'current_date', DAY(EOMONTH ( @date )) AS 'days_in_current_month',
		 Sum(EXTINVMISC) as  MTDSales from OESalesDetails  
            where LEFT(TRANSDATE,6) = @CurrentMonth and AUDTORG='BSLSKF'
            """, connection)

sales = sales_df['MTDSales']
actual_sales = float(sales)
print('sales = ', actual_sales)
rounded_sales = int(round(actual_sales / 1000000))




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
rounded_sales = str(rounded_sales) + ' M'

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), rounded_sales,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)


# # ---------- Sales Achievement Box ------------------------
left, width = .336, .16
bottom, height = .5, .5
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )
ax.add_patch(p)

kpi_label = 'Achievement' + "\n"
acv = int(round((actual_sales/target) * 100))
print('achievement =', acv)
acv = str(acv) + " %"


ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), acv,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)


# # ---------- Sales Trend Box ------------------------
left, width = .504, .16
bottom, height = .5, .5
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)

kpi_label = 'Sales Trend' + "\n"
day = int(sales_df['current_date'])
day_in_months = int(sales_df['days_in_current_month'])
trend = (sales/day) * day_in_months
trend = int(round(trend / 1000000))
trend = str(trend) + " M"

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .4*(bottom+top), trend,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)
#
# # ---------- Average Sales Box ------------------------
left, width = .672, .16
bottom, height = .5, .5
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Avg Sales /D' + "\n"
avg_sales = actual_sales/day
avg_sales_in_m = int(round(avg_sales / 1000000))
print('avg sales = ', avg_sales_in_m)

avg_sales = str(avg_sales_in_m) + ' M'

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

# # ---------- Sales Growth Box ------------------------
previous_month_sales_df = pd.read_sql_query("""
    select  sum(EXTINVMISC) as PreviousMonth 
                    from OESalesDetails 
                    where TRANSDATE between
                     (convert(varchar(8),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()) - 1, 0),112)) 
                     and 
                    (convert(varchar(8),dateadd(month, -1, GETDATE()-1),112))
            """, connection)

current_month_sales_df = pd.read_sql_query("""
    select  sum(EXTINVMISC) as CurrentMonth 
                      from OESalesDetails 
                      where TRANSDATE between 
                      (convert(varchar(8),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112)) 
                      and 
                      (convert(varchar(8),DATEADD(D,-1,GETDATE()),112))

            """, connection)

previous_month_sales = previous_month_sales_df['PreviousMonth']
current_month_sales = current_month_sales_df['CurrentMonth']
previous_sales = int(previous_month_sales)
current_sales = int(current_month_sales)
sales_growth = round((((current_sales - previous_sales) / previous_sales) * 100), 2)

print('Previous month sales =', previous_sales)
print('current month sales =', current_sales)
print('sales growth = ', sales_growth)


left, width = .84, .16
bottom, height = .5, .5
right = left + width
top = 1

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )


ax.add_patch(p)
kpi_label = 'Sales Growth' + "\n"

sales_growth = str(sales_growth) + ' %'


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

# ---------------------------------------------------
# ----------------Row 2 boxes -----------------------
# ---------------------------------------------------

# ------ Row two Boxes configurations ---------------
left, width = 0, .16
bottom, height = 0, .45
right = left + width
top = .4


# # ---------- Return % Box ------------------------
p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Return Growth' + "\n"
return_p = float(return_df['ReturnP'])
return_p = format(return_p, '.2f')

return_p = str(return_p) + " %"

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), return_p,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

# # ---------- Cov. Item Box ------------------------
total_item_df = pd.read_sql_query("""
    select count(DISTINCT(ITEMNO)) as Total_Item from  ICITEM 
    """, connection)
covered_item_df = pd.read_sql_query(""" 
select count(DISTINCT(ITEM)) as MTD_Item from OESalesDetails
            where 
            AUDTORG = 'MIRSKF' AND
            TRANSDATE between 
            (convert(varchar(8),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112)) 
            and 
            convert(varchar(8),DATEADD(D,-1,GETDATE()),112) 

""", connection)
total_item = int(total_item_df['Total_Item'])
covered_item = int(covered_item_df['MTD_Item'])


left, width = .168, .16
bottom, height = 0, .45
right = left + width
top = .4

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Cov. Item' + "\n"
total_item = str(total_item)
covered_item = str(covered_item)
item_status = covered_item + ' / ' + total_item


ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), item_status,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=28, color='red',
        transform=ax.transAxes)
#
# # ---------- Cov. Item % Box ------------------------
# left, width = .336, .16
# bottom, height = 0, .45
# right = left + width
# top = .4
#
# p = patches.Rectangle(
#     (left, bottom), width, height,
#     color='#b0d2cd'
#     )
#
# ax.add_patch(p)
# kpi_label = 'Cov. Item %' + "\n"
# cov_item = 13
# cov_cust = str(cov_cust) + " M"
#
# ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
#         horizontalalignment='center',
#         verticalalignment='center',
#         fontsize=24, color='black',
#         transform=ax.transAxes)
#
# ax.text(.5*(left+right), .3*(bottom+top), cov_item,
#         horizontalalignment='center',
#         verticalalignment='center',
#         fontsize=34, color='red',
#         transform=ax.transAxes)
#
# # ---------- Avg. Inv/D Box ------------------------
inv_df = pd.read_sql_query("""
   select count(distinct INVNUMBER ) as TotalInv from OESalesDetails
where AUDTORG = 'BOGSKF' and TRANSDATE = convert(varchar(8),DATEADD(D,-1,GETDATE()),112)
     """, connection)

total_inv = int(inv_df['TotalInv'])



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
# print('Total inv = ', total_inv)
# print('Day', day)
# print(type(day))
avg_inv = total_inv/day
# print('avg inv = ', avg_inv)
avg_inv = str(round(avg_inv))

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

# # ---------- Total Customer Box ------------------------
total_cust_df = pd.read_sql_query("""
	select DISTINCT(count(IDCUST)) as total_cuatomer 
    from CustomerInformation 
    where AUDTORG = 'BSLSKF'
            """, connection)

mtd_cust_df = pd.read_sql_query("""select count(DISTINCT(CUSTOMER)) as MTD_Customer from OESalesDetails
            where AUDTORG = 'BSLSKF' AND
            TRANSDATE between 
            (convert(varchar(8),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112)) 
            AND 
            convert(varchar(8),DATEADD(D,-1,GETDATE()),112)  
            """, connection)


total_customer = int(total_cust_df['total_cuatomer'])
mtd_customer = int(mtd_cust_df['MTD_Customer'])

total_customer = str(total_customer)
mtd_customer = str(mtd_customer)

left, width = .672, .16
bottom, height = 0, .45
right = left + width
top = .4

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Total Cust.' "\n"
customer_status = mtd_customer + ' / ' + total_customer

ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), customer_status,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=28, color='red',
        transform=ax.transAxes)

# # ---------- Outstanding Box ------------------------
out_std_df = pd.read_sql_query("""
        select sum(OUT_NET) as outstd from ARCOUT.dbo.CUST_OUT 
        where AUDTORG = 'BOGSKF'
        """, connection)


left, width = .84, .16
bottom, height = 0, .45
right = left + width
top = .4

p = patches.Rectangle(
    (left, bottom), width, height,
    color='#b0d2cd'
    )

ax.add_patch(p)
kpi_label = 'Outstanding' + "\n"
out_std = int(out_std_df['outstd'])
out_std = round(out_std/1000000)
out_std = str(out_std) + " M"


ax.text(.5*(left+right), .5*(bottom+top), kpi_label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=24, color='black',
        transform=ax.transAxes)

ax.text(.5*(left+right), .3*(bottom+top), out_std,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=34, color='red',
        transform=ax.transAxes)

plt.tight_layout()
plt.savefig('./kpi_summary.png')
# plt.show()
# # ------ KPI summery end -------------------------------------------
