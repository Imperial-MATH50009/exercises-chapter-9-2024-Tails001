import numbers


class Expression:

    def __init__(self, value=None, operands):
        self.value = value
        self.operands = operands

    def __add__(self, other):
        return Expression(self.operands + other.operands)
    

class Operator(Expression):

    def __repr__(self):
        return type(self).__name__ + repr(self.operands)
    

class Terminal(Expression):

    def __init__(self, value, operands=()):
        return super().__init__(value, operands)

    def __repr__(self):
        return repr(self.value)
    
    def __str__(self):
        return str(self.value)
    
class Number(Terminal):

    def __init__(self, value, operands=()):
        if isinstance(value, numbers.Number):
            return super().__init__(self, value, operands)
        else:
            raise TypeError(
                "Expected number, got something else."
            )

class Symbol(Terminal):

    def __init__(self, value, operands=()):
        if isinstance(value, str):
            return super().__init__(self, value, operands)
        else:
            raise TypeError(
                "Expected string, got something else."
            )