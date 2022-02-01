# 特殊メソッド

class Word(object):
    
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word('text')
w2 = Word('text')

print(w) # print(w.text)
print(len(w)) # print(len(w.text))
print(w + w2) # print(w.text + w2.text)
print(w == w2) # __eq__の特殊メソッドがなければwとw2は別のオブジェクトなのでFalseになる

"""
__eq__( self, other ) self == other
__ne__( self, other ) self != other
__lt__( self, other ) self < other
__gt__( self, other ) self > other
__le__( self, other ) self <= other
__ge__( self, other ) self >= other

__add__( self, other ) self + other
__sub__( self, other ) self - other
__mul__( self, other ) self * other
__floordiv__( self, other ) self // other
__truediv__( self, other ) self / other
__mod__( self, other ) self % other
__pow__( self, other ) self ** other

__str__( self ) str( self )
__len__( self ) len( self )

"""