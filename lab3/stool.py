class Stool:
    def __init__(self, height=50, quality='high'):
        self.height = height
        self.quality = quality

    def wood_amount(self):
        if self.quality == 'low':
            return 4 * self.height + 12
        elif self.quality == 'average' or self.quality == 'high':
            return 5 * self.height + 14

    def price(self, woodAmount):
        if self.quality == 'low':
            return woodAmount * 2
        elif self.quality == 'average':
            return woodAmount * 3
        elif self.quality == 'high':
            return woodAmount * 4

    def __str__(self):
        return f'Stool height is {self.height} and quality is {self.quality}'

    def __add__(self, other):
        if not isinstance(other, Stool):
            raise Exception("Right operand must be Stool type")
        return Stool(self.height + other.height)

    def _iadd__(self, other):
        if not isinstance(other, Stool):
            raise Exception("Right operand must be Stool type")
        self.height += other.height
        return self

    def __sub__(self, other):
        if not isinstance(other, Stool):
            raise Exception("Right operand must be Stool type")
        return Stool(self.height - other.height)

    def __isub__(self, other):
        if not isinstance(other, Stool):
            raise Exception("Right operand must be Stool type")
        self.height -= other.height
        return self

    def __mul__(self, other):
        if not isinstance(other, Stool):
            raise Exception("Right operand must be Stool type")
        return Stool(self.height * other.height)

    def __imul__(self, other):
        if not isinstance(other, Stool):
            raise Exception("Right operand must be Stool type")
        self.height *= other.height
        return self

    def __truediv__(self, other):
        if not isinstance(other, Stool):
            raise Exception("Right operand must be Stool type")
        return Stool(self.height / other.height)

    def __mod__(self, other):
        if not isinstance(other, Stool):
            raise Exception("Right operand must be Stool type")
        return Stool(self.height % other.height)

    def __eq__(self, other):
        return self.height == other.height

    def __nq__(self, other):
        return self.height != other.height

    def __lt__(self, other):
        return self.height < other.height

    def __le__(self, other):
        return self.height <= other.height

    def __gt__(self, other):
        return self.height > other.height

    def __ge__(self, other):
        return self.height >= other.height