#學生的總分為300
#有些學生可以加分5%

scores = int(input("請輸入學生分數(最高300分):"))
is_add = input("學生是否符合加分條件?(y,n)")
if is_add == "y":
   scoress *= 1.05

   print(f"學生分數是:{round(scores,ndigits=0)}")

   try:
       money = int(input("請輸入金額:"))
       print (money)
   except ValueError
       print("格式錯誤")
   print ("應用程式結束")