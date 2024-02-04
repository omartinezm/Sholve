class Equal:
    def __init__(self, sideLeft,sideRight) -> None:
        self.args = [sideLeft,sideRight]
        self.name='Equality'

    def __str__(self) -> str:
        return str(self.args[0])+'='+str(self.args[1])

class Add:
    def __init__(self, term1,*kwargs) -> None:
        self.args = [term1,*kwargs]
        self.name='Sum'

    def __str__(self) -> str:
        return "+".join([str(k) for k in self.args])

class Negative:
    def __init__(self,value) -> None:
        self.args = [value]
    
    def __str__(self) -> str:
        return '-'+str(self.args[0])

class Difference:
    def __init__(self, term1,term2) -> None:
        self.args = [term1,Negative(term2)]
        self.name='Difference'

    def __str__(self) -> str:
        return str(self.args[0])+'-'+str(self.args[1])

class Product:
    def __init__(self, factor1,factor2) -> None:
        self.args = [factor1,factor2]
        self.name='Product'

    def __str__(self) -> str:
        return str(self.args[0])+'*'+str(self.args[1])

class Quotient:
    def __init__(self, numerator,denominator) -> None:
        self.args = [numerator,denominator]
        self.name='Quotient'

    def __str__(self) -> str:
        return str(self.args[0])+'/'+str(self.args[1])
    
class Number:
    def __init__(self,value) -> None:
        self.args = [value]
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
    
class Variable:
    def __init__(self,name) -> None:
        self.args = [name]
        self.name=name

    def __str__(self) -> str:
        return str(self.name)


print(Add(1,2,3))