import random
import pyinputplus as pypi

min:int = 1
max:int = 100
count:int = 0

target:int = random.randint(min,max)
print("=======猜數字=======\n")
while(True):
    keyin:int = pypi.inputInt(f"猜數字範圍{min}~{max}:",min=min,max=max)

    count += 1
    if keyin == target:
       print(f"賓果!猜對了, 答案是:{keyin}")
       print("您猜了{count}次")
       break
    elif(keyin > target):
       print("再小一點")
       print("您已猜了{count}次")
    elif (keyin < target):
       print("再大一點")
       print("您已猜了{count}次")
print("遊戲結束")