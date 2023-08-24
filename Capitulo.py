l,m,mi,j,v,s,d = "lunes","martes","miercoles","jueves","viernes","sabado","domingo"

di = input("Escriba el dia que estuvo estacionado: ")
horas = int(input("Digite la cantidad de horas que estuvo estacionado: "))
min = int(input("Digite la cantidad de minutos que estuvo estacionado: "))
if min>= 60:
    print("Cantidad de minutos no permitidas")
elif min >=5:
    horas +=1
       
if di.lower() == l or di.lower() == m or di.lower() == mi:
    Tarifa= horas*2.00
    print("su tarifa es $ ", Tarifa)

if di.lower() == j or di.lower() == v :
    Tarifa= horas*2.50
    print("su tarifa es $", Tarifa)

if di.lower() == s or di.lower() == d:
    Tarifa= horas*3.00
    print("su tarifa es $", Tarifa)


