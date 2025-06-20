# Recolectamos el porcentaje
variacion = float(input('Ingrese el porcentaje de crecimiento: '))
# Verificamos si el valor es positivo o negativo con una comparación para ver si el número
# es mayor o menor que 0
if variacion > 0:
    print(f'Hubo un crecimiento del {variacion}%')
elif variacion < 0:
    print(f'Hubo un decrecimiento del {variacion}%')
else:
    print('No hubo crecimiento ni decrecimiento.')