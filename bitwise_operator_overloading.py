# Python program to demonstrate
# operator overloading

class BitwiseNumber:
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, BitwiseNumber):
            return self.value & obj.value
        raise TypeError("Operand must be BitwiseNumber")

    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, BitwiseNumber):
            return self.value | obj.value
        raise TypeError("Operand must be BitwiseNumber")

    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, BitwiseNumber):
            return self.value ^ obj.value
        raise TypeError("Operand must be BitwiseNumber")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, BitwiseNumber):
            return self.value << obj.value
        raise TypeError("Operand must be BitwiseNumber")

    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, BitwiseNumber):
            return self.value >> obj.value
        raise TypeError("Operand must be BitwiseNumber")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value
        
# Driver's code
if __name__ == "__main__":
    a = BitwiseNumber(10)
    b = BitwiseNumber(12)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)

# OUTPUT
# And operator overloaded
# 8
# Or operator overloaded
# 14
# Xor operator overloaded
# 6
# lshift operator overloaded
# 40960
# rshift operator overloaded
# 0
# Invert operator overloaded

# -11
