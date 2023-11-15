from dataclasses import dataclass


@dataclass
class Information:
    name: str
    address: str
    age: int
    tel_num: int

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_tel_num(self):
        return self.tel_num

    def set_name(self, name):
        return self.name

    def set_address(self, address):
        return self.address

    def set_age(self):
        return self.age

    def set_tel_num(self):
        return self.tel_num


a1 = Information('AA', 'dn', 35, 9878987676)
a2 = Information('Aa', 'dnt', 5, 4382389996)
a3 = Information('aa', 'dnert', 90, 987123432)

print(a1, a2, a3, sep='\n')