import random

delka_pole = random.randint(5,10)

print(f"delka pole je {delka_pole}")


while True:
    odpoved = input("hadej  delku pole: ")
    if odpoved.lower() == "konec":
        print("konec hry")
        break
    if not odpoved.isdigit():
        print("zadejte cele čislo, nebo 'konec' pro ukončení")
        continue
    odpoved = int(odpoved)
    if odpoved == delka_pole:
        print("spravně!")
        break
    else:
        print("špatně")