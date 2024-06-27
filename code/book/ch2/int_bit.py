class Int_Bit:
    def __init__(self, num):
        self.num = num

    def __and__(self, other):
        return Int_Bit(self.num & other.num)

    def __or__(self, other):
        return Int_Bit(self.num | other.num)

    def __xor__(self, other):
        return Int_Bit(self.num ^ other.num)

    def __str__(self):
        return bin(self.num)
