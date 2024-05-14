import random

pocet_kol = random.randint(1,15)

delka_pole = random.randint(5,10)

print(f"počet kol: {pocet_kol}")


body = 0

for kolo in range(1, pocet_kol + 1):
    print(f"\nKolo {kolo}")

    while True:
        odpoved = input("hadej  delku pole: ")
        if odpoved.lower() == "konec":
            print(f"konec hry, celkovy počet bodu: {body}")
            quit()
        if not odpoved.isdigit():
            print("zadejte cele čislo, nebo 'konec' pro ukončení")
            continue
        odpoved = int(odpoved)
        if odpoved == delka_pole:
            print("spravně!")
            body += 1
            break
        else:
            print("špatně")