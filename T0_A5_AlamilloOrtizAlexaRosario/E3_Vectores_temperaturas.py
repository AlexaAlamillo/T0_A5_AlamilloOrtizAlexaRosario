print("Ingrese el numero de temperaturas: ")
num_tem = int(input())
vector_temperaturas=[]
for i in range(num_tem):
    print(f"Ingrese temperatura {i+1}: ")
    vector_temperaturas.append(float(input()))


print(vector_temperaturas)

for j in range(num_tem): 
    if ( vector_temperaturas[j]>0):
        print(f"Temperaturas Mayores:{vector_temperaturas[j]} ")
 
print()          
for k in range(num_tem): 
    if ( vector_temperaturas[k]<0):
        print(f"Temperaturas Menores:{vector_temperaturas[k]} ")
           