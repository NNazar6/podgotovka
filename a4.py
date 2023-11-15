from dataclasses import dataclass


@dataclass
class Car:
    _year_model: str
    rttake: str
    _speed: int(0)

    def accerlerate(self):
        self._speed += 5
        print(f'Speed: {self._speed}')

    def broken(self):
        self._speed -= 5
        print(f'Speed: {self._speed}')

    def get_speed(self):
        return self._speed


audi = Car(2020, 'gg', 200)

for i in range(5):
    audi.accerlerate()
    audi.broken()

print(audi.get_speed())