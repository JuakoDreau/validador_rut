def validando_rut(rut):
    lista_rut=list(rut)
    lista2_rut=[]
    cv=""
    contador=2
    acumulado=0
    i = 0
    for i in range(len(lista_rut)):
        if lista_rut[i]=='-':
            cv=lista_rut[i+1]
            break
        if lista_rut[i]=='.':
            lista_rut[i].replace(".","")
        else:
            lista2_rut.append(lista_rut[i])
    lista2_rut=lista2_rut[::-1]
    for i in range(len(lista2_rut)):
        if contador<=7:
            ##print(lista2_rut[i]+"*"+str(contador)+"="+str(int(lista2_rut[i])*contador))
            acumulado=acumulado+(int(lista2_rut[i])*contador)
            ##print(acumulado)
        else:
            contador=2
            ##print(lista2_rut[i]+"*"+str(contador)+"="+str(int(lista2_rut[i])*contador))
            acumulado=acumulado+(int(lista2_rut[i])*contador)
            ##print(acumulado)
        contador+=1

    resto_entero=acumulado//11
    cv_esperado=11-(acumulado-(11*resto_entero))
    print("El codigo verificador esperado es: "+str(cv_esperado))
    print("El codigo verificador recibido por el usuario es: "+cv)
    validador_cv(cv_esperado,cv)

def validador_cv(cv_esperado, cv):
    if cv.isdigit():
        if cv_esperado==int(cv):
            print("El RUT es correcto")
        else:
            if int(cv)==0 and cv_esperado==11:
                print("El RUT es correcto")
            else:
                print("Hubo un error al escribir el RUT")
    else:
        if (cv=="k" or cv=="K")and cv_esperado==10:
            print("El RUT es correcto")
        else:
            print("Hubo un error al escribir el RUT")

def run():
    validando_rut(rut)

rut = input("Ingrese su RUT: ")

if __name__ == '__main__':
    run()