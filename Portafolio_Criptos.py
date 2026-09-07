#Inversion en Dlrs
inversion_bitcoin = 250.50
inversion_ethereum = 180.00
inversion_solana = 75.25

inversion_total = inversion_bitcoin + inversion_ethereum + inversion_solana

# Porcentaje que representa cada inversión del total
porcentaje_bitcoin = (inversion_bitcoin / inversion_total) * 100
porcentaje_ethereum = (inversion_ethereum / inversion_total) * 100
porcentaje_solana = (inversion_solana / inversion_total) * 100

# Comparación para saber cuál es la mayor inversión
mayor_inversion = inversion_bitcoin
if inversion_ethereum > mayor_inversion:
    mayor_inversion = inversion_ethereum
if inversion_solana > mayor_inversion:
    mayor_inversion = inversion_solana
opcion = ""
while opcion != "5":
    print("\n--- Menú ---")
    print("1. Ver inversiones individuales")
    print("2. Ver porcentajes por activo")
    print("3. Ver inversión total")
    print("4. Ver la mayor inversión")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Bitcoin: ${inversion_bitcoin:.2f}")
        print(f"Ethereum: ${inversion_ethereum:.2f}")
        print(f"Solana: ${inversion_solana:.2f}")
    elif opcion == "2":
        print(f"Bitcoin: {porcentaje_bitcoin:.1f}%")
        print(f"Ethereum: {porcentaje_ethereum:.1f}%")
        print(f"Solana: {porcentaje_solana:.1f}%")
    elif opcion == "3":
        print(f"Inversión total: ${inversion_total:.2f}")
    elif opcion == "4":
        print(f"La mayor inversión individual es de: ${mayor_inversion:.2f}")
    elif opcion == "5":
        print("Saliendo del programa...")
    else:
        print("Opción no válida, intenta de nuevo.")
