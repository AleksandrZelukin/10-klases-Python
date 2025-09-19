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
        lives -= 1
        score -= 20
        print("Tu zaudē dzīvību!", lives, score)
    elif durvis[speletajs] == "Dzivais ūdens":
        lives += 1
        score += 10
        print("Apsveicu, tu esi izdzīvojis!", lives, score)
    elif durvis[speletajs] == "Nekas":
        print("Tu uzminēji! Apsveicu, tu esi izdzīvojis!", lives, score)

    # Pārbauda, vai spēle ir beigusies
    if lives == 0 or score < 0:
        print("Spēle beigusies! Tev ir", lives, "dzīvības un", score, "punkti.")
        break
