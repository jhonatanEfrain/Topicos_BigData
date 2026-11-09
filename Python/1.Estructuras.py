print("estructuras condicionales")

#Condicional simple
NotaTBI=18

if NotaTBI>=10.51:
    print("aprobado")

#condicion doble 
edad=17
if edad>= 18:
    print("Tomar bebidas en exceso no es bueno")
else: 
    print("No apto para menores")

#condicional anidado
nota=11
if nota>17 & nota <=20:
    print("alumno brillante")
elif nota >=15 & nota<17:
    print("alumno exelente")
elif nota >14 & nota<15:
    print("alumno bueno")
elif nota>10.5 & nota<13:
    print("alumno regular")
else:
    print ("alumno con bajo rendimiento")

#condicional multiple

"""
python 3.9.0 a versiones anteriores no existe condicional multiple todo se trabajaba con con IF-ELIF- ELIF-ELSE

python 3.10 o superior 
se trabaja con MATCH
"""
num=4
match num:
    case 1 : print ("vocal A")
    case 2 : print ("vocal A")
    case 3 : print ("vocal A")
    case 4 : print ("vocal A")
    case 5 : print ("vocal A")
    case _ : print ("numero no corresponde a voval")