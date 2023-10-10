from math import sqrt

# /*
#  * Crea una función que encuentre todos los triples pitagóricos
#  * (ternas) menores o iguales a un número dado.
#  * - Debes buscar información sobre qué es un triple pitagórico.
#  * - La función únicamente recibe el número máximo que puede
#  *   aparecer en el triple.
#  * - Ejemplo: Los triples menores o iguales a 10 están
#  *   formados por (3, 4, 5) y (6, 8, 10).
#  */

print("Elige un número límite: ")
limit = int(input())
tuple_list = []

# Versión O(n²)
for i in range(1, limit):
    for j in range(i+1, limit):
        value = pow(i,2) + pow(j, 2)
        if sqrt(value).is_integer() and sqrt(value) <= limit:
            tuple_list.append(i)
            tuple_list.append(j)
            tuple_list.append(int(sqrt(value)))

i=0
while i < len(tuple_list):
    print(f"({tuple_list[i]},{tuple_list[i+1]},{tuple_list[i+2]})")
    i = i+3
