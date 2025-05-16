# for, while
from itertools import count

for i in range(10):
    print("i is:", i)

print("==========================================")
for i in range(5, 10):
    print("i is:", i)

print("==========================================")
nameList = ["Ashibul", "Nazim", "Lucky", "sojib"]
for name in nameList:
    print(name)

print("==========================================")
numberSet = {98, 32, 54, 87, 100}
for x in numberSet:
    print(x)

print("==========================================")
count = 0
while count <= 10:
    print("Count is", count) #0, 3, 6, 9
   # count+=3 # 0+3=3, 3+3=6, 6+3=9, 9+3=12
