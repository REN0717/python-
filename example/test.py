xs = []
totals= inscores=0


while inscores != -1:
    if inscores == "q" :
        break
    inscores = int(input("請學生輸入成績"))
    if inscores != -1 :
        xs.append(inscores)
        totals = sum(xs)
        avg = totals / len(xs)
        print(f"班上共有{len(xs)}學生,班上總成績={totals},平均成績={avg}")
