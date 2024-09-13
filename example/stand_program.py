menu={
    "披薩":300,
    "爆米花":200,
    "洋芋片":40,
    "可樂":60,
    "麵包":30
}
foodcar =[]
total=0
print("----菜單-----")
for item, price in menu.items():
    print(f"{item}:{price}")

while True:
    food = input("請輸入菜單中想要的食物(空白結束訂購):")
    if food == " ":
        break
    elif menu.get(food) is None:
        print("沒有賣")
    else:
        foodcar.append(food)
        total += menu.get(food)
        print(food, end="")
print(f"總共{total}元!")