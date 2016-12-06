# coding: utf-8

from decimal import Decimal

class QueryFile():
    def __init__(self, filename):
        self._file = open(filename, "r")

    def __iter__(self):
        return self

    def __next__(self):
        data = self._file.readline()
        if not data:
            self._file.close()
            raise StopIteration

        returned_el = []
        for position in self.positions:
            if len(data) >= position:
                returned_el.append(data[position])
        return returned_el

    def __call__(self, *args):
        self.positions = args
        return self



query = QueryFile("data/data/ExecucaoFinanceira.csv")

for data in query(5, 7):
    print("Execução no valor de {} assinada {}".format(data[0], data[1]))
# total = sum(dec(element, 5) for element in query)
#
# print("Total gasto: {}".format(total))
#
# for n in query:
#     print(n)
