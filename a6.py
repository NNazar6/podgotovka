from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    num_id: int
    office: str
    work: str

    def __str__(self):
        return f'Ego zovyt: {self.name}, nomer: {self.num_id},po addresy: {self.office}, rabotaet on v: {self.work}.'

a1 = Employee('cuzan', 98765, 'P. 346', 'police')
a2 = Employee('sdf', 3456120, 'p. 231', 'agf')
a3 = Employee('sfwef', 3241245, 'ekfq[p', 'medic')

print(a1, a2, a3, sep='\n')