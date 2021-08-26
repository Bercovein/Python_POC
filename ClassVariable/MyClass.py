class MyClass:

    variable = 'Valor variable clase'

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        print(MyClass.variable)

    @classmethod
    def class_method(cls):
        print(cls.variable)


## Se puede crear una variable de clase fuera de la definicion de nuestra clase en si
## se puede generar dinamicamente

print(MyClass.variable)

MyClass.variable2 = 'Variable 2'

print(MyClass.variable2)