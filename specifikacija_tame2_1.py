import math

def read_positive_float(text):
    """Nolasa pozitīvu skaitli"""
    while True:
        try:
            value = float(input(text))
            if value > 0:
                return value
            print("❌ Ievadiet skaitli, kas ir lielāks par 0")
        except ValueError:
            print("❌ Tas nav skaitlis")

def calculate_wallpaper(perimeter, roll_width, price):
    """Aprēķina tapešu ruļļu skaitu un kopējo cenu"""
    rolls = math.ceil(perimeter / roll_width)
    total_price = round(rolls * price, 2)
    return rolls, total_price

def calculate_linoleum(width, length, price):
    """Aprēķina linoleja platību un kopējo cenu"""
    area = width * length
    total_price = round(area * price, 2)
    return area, total_price


# ===== Datu ievade =====
platums = read_positive_float("Platums (m): ")
garums = read_positive_float("Garums (m): ")
augstums = read_positive_float("Augstums (m): ")

linoleja_cena = read_positive_float("Linoleja cena par m²: ")
tapetes_cena = read_positive_float("Tapešu cena par ruļli: ")

# ===== Aprēķini =====
perimetrs = 2 * (platums + garums)

tapetes_daudzums, tapetes_kopa = calculate_wallpaper(
    perimetrs,
    roll_width=0.5,
    price=tapetes_cena
)

linoleja_daudzums, linolejs_kopa = calculate_linoleum(
    platums,
    garums,
    linoleja_cena
)

# ===== Rezultātu izvade =====
print("\n--- Rezultāti ---")
print(f"Tapetes: {tapetes_daudzums} ruļļi, kopējā cena {tapetes_kopa} EUR")
print(f"Linolejs: {linoleja_daudzums:.2f} m², kopējā cena {linolejs_kopa} EUR")
