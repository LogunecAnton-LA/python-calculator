while True:
    num1 = int(input("Die erste Zahl: "))
    num2 = int(input("Die zweite Zahl: "))
    print("Gra: *, /, +, -")
    gra = input("Wählen Sie sich einen Gra aus: ")
    if gra == "*":
        print("Das Produkt: ", num1 * num2)
    elif gra == "/":
        if num2 == 0:
            print("Unmögliche Rechnung")
            continue
        else:
            print("Der Quotient: ", num1 / num2)
    elif gra == "+":
        print("Die Summe: ", num1 + num2)
    elif gra == "-":
        print("Die Differenz: ", num1 - num2)
    else:
        print("Unbekannte Rechnung")


