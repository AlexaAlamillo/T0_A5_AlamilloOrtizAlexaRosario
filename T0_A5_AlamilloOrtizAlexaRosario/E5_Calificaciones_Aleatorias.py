import random
print("Ingrese el numero de calificaciones: ")
numero = int(input())
contador =0

vector_calificaciones = []
for i in range(numero):
    vector_calificaciones.append(random.randint(0,100))
print(vector_calificaciones)
promedio =0
opcion =0
contador_mayor=0
contador_menor=0
while opcion!= 4:
    print("1) Obtener el promedio de calificaciones")
    print("2) Mostrar cuantas estan por encima del promedio y cuantas por debajo")
    print("3) Mostrar promedio de calificaciones aprobatorias y no aprobatorias")
    print("4) salir ")
    opcion= int(input("Opcion: "))
    if(opcion ==1):
        for w in range(numero):
            contador = contador + vector_calificaciones[w]
        promedio = contador / numero 
        print(f"El promedio de las calificaciones generadas es: {promedio}")
    elif(opcion==2):
        suma =0;
        for a in range(numero):
            if(vector_calificaciones[a]>promedio):
                contador_mayor+=1
            else: 
                contador_menor+=1
        print("====CALIFICACIONES MAYORESO MENORES AL PROMEDIO===")
        print(f"MAYORES: {contador_mayor} ")  
        print(f"MENORES: {contador_menor}")   
    elif(opcion==3):
        vector_aprobatorias =[]
        vector_reprobatorias=[]
        
        for e in range(numero):
            if(vector_calificaciones[e] >70):
                vector_aprobatorias.append(vector_calificaciones[e])
            else:
                vector_reprobatorias.append(vector_calificaciones[e])   
        print(f"CALIFICACIONES APROBATORIAS: {vector_aprobatorias}") 
        print(f"CALIFICACIONES REPROBATORIAS: {vector_reprobatorias}") 
        
        if (len(vector_aprobatorias)> 0):
            suma_aprobatorias =0
            for c in range(len(vector_aprobatorias)):
                suma_aprobatorias = suma_aprobatorias + vector_aprobatorias[c]
            promedio_apro = suma_aprobatorias/ len(vector_aprobatorias)    
            print(f"PROMEDIO DE CALIFICACIONES APROBATORIAS: {promedio_apro}") 
        else:
            print("No hay calificaciones aprobatorias")       
        if (len(vector_reprobatorias)> 0):
            suma_reprobatorias =0
            for r in range(len(vector_reprobatorias)):
                suma_reprobatorias = suma_reprobatorias + vector_reprobatorias[r]
            promedio_repro = suma_reprobatorias/ len(vector_reprobatorias)    
            print(f"PROMEDIO DE CALIFICACIONES APROBATORIAS: {promedio_repro}") 
        else:
            print("No hay calificaciones reprobatorias")        
              
    elif(opcion==4):
        print("Saliemndo del menu...")    
                
        
            
                  
    
        