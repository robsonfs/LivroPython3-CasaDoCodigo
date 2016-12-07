class Column:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise Exception("Nome não pode mudar!")

    @name.deleter
    def name(self):
        pass
