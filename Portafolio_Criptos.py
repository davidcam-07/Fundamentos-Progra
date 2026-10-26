# Proyecto de clase
# Supuesto: cantidad de dinero invertido (en USD) en distintas criptomonedas

import urllib.request
import json

API_KEY = "TU_API_KEY"  # placeholder
DIAS = 7 #Los ultimos 7 dias se piden a la API 

#Listas
nombres = ["Bitcoin", "Ethereum", "Solana"]
ids_api = ["bitcoin", "ethereum", "solana"] #nombre de la api en el mercado
inversiones = [250.50, 180.00, 75.25]


# Supuesto: precio al que se compró la cripto
precios_compra= [60000.00, 2400.00, 140.00]


def calcular_total(lista_montos):
    total = 0
    for monto in lista_montos:
        total = total + monto
    return total


def calcular_porcentaje(monto, total):
    return (monto / total) * 100
    
def calcular_porcentajes(lista_montos, total):
    porcentajes = []
    for monto in lista_montos:
        porcentajes.append(calcular_porcentaje(monto, total))
    return porcentajes


def calcular_mayor_inversion(lista_montos):
    mayor = lista_montos[0]
    for monto in lista_montos:
        if monto > mayor:
            mayor = monto
    return mayor
    
def calcular_promedio(fila):
    suma = 0
    for precio in fila:
        suma = suma + precio
    return suma / len(fila)

def calcular_ganancia(inversion, precio_compra, precio_actual):
    valor_actual = inversion * (precio_actual / precio_compra)
    return valor_actual - inversion
    
def obtener_precios_historicos(id_cripto):
    # Pide a CoinGecko los precios diarios de los últimos DIAS días
    url = (f"https://api.coingecko.com/api/v3/coins/{id_cripto}/market_chart"
           f"?vs_currency=usd&days={DIAS}&interval=daily")
    # Si hay una key real se agrega, si no, se usa la API pública sin key para que corra igual
    if API_KEY != "TU_API_KEY":
        url = url + f"&x_cg_demo_api_key={API_KEY}"
    try:
        with urllib.request.urlopen(url, timeout=10) as respuesta:
            datos = json.loads(respuesta.read())
    except Exception as error:
        print(f"Error al consultar {id_cripto}: {error}")
        return None
    if "prices" not in datos:
        return None
    precios = []
    for punto in datos["prices"]:  # cada punto es [fecha, precio]
        precios.append(punto[1])
    return precios[-DIAS:]

def construir_matriz_precios(lista_ids):     # Matriz: una fila por criptomoneda, una columna por día
    matriz = []
    for id_cripto in lista_ids:
        fila = obtener_precios_historicos(id_cripto)
        if fila is None:
            return None
        matriz.append(fila)
    return matriz

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ver inversiones individuales")
    print("2. Ver porcentajes por activo")
    print("3. Ver inversión total")
    print("4. Ver la mayor inversión")
    print("5. Ver historial de precios")    
    print("6. Salir")



def mostrar_inversiones(lista_nombres, lista_montos):
    for i in range(len(lista_nombres)):
        print(f"{lista_nombres[i]}: ${lista_montos[i]:.2f}")



def mostrar_porcentajes(lista_nombres, lista_porcentajes):
    for i in range(len(lista_nombres)):
        print(f"{lista_nombres[i]}: {lista_porcentajes[i]:.1f}%")


def mostrar_total(total):
    print(f"Inversión total: ${total:.2f}")


def mostrar_mayor_inversion(mayor):
    print(f"La mayor inversión individual es de: ${mayor:.2f}")


def mostrar_ganancias(lista_nombres, lista_inversiones, lista_compras, matriz):
    print("\nEstado actual de tus inversiones:")
    for i in range(len(lista_nombres)):
        precio_actual = matriz[i][-1]  # último día = precio más reciente
        ganancia = calcular_ganancia(lista_inversiones[i], lista_compras[i], precio_actual)
        print(f"{lista_nombres[i]}: precio actual ${precio_actual:.2f}")
        if precio_actual > lista_compras[i]:
            print(f"  Va en ganancia: +${ganancia:.2f}")
        elif precio_actual < lista_compras[i]:
            print(f"  Va en pérdida: -${abs(ganancia):.2f}")
        else:
            print("  Sin cambios.")

def mostrar_historial(lista_nombres, matriz):
    print("\nHistorial de precios en USD (el último día es el más reciente)")
    encabezado = " " * 10
    for dia in range(len(matriz[0])):
        etiqueta = "Día " + str(dia + 1)
        encabezado = encabezado + f"{etiqueta:>11}"
    print(encabezado)
    for i in range(len(matriz)):
        linea = f"{lista_nombres[i]:<10}"
        for j in range(len(matriz[i])):
            linea = linea + f"{matriz[i][j]:>11.2f}"
        print(linea)

def mostrar_tendencias(lista_nombres, matriz):
    print("\nTendencia en el periodo:")
    for i in range(len(matriz)):
        primero = matriz[i][0]
        ultimo = matriz[i][-1]
        promedio = calcular_promedio(matriz[i])
        if ultimo > primero:
            tendencia = "al alza"
        elif ultimo < primero:
            tendencia = "a la baja"
        else:
            tendencia = "estable"
        print(f"{lista_nombres[i]}: {tendencia} (precio promedio ${promedio:.2f})")
 

# Programa principal
inversion_total = calcular_total(inversiones)

porcentajes = calcular_porcentajes(inversiones, inversion_total)

mayor_inversion = calcular_mayor_inversion(inversiones)

# Consulta del precio actual al iniciar el programa y general la matrizz de precios de las 3 criptos y los DIAS

print("Consultando precios en CoinGecko...")
matriz_precios = construir_matriz_precios(ids_api)
if matriz_precios is None:
    print("No se pudieron obtener los precios. La opción 5 no tendrá datos.")
else:
    mostrar_ganancias(nombres, inversiones, precios_compra, matriz_precios)

opcion = ""
while opcion != "6":
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_inversiones(nombres, inversiones)
    elif opcion == "2":
        mostrar_porcentajes(nombres, porcentajes)
    elif opcion == "3":
        mostrar_total(inversion_total)
    elif opcion == "4":
        mostrar_mayor_inversion(mayor_inversion)
    elif opcion == "5":
        if matriz_precios is None:
            print("No hay datos de precios disponibles.")
        else:
            mostrar_historial(nombres, matriz_precios)
            mostrar_tendencias(nombres, matriz_precios)
    elif opcion == "6":
        print("Saliendo del programa...")

    else:
        print("Opción no válida, intenta de nuevo.")
