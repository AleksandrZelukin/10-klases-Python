import random

def main():
    print("Laipni lūdzam Spoku spēlē!")
    print("Izvēlies grūtības līmeni:")
    print("1. Viegli")
    print("2. Vidēji")
    print("3. Grūti")

    while True:
        choice = input("Ievadi savu izvēli (1-3): ")
        if choice in ['1', '2', '3']:
            break
        print("Lūdzu, ievadi derīgu izvēli.")

    if choice == '1':
        max_number = 10
    elif choice == '2':
        max_number = 50
    else:
        max_number = 100

    secret_number = random.randint(1, max_number)
    attempts = 0

    while True:
        guess = input(f"Ievadi skaitli no 1 līdz {max_number}: ")
        if not guess.isdigit():
            print("Lūdzu, ievadi derīgu skaitli.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Par zemu! Mēģini vēlreiz.")
        elif guess > secret_number:
            print("Par augstu! Mēģini vēlreiz.")
        else:
            print(f"APSVEICAM! Tu uzminēji skaitli {secret_number} pēc {attempts} mēģinājumiem.")
            break

if __name__ == "__main__":
    main()# Spoku spēle - skaitļa minēšanas spēle ar grūtības līmeņiem