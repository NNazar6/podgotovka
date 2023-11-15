from dataclasses import dataclass, field


@dataclass
class RetailItem:
    desc: str
    col_v: int
    price: float

    def __str__(self):
        return f'{self.desc}, {self.col_v}, {self.price}'

@dataclass
class CashRegister:
    item_list: list = field(default_factory=list)

    def purchase_item(self, purches):
        self.item_list.append(purches)

    def get_total(self):
        total_summ = 0
        for i in self.item_list:
            total_summ += i.price

        return total_summ

    def show_item(self):
        for i in self.item_list:
            print(i)

    def clear_register(self):
        self.item_list = []


cash_register = CashRegister()
item1 = RetailItem('Товар1', 'Пиджак', 12)
item2 = RetailItem('Товар2', 'Дизайнерские джинсы', 40)
item3 = RetailItem('Товар3', 'Рубажка', 20)
# print(item1)
cash_register.purchase_item(item2)
cash_register.purchase_item(item1)
cash_register.show_items()
print(f'total: {cash_register.get_total()}')
cash_register.clear_register()
cash_register.show_items()