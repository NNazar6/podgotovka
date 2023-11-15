class Book:

    def __init__(self, header, title, name):
        self.header = header
        self.title = title
        self.name = name

    def get_header(self):
        return self.header

    def get_title(self):
        return self.title

    def get_name(self):
        return self.name

    def set_header(self, header):
        return self.header

    def set_title(self, title):
        return self.title

    def set_name(self, name):
        return self.name

    def __str__(self):
        return 'Hello!'

a = Book(1, 2, 3)
print(a.header)
print(a.title)
print(a.name)