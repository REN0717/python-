import random
# randint
#print(random.randint(1,10))

# 隨機選擇一個元素
# x = ["剪刀","石頭","布"]
# random_x = random.choice(x)
# print("電腦出的是",random_x)


#將列表打亂
# cards=["2","3","4","5","6","7","8","9"]
# random.shuffle(cards)
# print(cards)

low = 1
high=100
num = random.randint(low,high)
guesses=0

while True:
    guess=int(input("猜一個介於{low}~{high}的數字:"))
    guesses += 1
    if guess < num:
        print("在大一點")
    elif guess > num:
        print("在小一點")
    else:
        print(f"猜對了~ ,你的數字是{num}")
        print(f"你猜了{guesses}次")
        break