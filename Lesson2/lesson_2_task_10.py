def bank(x, y):
    for i in range(1, y+1):
        count = x + (x/10)
        x = count
        print(round(count))


x = int(input("Введите сумму вклада: "))
y = int(input("Введите срок вклада: "))

bank(x, y)
