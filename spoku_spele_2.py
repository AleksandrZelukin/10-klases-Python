from random import shuffle

durvis = ["Spoks", "Dzivais ūdens", "Nekas"]
lives = 1
score = 0

print("Izvēlies durvis, aiz kurām var būt spoks, dzīvā ūdens vai nekas!")

while True:
    print("Tev ir", lives, "dzīvības un", score, "punkti.")
    speletajs = input("Ievadi durvju numuru (1-3): ")

    # Pārbauda, vai ievade ir derīga
    if not speletajs.isdigit() or not (1 <= int(speletajs) <= 3):
        print("Nederīga izvēle! Ievadi skaitli no 1 līdz 3.")
        continue

    shuffle(durvis)
    speletajs = int(speletajs) - 1

    if durvis[speletajs] == "Spoks":
        print("Tu izvēlējies durvis ar spoku!")
        lives -= 1
        score -= 20
        print(f"Tu zaudē dzīvību! un tev {lives} dzīvības un {score} punktus")
    elif durvis[speletajs] == "Dzivais ūdens":
        print("Tu izvēlējies durvis ar dzivo ūdeni!")
        lives += 1
        score += 10
        print(f"Apsveicu, tu esi izdzīvojis! un tev {lives} dzīvibas un {score} punktus")
    elif durvis[speletajs] == "Nekas":
        print("Tu izvēlējies durvis ar neko!")
        print(f"Apsveicu, tu esi izdzīvojis! un tev {lives} dzīvibas un {score} punktus")
    # Pārbauda, vai spēle ir beigusies
    if lives == 0 or score < 0:
        print(f"Spēle beigusies! Tev ir {lives} dzīvības un {score} punkti.")
        break
