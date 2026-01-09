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

def calculate_linoleum(width, length, price, roll_width, roll_length):
    """Aprēķina linoleja platību, kopējo cenu un nepieciešamo ruļļu skaitu"""
    area = width * length
    total_price = round(area * price, 2)
    roll_area = roll_width * roll_length
    rolls_needed = math.ceil(area / roll_area)
    return area, total_price, rolls_needed

# ===== Datu ievade =====
print("--- Telpas izmēri ---")
platums = read_positive_float("Platums (m): ")
garums = read_positive_float("Garums (m): ")
augstums = read_positive_float("Augstums (m): ")

print("\n--- Materiālu cenas ---")
linoleja_cena = read_positive_float("Linoleja cena par m²: ")
tapetes_cena = read_positive_float("Tapešu cena par ruļli: ")

print("\n--- Linoleja ruļļa izmēri ---")
roll_width = read_positive_float("Ruļļa platums (m): ")
roll_length = read_positive_float("Ruļļa garums (m): ")

# ===== Aprēķini =====
perimetrs = 2 * (platums + garums)

tapetes_daudzums, tapetes_kopa = calculate_wallpaper(perimetrs, roll_width=0.5, price=tapetes_cena)
linoleja_daudzums, linolejs_kopa, linoleja_rulli = calculate_linoleum(
    platums, garums, linoleja_cena, roll_width, roll_length
)

# ===== Rezultātu izvade =====
print("\n================== REZULTĀTI ==================")
print(f"{'Materiāls':<15}{'Daudzums':<20}{'Cena EUR':<10}{'Papildus info'}")
print("-"*60)
print(f"{'Tapešu ruļļi':<15}{tapetes_daudzums:<20}{tapetes_kopa:<10}{'Ruļļa platums 0.5 m'}")
print(f"{'Linolejs':<15}{linoleja_daudzums:.2f} m²{'':<9}{linolejs_kopa:<10}{linoleja_rulli} ruļļi ({roll_width}x{roll_length} m)")
print("================================================")
