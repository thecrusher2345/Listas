
from HolaMundo import Figura, Triangulo, Cuadrado, Rombo
print("1.- Triangulo")
print("2.- Cuadrado ")
print("3.- Rombo")
op=int(input("ingrese un numero "))
match op:
    case 1:
        _base=int(input("ingrese un valor para la base: "))
        _altura=int(input("ingrese un valor para la altura: "))
        t=Triangulo(_base,_altura)
        print("el perimetro es ", t.perimetro())
        print("el area es: ", t.area())
    case 2:
        _base=int(input("ingrese un valor para la base: "))
        _altura=int(input("ingrese un valor para la altura: "))
        c=Cuadrado(_base,_altura)
        print("el perimetro es ", c.perimetro())
        print("el area es: ", c.area())
        
    case 3:
        _base=int(input("ingrese un valor para la base: "))
        _altura=int(input("ingrese un valor para la altura: "))
        _mayor=int(input("ingrese un valor para la Diagonal mayor: "))
        _menor=int(input("ingrese un valor para la Diagonal menor: "))
        r=Rombo(_base,_altura,_mayor,_menor)
        print("el perimetro es ", r.perimetro())
        print("El area es: ", r.area())
            






