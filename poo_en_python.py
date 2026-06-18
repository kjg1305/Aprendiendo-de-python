#----cosntructores en poo-----------

class Estudiante: 

    def __init__ (self,nombre,edad):
        self.nombre=nombre;
        self.edad=edad;

#--------------------------
#La diferencia de java a python es que en el constructor se inisialisan 
#con this.la_variable en java y en python es self.la _variable
# ademas la estructura de inicialiacion es diferente meintras que en java
# se debe colocar el tipo de visivilidad el nombre de constructor y luego sus
#atributos y despues la declaracion this ; por otro lado en python se usa la declaracion 
# de funcion def mas __init__ como inicializar del constructor sin nombre , se le agrgan
# la palabra self y luego las variables a inicializar , por ultimo se hace la declracion self.
# la estructura en ambos es similar sinembargo como siempre en java se es mas estricto con la sintaxis.

#-------------------------

#----Metodos en pooo--------------

class Estudiante:

    def mostrar_info(self):
        print(self.nombre + self.edad);

# en python la estructura para crear un metodo es la declaracion def de funcion
# + nombre del metodo + atributos que se usan en el metodo , cuando es un metodo del 
# tipo void no se coloca en si un atributo sino la instrucion self para indicar que no hay retorno de ningun valor 
# las variables que se usen en el metodo deben ser declaradas con el self.nombre_variable 
# ya que de esta forma el metodo puede acceder al valor de la varible .

#-------------------------

#----Herencia en poo----------------
class Persona :
     def __init__(self,nombre):
         self.nombre=nombre;

class Estudiante(Persona):

    def __intit__( self,nombre,carrera):
        super().__init__(nombre);
        self.carrera=carrera;

# para hacer herencia en python com en java se debe tener una clase padre de la cual una clase hija pueda heredar
# en python se hace la declaracion de la clase padre como una clase normal y para delcar la clase hija 
# se coloca el nombre de la clase y se debe colocar entre parentesis el nombre de la clase padre de la cual hereda,
# para hacer la declaracion del constructor se usa  la misma declaraion de  def y self 
# lo que se debe agregar es la palabra super().__init__(nombre de las varibales que se heredan) y posteriormente 
# si  se puede hacer self.nombre_variable_claseHija  para gregar las variabes propias de la clase hija.

#-------------------------

#----Sobreescritura de metodos en poo------

def mostrar_info(self):
    print("Nuevo comportamiento");

# para hacer la sobreescritura de un metodo en python se debe declarar el mismo metodo a sobreescribir
# con la misma estructura de declaracion pero con un nuevo copratamiento en su interior , puede hacer 
# mas o menos funciones que tenia antes el metodo original pero lo importante es que se mantenga 
# la misma estructura de declaracion del metodo.

#-------------------------

#----Polimorfismo en poo---------------

class Animal :

    def sonido(self):
        pass

class Perro(Animal):

    def sonido(self):
        print("GUAU")

class Gato(Animal):

    def sonido(self):
        print("MIAU")


# para usar el polimofismo en python en lugar de indicar que la clase es adtracta como se hace en java
# solo se declara  la clase padre con un metodo de plantilla sin alfuna funcionalidad y con solo la palabra pass
# luego se declara una clase hija que hereda el metodo declarado en la clase padre y en la clase hija ya se lae 
#agrega una funcionalidad segun la clase lo requeira , esto se puede hacer con varias clases hijas y en cada una
#de ellas se le puede dar una funcionalidad diferente al mismo metodo delcardo en la clase padre , 
#esto es lo que se conoce como polimorfismo ya que el mismo metodo puede tener diferentes 
#comportamientos segun la clase que lo implemente.

# --ENCAPSULAMIENTO EN POO----------------

self.__nombre 

# en python no existe el ecapsulamiento como lo hace en java 
# en python se puede simular el encapsulamiento usando el doble guion bajo antes del nombre de la variable
# esto hace que la variable sea privada y no pueda ser accedida desde fuera de la clase , sin embargo
# esto no es un verdadero encapsulamiento ya que la variable sigue siendo accesible desde dentro de la clase
#  y se puede acceder a ella usando el nombre de la variable con el doble guion bajo , 
# por lo que es importante tener cuidado al usar esta tecnica para simular el encapsulamiento en python.


##EJERCICIOS 

#1-Crear una clase llamada libro con atributos titulo , autor y año de publicacion
#debe tener el metodo de mostrar informacion 

class Libro:
    def ___init__(self,titulo,autor,año_publicacion):
        self.titulo=titulo;
        self.autor=autor;
        self.año_publicacion=año_publicacion;

    def mostrar_Info(self):
        print(self.titulo + self.autor+self.año_publicacion);

#2-Crear persona y profesor con herencia 

class Persona:
    def __init__(self,nombre, edad,estatura):
        self.nombre=nombre;
        self.edad=edad;
        self.estatura=estatura;

class Profesor(Persona):

    def __init__(self,nombre , edad , estatura,curso,salario):
        super().__init__(nombre,edad,estatura)
        self.curso=curso
        self.salario=salario
        