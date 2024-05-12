
import matplotlib.pyplot as plt

"""
Example txt

Positive,0.6837515830993652
Positive,0.8969659805297852
Nagetive,0.4694402515888214
Positive,0.8963819146156311
Positive,0.8939884305000305

"""

PresultFileName = r"TestResults\Real_0dBPositiveTest.txt"
# PresultFileName = r"TestResults\Real_5dBPositiveTest.txt"
# PresultFileName = r"TestResults\Real_30dBPositiveTest.txt"
Presults = []
with open(PresultFileName,"r") as f:
    rows = f.readlines()
    for row in rows:
        row = row.strip('\n')
        res = row.split(',')
        res[1] = float(res[1])
        Presults.append(res)

pos = []
nag = []

for res in Presults:
    if res[0] == "Positive": pos.append(res[1])
    else : nag.append(res[1])

print("Positive Counts : ",len(pos))
print("Negative Counts : ",len(nag))

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签



plt.subplot(2,1,1)
plt.title("辨识正确唤醒词可信度分布")
plt.ylabel("个数")
plt.hist(pos,bins=10)
# plt.show()

plt.subplot(2,1,2)
plt.title("辨识错误唤醒词可信度分布")
plt.ylabel("个数")
plt.hist(nag,bins=10)

plt.tight_layout()
plt.show()
