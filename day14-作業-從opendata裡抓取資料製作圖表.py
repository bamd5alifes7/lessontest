
import numpy as np
import matplotlib.pyplot as plt # 匯入matplotlib 的pyplot 類別，並設定為plt
from matplotlib.font_manager import FontProperties # 中文字體

from PIL import ImageTk, Image
import matplotlib.image as mpimg
import statistics
import xlwt
import xlrd
import matplotlib.pyplot as plt
import csv

# 換成中文的字體
# plt.rcParams['font.新細明體'] = ['SimSun']                     #（替換sans-serif字型）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False                      #（解決座標軸負數的負號顯示問題）

def ExcelGetIntValues(list1,list2,col1):
    with open('high_diamond_ranked_10min.csv', 'r',encoding="utf-8") as fin:
            read = csv.reader(fin, delimiter=',')
            header = next(read)   # 讀擋頭
            #print(header)
            x=0
            list1.clear()
            for row in read:
                #print(row[2])

                list1.append(int(x))                            # 第幾筆資料
                list2.append(float(row[col1]))                  # 取得 資料

                x=x+1
    return list1,list2

list1=[]

list2=[]
list3=[]
list4=[]
list5=[]

ExcelGetIntValues(list1,list2,2)                                # 取得 藍隊插眼 資料
ExcelGetIntValues(list1,list3,21)                               # 取得 紅隊插眼 資料
ExcelGetIntValues(list1,list4,20)                               # 取得 藍隊每分鐘經濟 資料
ExcelGetIntValues(list1,list5,39)                               # 取得 藍隊每分鐘經濟 資料

print("藍隊最多插眼數量",max(list2))
print("藍隊最少插眼數量",min(list2))
avg_value = 0 if len(list2) == 0 else sum(list2)/len(list2)
print("藍隊平均插眼數量",avg_value)
print("藍隊插眼中位數",statistics.median(list2))

print("藍隊最高每分鐘經濟",max(list4))
print("藍隊最低每分鐘經濟",min(list4))
avg_value1 = 0 if len(list4) == 0 else sum(list4)/len(list4)
print("藍隊每分鐘經濟平均",avg_value1)
print("藍隊每分鐘經濟中位數",statistics.median(list4))


# 3. 畫出圖表

fig, ax = plt.subplots(figsize = (16, 10),nrows=2, ncols=3)   # 設定視窗 寬14英吋長8英吋 上下二分 左右三分


# 第一張圖表 藍隊插眼數據

ax[0,0].scatter(list1,
                list2,
                label="藍隊插眼數量")
ax[0,0].set_ylabel('數量')
ax[0,0].set_xlabel('場次')
ax[0,0].legend()

# 第二張圖表 藍隊插眼數據

ax[0,1].plot(list1,
             list3,"ro",
             label="紅隊插眼數量")
ax[0,1].set_ylabel('數量')
ax[0,1].set_xlabel('場次')
ax[0,1].legend()

# 第三張圖表 兩隊插眼數據比較

ax[0,2].plot(list1,
             list2,"b",
             label="藍隊插眼數量")

ax[0,2].plot(list1,
             list3,"r",
             label="紅隊插眼數量")

ax[0,2].set_ylabel('數量')
ax[0,2].set_xlabel('場次')
ax[0,2].legend()

# 第四張圖表 藍隊每分鐘經濟

ax[1,0].plot(list1,
             list4,"b*",
             label="藍隊每分鐘經濟")

ax[1,0].set_ylabel('金額')
ax[1,0].set_xlabel('場次')
ax[1,0].legend()

# 第五張圖表 紅隊每分鐘經濟

ax[1,1].plot(list1,
             list5,"r*",
             label="紅隊每分鐘經濟")

ax[1,1].set_ylabel('金額')
ax[1,1].set_xlabel('場次')
ax[1,1].legend()


# 第五張圖表 紅隊每分鐘經濟

ax[1,2].plot(list1,
             list4,
             label="藍隊每分鐘經濟")
ax[1,2].plot(list1,
             list5,"r",
             label="紅隊每分鐘經濟")

ax[1,2].set_ylabel('金額')
ax[1,2].set_xlabel('場次')
ax[1,2].legend()



plt.show()
