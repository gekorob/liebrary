class Author:
    def __init__(self, id_in, name, birth_date):
        self.id = id_in
        self.name = name
        self.birth_date = birth_date

    def __eq__(self, other):
        return self.id == self.id and \
               self.name == other.name and \
               self.birth_date == other.birth_date
