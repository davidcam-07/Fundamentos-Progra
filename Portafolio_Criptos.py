inversion_bitcoin = 250.50
inversion_ethereum = 180.00
inversion_solana = 75.25

def calcular_total(monto1, monto2, monto3):
    return monto1 + monto2 + monto3

def calcular_porcentaje(monto, total):
    return (monto / total) * 100

def calcular_mayor_inversion(monto1, monto2, monto3):
    mayor = monto1
    if monto2 > mayor:
        mayor = monto2
    if monto3 > mayor:
        mayor = monto3
    return mayor

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ver inversiones individuales")
    print("2. Ver porcentajes por activo")
    print("3. Ver inversión total")
    print("4. Ver la mayor inversión")
    print("5. Salir")

def mostrar_inversiones(monto1, monto2, monto3):
    print(f"Bitcoin: ${monto1:.2f}")
    print(f"Ethereum: ${monto2:.2f}")
    print(f"Solana: ${monto3:.2f}")

def mostrar_porcentajes(porc1, porc2, porc3):
    print(f"Bitcoin: {porc1:.1f}%")
    print(f"Ethereum: {porc2:.1f}%")
    print(f"Solana: {porc3:.1f}%")

def mostrar_total(total):
    print(f"Inversión total: ${total:.2f}")

def mostrar_mayor_inversion(mayor):
    print(f"La mayor inversión individual es de: ${mayor:.2f}")

inversion_total = calcular_total(inversion_bitcoin, inversion_ethereum, inversion_solana)
porcentaje_bitcoin = calcular_porcentaje(inversion_bitcoin, inversion_total)
porcentaje_ethereum = calcular_porcentaje(inversion_ethereum, inversion_total)
porcentaje_solana = calcular_porcentaje(inversion_solana, inversion_total)
mayor_inversion = calcular_mayor_inversion(inversion_bitcoin, inversion_ethereum, inversion_solana)

opcion = ""
while opcion != "5":
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_inversiones(inversion_bitcoin, inversion_ethereum, inversion_solana)
    elif opcion == "2":
        mostrar_porcentajes(porcentaje_bitcoin, porcentaje_ethereum, porcentaje_solana)
    elif opcion == "3":
        mostrar_total(inversion_total)
    elif opcion == "4":
        mostrar_mayor_inversion(mayor_inversion)
    elif opcion == "5":
        print("Saliendo del programa...")
    else:
        print("Opcion no válida, usa una opcion del 1 al 5.")
