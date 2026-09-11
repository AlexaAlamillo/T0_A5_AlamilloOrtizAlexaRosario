print("Ingrese el numero de temperaturas: ")
num = int(input())

vector_temperaturas = []

suma=0
for i in range(num):
    vector_temperaturas.append(float(input(f"Ingrese la temperatura en celsius {(i+1)} :")))
    suma = suma + vector_temperaturas[i]
promedio= suma/num
print(suma)
print(f"Promedio en grados celcius: {promedio}")

promedio_fahrenheit = (promedio * 1.8) +32
print(f"Promedio en grados Fahrenheit: {promedio_fahrenheit}")