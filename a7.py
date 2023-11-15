from dataclasses import dataclass
@dataclass
class Retailitem:
    desc: str
    col_v: int
    price: float

    def __str__(self):
        return f'{self.desc}, {self.col_v}, {self.price}'

p1 = Retailitem('pidj', 52, 95.5)
p2 = Retailitem('drevo', 11000, 3.3)
p3 = Retailitem('redis', 432, 4.0)
print(p1, p2, p3, sep='\n')

