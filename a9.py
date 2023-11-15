from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    num_id: int
    office: str
    work: str

    def set_name(self, name):
        self.name = name

    def set_office(self, office):
        self.office = office

    def set_work(self, work):
        self.work = work

    def __str__(self):
        return f'{self.name}, {self.num_id}, {self.office}, {self.work}'


def e_list(key, Value, dict):
    dict[key] == Value
    return dict


def e_search(dict, name):
    res = {}
    for key in dict:
        if name == dict[key].name:
            print(dict[key])
        else:
            print('Error, you oshibsia, durachok!')


def e_change(name, office, work, Emp):
    Emp.set_name(name)
    Emp.set_office(office)
    Emp.set_work(work)


def e_delete(key, dict):
    del dict[key]


counter = 0
reestr = {}
a1 = Employee('GG', 7777, 'opera', 'fff')
e_list(counter, a1, reestr)
counter += 1
a2 = Employee('dd', 1111, 'google', 'yy')
e_list(counter, a2, 'microsoft')
counter += 2
a3 = Employee('ll', 1234, 'dn', 'cfgd')
e_list(counter, a3, reestr)

e_search(reestr, 'dd')
e_change('asfdqw', 'dqewqw', 'efwew', reestr[0])
print(reestr[0])
e_delete(0, reestr)
print(reestr[1])
