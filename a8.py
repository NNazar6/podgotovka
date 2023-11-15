from dataclasses import dataclass, field


@dataclass
class Patient:
    address: str
    town: str
    obl: str
    mail_index: str
    phone: list = field(default_factory=list)
    fio: list = field(default_factory=list)
    procedures: list = field(default_factory=list)

    def get_fio(self):
        return self.fio

    def get_address(self):
        return self.address

    def get_town(self):
        return self.town

    def get_obl(self):
        return self.obl

    def get_mail_index(self):
        return self.mail_index

    def get_phone(self):
        return self.phone

    def get_procedures(self):
        for i in self.procedures:
            print(i)

    def set_fio(self, fio):
        self.fio = fio

    def set_address(self, address):
        self.address = address

    def set_town(self, town):
        self.town = town

    def set_obl(self, obl):
        self.obl = obl

    def set_mail_index(self, mail_index):
        self.mail_index = mail_index

    def set_phone(self, phone):
        self.phone = phone

    def repr(self):
        return f'{self.address},\n{self.town},\n{self.obl},\n{self.mail_index},\n{self.phone},\n{self.fio}'


@dataclass
class Procedure:
    name_proceduri: str
    data_proc: str
    doctor: str
    price: float

    def get_name_proceduri(self):
        return self.name_proceduri

    def get_data_proc(self):
        return self.data_proc

    def get_doctor(self):
        return self.doctor

    def get_price(self):
        return self.price

    def set_name_proceduri(self, name_proceduri):
        self.name_proceduri = name_proceduri

    def set_data_proc(self, data_proc):
        self.data_proc = data_proc

    def set_doctor(self, doctor):
        self.doctor = doctor

    def set_price(self, price):
        self.price = price

    def str(self):
        return f'{self.name_proceduri},\n{self.data_proc}\n{self.doctor},\n{self.price}'

    def repr(self):
        return f'{self.name_proceduri},\n{self.data_proc}\n{self.doctor},\n{self.price}'


patient = Patient('Shihkino', 'Elabuga', 'Tatarstanscaya obl', 'G331h7R', [89445332138, 98765464123],
                  ['Nazarov', 'Nazar', 'Michailovich'])
print(patient)

p1 = Procedure('Врачебный осмотр', 'today', 'Irvin', 250)
p2 = Procedure('Rentgen', 'today', 'Jemison', 500)
p3 = Procedure('Analiz crovi','today', 'Smit', 200)
patient.procedures = [p1, p2, p3]
patient.get_procedures()
