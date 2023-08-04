num1 = input("Dame un primer numero\n") 
num1 = int (num1)
num2 =int(input("Dame un segundo numero\n"))
num3 =int(input("Dame un tercer numero\n"))
print("Orden original", num1, num2, num3)

# import pdb; pdb.set_trace()
if num1>num2 and num1>num3 and num2>num3 :
    print("Ordenado: ",num1, num2, num3)
elif num1>num2 and num1>num3 and num2<num3 :
    print("Ordenado: ", num1, num3, num2)

elif num2>num1 and num2>num3 and num1>num3 :
    print("Ordenado: ",num2, num1, num3)
elif num2>num1 and num2>num3 and num1<num3 :
    print("Ordenado: ",num2, num3, num1)

elif num3>num1 and num3>num2 and num2>num1 :
    print("Ordenado: ",num3, num2, num1)
elif num3>num1 and num3>num2 and num2<num1 :
    print("Ordenado: ",num3, num1, num2)

######################################################################################

print("Ordenado con lista: ", sorted([num1,num2,num3], reverse=True))

######################################################################################

if num1>=num2 and num1>=num3 :
    if num2>=num3:
        print(num1, num2, num3)
    else :
        print(num1, num3, num2)
elif num2>=num1 and num2>=num3 :
    if num1>=num3:
        print(num2, num1, num3)
    else :
        print(num2, num3, num1)
else :
    if num1>=num2:
        print(num3, num1, num2)
    else :
        print(num3, num2, num1)