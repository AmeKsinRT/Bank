def trade(v1, v2, amount, direction):
    if direction == "BUY":
        if v1 == "RUB":
            if v2 == "EUR":
                amount1 = amount * 0.03
                return amount1
            elif v2 == "USD":
                amount1 = amount * 0.04
                return amount1
            else:
                print("С этой валютой не работаем")
        elif v1 == "EUR":
            if v2 == "RUB":
                amount1 = amount * 60
                return amount1
            elif v2 == "USD":
                amount1 = amount * 1.5
                return amount1
            else:
                print("С этой валютой не работаем.")
        elif v1 == "USD":
            if v2 == "RUB":
                amount1 = amount * 50
                return amount1
            elif v2 == "EUR":
                amount1 = amount * 1.5
                return amount1
            else:
                print("С этой валютой не работаем.")
        else:
            print("С этой валютой не работаем.")
    if direction == "SELL":
        if v1 == "RUB":
            if v2 == "EUR":
                print("Рубли можно только купить.")
                exit(12)
            elif v2 == "USD":
                print("Рубли можно только купить.")
                exit(12)
            else:
                print("С этой валютой не работаем.")
        elif v1 == "EUR":
            if v2 == "RUB":
                amount1 = amount * 50
                return amount1
            elif v2 == "USD":
                amount1 = amount * 1.4
                return amount1
            else:
                print("С этой валютой не работаем.")
        elif v1 == "USD":
            if v2 == "RUB":
                amount1 = amount * 45
                return amount1
            elif v2 == "EUR":
                amount1 = amount * 1.4
                return amount1
            else:
                print("С этой валютой не работаем.")
        else:
            print("С этой валютой не работаем.")

while True:
    print("Какая валюта в наличии?[RUB/EUR/USD]")
    v1 = str(input())
    if v1 != "RUB" and v1 != "EUR" and v1 != "USD":
        print("С этой валютой не работаем или введено не верное значение.")
        continue
    else:
        break
while True:
    print("Купить или продать?[SELL/BUY]")
    direction = str(input())
    if direction != "SELL" and direction != "BUY":
        print("Введено не верное значение.")
        continue
    else:
        if direction == "SELL" and v1 == "RUB":
            print("Рубли можно только купить")

        break
while True:
    print("Какая валюта нужна?[RUB/EUR/USD]")
    v2 = str(input())
    if v2 != "RUB" and v2 != "EUR" and v2 != "USD":
        print("С этой валютой не работаем или введено не верное значение.")
        continue
    else:
        break
while True:
    print("Сколько нужно обменять " + str(v1) + "?")
    try:
        amount = float(input())
        break
    except ValueError:
        print("Не верное значение")
        continue

print(trade(v1, v2, amount, direction))
