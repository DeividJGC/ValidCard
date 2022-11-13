#Importar
import random
#Créditos
print("\033[1;31m " + "  _____           _           _       _                 _    _____    _____ 	 ")
print("\033[1;31m " + " |  __ \         (_)         (_)     | |               | |  / ____|  / ____|  ")
print("\033[1;33m " + " | |  | |   ___   _  __   __  _    __| |               | | | |  __  | |       ")
print("\033[1;33m " + " | |  | |  / _ \ | | \ \ / / | |  / _` |           _   | | | | |_ | | |       ")
print("\033[1;31m " + " | |__| | |  __/ | |  \ V /  | | | (_| |          | |__| | | |__| | | |____   ")
print("\033[1;31m " + " |_____/   \___| |_|   \_/   |_|  \__,_|           \____/   \_____|  \_____|  ")
print("\033[1;31m " + "                                        ______                                ")
print("\033[1;31m " + "                                       |______|                               ")
print("\033[1;32m " + "Creado por Deivid_JGC :)")
#Código de Validación de Números de tarjeta
def validcard(N):
    T=""; par=0;impar=0;X=""
    if not N.isdigit():return 1,""
    if len(N)<14 or len(N)>19:return 2,""

    for c in range(0,len(N),2):
        X=str(int(N[c])*2)
        if len(X)==2:
            par+=(int(X[0])+int(X[1]))
        else:par+=int(X)
    for c in range(1,len(N),2):
        impar+=int(N[c])

    if (par+impar)%10!=0:return 3,""
#Código de Validación de Tipo de Tarjeta
    if int(N[0:2])>49 and int(N[0:2])<56:T="**Mastercard"
    if N[0:2]=="34" or N[0:2]=="37":T="**America Express"
    if N[0]=="4":T="**VISA"
    if N[0:2] in "60626465":T="**Discover"

    return 4,T

msg=(0,"")
#Mensajes de la Terminal
while msg[0]!=4:
    msg=validcard(input("\033[33m " + "Inserta un número de tarjeta de mínimo 13 y máximo o exáctamente 19 dígitos: "))
    if msg[0]==1:print("\033[1;31m " + "Solo puede usar números del 0 al 9 ")
    if msg[0]==2:print("\033[1;31m " + "Solo mínimo 13 y máximo o exáctamente 19 dígitos")
    if msg[0]==3:print("\033[1;31m " + "Número de tarjeta INVALIDO!!")

print("\033[1;32m " + "Tarjeta VALIDA!!")
print("Tipo:"+msg[1])

#Muchas Gracias por usar mi script. <3