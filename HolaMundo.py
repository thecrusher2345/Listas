import math
class Figura:
    def __init__(self, base, altura):
        self.__base=base
        self.__altura=altura
    def setbase(self,base):
        self.__base=base
    def getbase(self):
        return self.__base
    def setaltura(self,altura):
        self.__altura=altura
    def getaltura(self):
        return self.__altura
    #creacion de las funciones
    def hipotenusa(self):
        return math.sqrt((self.getbase()**2)+(self.getaltura()**2))
    def area(self):
        return 0
    def perimetro(self):
        return 0
    #creacion de las clases a manejar
class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base,altura)
        
    def perimetro(self):
        return self.getbase()+self.getaltura()+self.hipotenusa()
    
    def area(self):
        return self.getbase()*self.getaltura()/2
    
class Cuadrado(Figura):
    def __init__(self, base, altura):
        super().__init__(base,altura)
        
        
    def perimetro(self):
        return 2*self.getbase()+2*self.getaltura() 
    
    def area(self):
        return self.getbase()*self.getaltura()
    
class Rombo(Figura):
    def __init__(self, base, altura, mayor, menor):
        super().__init__(base, altura)
        self.__mayor=mayor
        self.__menor=menor
        
    def setmayor(self,mayor):
        self.__mayor = mayor
    def getmayor(self):
        return self.__mayor
        
    def setmenor(self,menor):
        self.__menor = menor
    def getmenor(self):
        return self.__menor
        
    def perimetro(self):
        return 2*self.getbase()+2*self.getaltura() 
    
    def area(self):
        return (self.getmayor()*self.getmenor())/2
