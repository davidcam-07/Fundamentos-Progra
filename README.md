# Fundamentos-Proga Proyecto Monitor de Criptomonedas
Mi github de la clase de Fundamentos de la programación.
Las criptomonedas son conocidas por ser un activo financiero que es de los más volatiles existentes, lo que significa que de un minuto a otro puede haber un cambio grande en su valor, lo que hace que si quieres visualizar varias monedas termines cansado de tener varias graficas abiertas, o no podrás prestarle la atención necesaria a cada una. Este proyecto lo hago porque me interesa poder ver datos en tiempo real con un equipo hecho pro mí, así como ver el análisis de tendencias en una interfaz visual y aplicar algunos de los conocimientos de POO que ya tengo. Esto tiene el fin de poder ayudar a una persona a monitorear el valor de su portafolio y recibir alertas cuando un valor cruce cierto precio marcado.

**ALGORITMO**
1.Inicio
2.Cargar portafolio guardado
3. Mostrar menu al usuario:
 3.1Agregar criptomoneda
 3.2 Quitar criptomoneda
 3.3 Actualizar precios 
 3.4 Ver historial 
 3.5 Configurar alarma de precios
 3.6 Ver alertas actovas
 3.7 Salior
4. Dependiendo de la opcion elegida:
 -Si agrega: pedir simbolo del activo, validar que exista, añadirlo al portafolio
 -Si quita: pedir simbolo, eliminarlo del portafolio si existe
 -Si actualiza precio: para cada activo en el portafolio, obtener precio actual, guardar el nuevo dato en el historial local
 -Si consulta historia: pedir simbolo, calcular variacion entre primer y ultimo precio guardado, mostrar tendencia
 -Si configura alerta: pedir simbolo, tipo de alerta (sube de x valor / baja de x valor), guardar la alerta asociada al activo
 -Si revisa alertas: Comparar precio actual del activo contra la alerta configurada: si se cumple la condición, notificar
5. Guardar cambios del portafolio y del historial antes de salir
6. Repetir desde el paso 3 hasta que el usuario decida salir
7. Fin del programa

**Aclaracion**
Esta es mi idea inicial del proyecto, me gustaría configurarlo para que se corra de manera automática cada cierto tiempo, pero no sé lo que eso conlleva de recursos ni de código, por lo que no lo anote como el punto final, pero me gustaría desarrollarlo a eso.
