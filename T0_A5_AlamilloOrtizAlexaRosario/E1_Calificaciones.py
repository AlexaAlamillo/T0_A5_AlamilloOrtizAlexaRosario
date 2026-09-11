print("Ingrese el numero de califcaciones a promediar: ")
cantidad = int(input()) 

vector_calificaciones = []

suma =0.0

suma_apro =0

contador =0
contador_mayor = 0
suma_mayor=0

for i in range(cantidad):
    print(f"Ingrese calificacion {i+1}: ")
    vector_calificaciones.append(float(input())) 
    suma = suma + vector_calificaciones[i]
promedio =suma / cantidad
for j in range(cantidad):
    if ( vector_calificaciones[j] > 70 ):
        contador +=1
        suma_apro = suma_apro + vector_calificaciones[j]
        
for w in range(cantidad):
    if(vector_calificaciones[w]>promedio):
        contador_mayor+=1
        suma_mayor = suma_mayor + vector_calificaciones[w]
      
         

print(contador)  
print(f"El promedio general es: {promedio}")
print(f"El promedio de calificaciones mayores: {suma_apro/ contador  } ")
print(f"Promedio de calificaciones mayores al promedio general:  {suma_mayor/contador_mayor}")
     
