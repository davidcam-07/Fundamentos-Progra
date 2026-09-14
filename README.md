# Fundamentos-Proga Proyecto Monitor de Criptomonedas
Mi github de la clase de Fundamentos de la programación.
Las criptomonedas son conocidas por ser un activo financiero que es de los más volatiles existentes, lo que significa que de un minuto a otro puede haber un cambio grande en su valor, lo que hace que si quieres visualizar varias monedas termines cansado de tener varias graficas abiertas, o no podrás prestarle la atención necesaria a cada una. Este proyecto lo hago porque me interesa poder ver datos en tiempo real con un equipo hecho pro mí, así como ver el análisis de tendencias en una interfaz visual y aplicar algunos de los conocimientos de POO que ya tengo. Esto tiene el fin de poder ayudar a una persona a monitorear el valor de su portafolio y recibir alertas cuando un valor cruce cierto precio marcado.

**ALGORITMO**
```text
Entradas

- Monto invertido en Bitcoin (USD)
- Monto invertido en Ethereum (USD)
- Monto invertido en Solana (USD)
- Opción seleccionada por el usuario en el menú (número del 1 al 5)
Procesos

Procesos
1. Inicio
2. Definir el monto invertido en Bitcoin, Ethereum y Solana
3. Calcular la inversión total sumando los tres montos
4. Calcular el porcentaje que representa cada criptomoneda respecto al total
5. Calcular cual es la mayor inversión individual
6. Mostrar el menú de opciones al usuario
7. Leer la opción ingresada por el usuario
8. Si la opción es 1:
   8.1. Mostrar el monto invertido en Bitcoin
   8.2. Mostrar el monto invertido en Ethereum
   8.3. Mostrar el monto invertido en Solana
9. Si la opción es 2:
   9.1. Mostrar el porcentaje de Bitcoin respecto al total
   9.2. Mostrar el porcentaje de Ethereum respecto al total
   9.3. Mostrar el porcentaje de Solana respecto al total
10. Si la opción es 3:
    10.1. Mostrar el monto total invertido
11. Si la opción es 4:
    11.1. Mostrar el monto de la mayor inversión individual
12. Si la opción es 5:
    12.1. Mostrar mensaje de despedida
    12.2. Finalizar el programa
13. Si la opción no corresponde a ninguna de las anteriores:
    13.1. Mostrar mensaje de opción no válida
14. Repetir desde el paso 6 mientras la opción no sea 5
15. Fin

Salidas
- Monto invertido en cada criptomoneda individualmente
- Porcentaje que representa cada criptomoneda del total invertido
- Monto total invertido
- Monto de la mayor inversión individual
- Mensaje de despedida al salir del programa
```
**Aclaracion**
Esta es mi idea inicial del proyecto, me gustaría configurarlo para que se corra de manera automática cada cierto tiempo, pero no sé lo que eso conlleva de recursos ni de código, por lo que no lo anote como el punto final, pero me gustaría desarrollarlo a eso.
