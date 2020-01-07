import matplotlib.pyplot as plt
import numpy as np
import pyodbc as db
import pandas as pd

connection = db.connect('DRIVER={SQL Server};'
                        'SERVER=10.168.2.241;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp')

cursor = connection.cursor()
df = pd.read_sql_query("""DECLARE @TotalItem VARCHAR(20)
        SET @TotalItem = (SELECT count( distinct  ITEMNO) as TotalMovingItem FROM ICStockStatusCurrentLOT 
                      where  left(ITEMNO,1)<>'9' and AUDTORG<>'SKFDAT' and AUDTORG='BOG') 
        SELECT  LEFT(AUDTORG,3) AS AUDTORG,  --NDMNAME,
        ISNULL(Sum( CASE WHEN [Days]<=15 THEN 1 END),0) AS SUS
        ,ISNULL(Sum( CASE WHEN [Days]>15 AND [Days]<=35 THEN 1 END),0) AS US
        ,ISNULL(Sum( CASE WHEN [Days]>35 AND [Days]<=45 THEN 1 END),0) AS NS
        ,ISNULL(Sum( CASE WHEN [Days]>45 AND [Days]<=60 THEN 1 END),0) AS OS
        ,ISNULL(Sum( CASE WHEN [Days]>60 THEN 1 END),0) AS SOS
        ,@TotalItem-(ISNULL(Sum( CASE WHEN [Days]<=15 THEN 1 END),0)+ISNULL(Sum( CASE WHEN [Days]>15 AND [Days]<=35 THEN 1 END),0)+ISNULL(Sum( CASE WHEN [Days]>35 AND [Days]<=45 THEN 1 END),0)
        +ISNULL(Sum( CASE WHEN [Days]>45 AND [Days]<=60 THEN 1 END),0)+ISNULL(Sum( CASE WHEN [Days]>60 THEN 1 END),0)) AS NIL
        
        FROM
        
        ( SELECT  Stock.ITEMNO, Stock.AUDTORG, Sum(QTYONHAND) as QTYONHAND , Sum(QTYSHIPPED)as QTYSHIPPED --NDMNAME,
        ,CAST(ISNULL(CASE WHEN SUM(QTYSHIPPED)>0 THEN (SUM(QTYONHAND)+ISNULL(SUM(SIT),0))/(SUM(QTYSHIPPED)/90) END,0) AS INT) AS [Days]FROM
        -----
        (SELECT ITEMNO, AUDTORG, SUM(QTYONHAND) AS QTYONHAND FROM ICStockStatusCurrentLOT
        where LEN(LOCATION)>'3' AND left(ITEMNO,1)<>'9' AND AUDTORG <> 'SKFDAT'  and AUDTORG='BOG'
        GROUP BY ITEMNO, AUDTORG) AS Stock
        LEFT JOIN
        (SELECT ITEM, AUDTORG, SUM(QTYSHIPPED) AS QTYSHIPPED FROM OESalesDetails
        WHERE TRANSDATE BETWEEN CONVERT(varchar(8), GETDATE()-91,112) AND CONVERT(varchar(8), GETDATE()-1,112)
        and AUDTORG='BOG'
        GROUP BY ITEM, AUDTORG) AS Sales
        ON RTRIM(Stock.ITEMNO) = RTRIM(Sales.ITEM) AND RTRIM(Stock.AUDTORG) = RTRIM(Sales.AUDTORG)
        LEFT JOIN
        (SELECT ITEMNO, AUDTORG,SUM(QTY) AS SIT FROM GIT 
        WHERE OPENINGDATE = convert(varchar, getdate(), 23)
        and AUDTORG='BOG'
        GROUP BY ITEMNO, AUDTORG) as GIT 
        ON Stock.ITEMNO = GIT.ITEMNO AND Stock.AUDTORG=GIT.AUDTORG
        
        Group BY Stock.ITEMNO, Stock.AUDTORG) AS TX --NDMNAME,
        GROUP BY AUDTORG   --NDMNAME,
        ORDER BY  AUDTORG --NDMNAME  """, connection)

nil = int(df['NIL'])
ns = int(df['NS'])
os = int(df['OS'])
sos = int(df['SOS'])
us = int(df['US'])
sus = int(df['SUS'])

labels = ['NIL', 'NS', 'US', 'SUS', 'OS', 'SOS']
energy = [nil, ns, os, sos, us, sus]
# energy.reverse()
plt.figure(4)
x_pos = [i for i, _ in enumerate(labels)]

bars = plt.bar(x_pos, energy, width=0.5)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + 0.22, yval+8, yval, horizontalalignment='center', verticalalignment='center',
             fontsize=10)
bars[0].set_color('#ffd966')
bars[1].set_color('#548235')
bars[2].set_color('#f4b183')
bars[3].set_color('#843c0c')
bars[4].set_color('#2f5597')
bars[5].set_color('#333f50')
plt.xlabel("Stock Type")
plt.ylabel("Total Stocks")
plt.xticks(x_pos, labels, fontsize=14)
plt.title("Type Wise Stock", color='#db3838', fontsize='18', fontweight='bold')
plt.tight_layout()
plt.savefig('type_wise_stock.png')
plt.show()