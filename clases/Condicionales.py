x = 10
if True :
    print("Evaluacion verdadera")

if False :
    print("Evaluacion verdadera")

if not False :
    print("Evaluacion de negacion")

if 0 :
    print("Evaluacion 0")

if 1 :
    print("Evaluacion 1")

if -1 :
    print("Evaluacion -1")

if 1.5 :
    print("Evaluacion 1.5")

if [] :
    print("Evaluacion lista vacia")

if "" :
    print("Evaluacion string vacio")

if None :
    print("Valor nulo")

if not None :
    print("Valor nulo")

if x==10.0 :
    print("Comparacion")

if x>10.0 :
    print("Mayor que")

if x<10.0 :
    print("Menor que")

if x>=10.0 :
    print("Mayor o igual que")

if x<=10.0 :
    print("Menor o igual que")

if x!=10.5 :
    print("Diferente que")

#######################################################################################################

if x<5 :
    print("Verdadero")
else :
    print("Falso")

if x<0 :
    print("Menor que cero")

elif x>=0 and x<=5 :
    print("Entre cero y cinco")

else :
    print("Mayor que 5")

#########################################################################################################

match x:
    case 1 :
        print("Vale 1")
    case 5 :
        print("Vale 5")
    case 9 :
        print("Vale 10")
    case _ :
        print("Vale ", x)



