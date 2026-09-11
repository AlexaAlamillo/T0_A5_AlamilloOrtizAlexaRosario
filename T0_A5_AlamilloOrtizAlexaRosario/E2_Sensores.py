import random
from _socket import if_indextoname
print("=======Sensores encendidos y apagados======")

vector_sensores = []
vector_sensores = [random.choice([True, False]) for _ in range(24)]
contador_Verdadero = 0
contador_Falso= 0
abiertos_dia=0
cerrados_dia =0
abiertos_noche=0
cerrados_noche=0
for i in range(24):
    if (vector_sensores[i] == True):
        contador_Verdadero +=1
        if(i < 12):
            abiertos_dia+=1
        else:
            cerrados_dia+=1    
    else: 
        contador_Falso +=1 
        if(i<12):
            abiertos_noche+=1
        else:
            cerrados_noche+=1     
        
print(vector_sensores)        
print(f"Valores de TRUE: {contador_Verdadero}")  
print(f"Valores de FALSE: {contador_Falso}")
print(f"Valores de TRUE durante el dia: {abiertos_dia}")
print(f"Valores de FALSE durante el dia: {cerrados_dia}") 
print(f"Valores de TRUE por la noche: {abiertos_noche}")  
print(f"Valores de FALSE por la noche: {cerrados_noche}") 
if(abiertos_dia> cerrados_dia):
    print("Hubo mas sensores encendidos en el dia")
elif(cerrados_dia>abiertos_dia):
    print("Hubo mas sensores apagados en el dia")
else:
    print("Hubo la misma cantidad")        
   
   
if(abiertos_noche> cerrados_noche):
    print("Hubo mas sensores encendidos en la noche")
elif(cerrados_noche>abiertos_noche):
    print("Hubo mas sensores apagados en la noche")
else:
    print("Hubo la misma cantidad")        
       
