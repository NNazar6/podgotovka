from dataclasses import dataclass


@dataclass
class Pet:
    _name: str
    _animal_type: str
    _age: str

    def get__name(self):
     return f'Name`s {self._name}'
    def get_animal_type(self):
        return f'Breed: {self._animal_type}'
    def get_age(self):
        return f'Vozrast: {_age}'

    def set_name(self, _name):
        self._name = _name

    def set_animal_type(self, _animal_type):
        self._animal_type = _animal_type

    def set_age(self, _age):
        self._age = _age


a = Pet(_name=1, _animal_type=2, _age=3)
print(a)