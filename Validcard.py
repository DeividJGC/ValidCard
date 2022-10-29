print("  _____           _           _       _                 _    _____    _____ 	 ")
print(" |  __ \         (_)         (_)     | |               | |  / ____|  / ____|  ")
print(" | |  | |   ___   _  __   __  _    __| |               | | | |  __  | |       ")
print(" | |  | |  / _ \ | | \ \ / / | |  / _` |           _   | | | | |_ | | |       ")
print(" | |__| | |  __/ | |  \ V /  | | | (_| |          | |__| | | |__| | | |____   ")
print(" |_____/   \___| |_|   \_/   |_|  \__,_|           \____/   \_____|  \_____|  ")
print("                                        ______                                ")
print("                                       |______|                               ")
print("Creado por Deivid_JGC :)")
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

    if int(N[0:2])>49 and int(N[0:2])<56:T="**Mastercard"
    if N[0:2]=="34" or N[0:2]=="37":T="**America Express"
    if N[0]=="4":T="**VISA"
    if N[0:2] in "60626465":T="**Discover"

    return 4,T

msg=(0,"")

while msg[0]!=4:
    msg=validcard(input("Enter Credit card number 13-19:"))
    if msg[0]==1:print("must be only numbers 0 - 9")
    if msg[0]==2:print("must be 13 or more(less or equal 19)")
    if msg[0]==3:print("Número de tarjeta INVALIDO!!")

print("Tarjeta VALIDA!!")
print("Tipo:"+msg[1])
