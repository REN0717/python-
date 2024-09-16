# 骰出後顯示總和圖案
#使用 Unicode 自原來製作骰子圖案

import random

dice_art = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐", # 0
        "│ ●   ● │", # 1
        "│ ●   ● │", # 2
        "│ ●   ● │", # 3
        "└───────┘", # 4
    ),
}

num_dice = int(input("請輸入要職幾個骰子:"))
dice=[]

for i in range(num_dice):
    dice_number = random.randint(1,6)
    dice.append(dice_number)
# print(dice)


def get_dice_number(number):
    for i in range(5):
        print (dice_art.get(number)[i])

# get_dice_number(5)

for i in dice:
    get_dice_number(i)
print("總和:", sum(dice))
