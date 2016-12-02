from decimal import Decimal
from custom_exceptions import validate_kind

class DataTable:
    """Representa uma tabela de dados.

    Essa classe representa uma tabela de dados do portal da transparência. Deve
    Ser capaz de validar linhas inseridas de acordo com as colunas que possui.
    As linhas inseridas ficam registradas dentro dela.

    Attributes:
        name: Nome da tabela
        column: [Lista de colunas]
        data: [Lista de dados]
    """
    def __init__(self, name):
        """Constructor

            Args:
                name: nome da tabela
        """
        self._name = name
        self._columns = []
        self._data = []
        self._references = []
        self._referenced = []

    def add_column(self, name, kind, description=""):
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        """Cria uma referência dessa tabela para uma outra tabela.

        Args:
            name: Nome da relação
            to: instancia da tabela apontada
            on: Instancia de coluna em que existe a relação.
        """
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        """Cria uma referência para outra tabela que aponta para essa.

            Args:
                name: Nome da relação
                by: instancia da tabela que aponta para essa
                on: instancia coluna em que existe relação.
        """
        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)


class Column:
    """Representa uma coluna em um DataTable.

    Essa classe contém as informações de uma coluna e deve validar um dado de
    acordo com o tipo de dado configurado no construtor.

    Attributes:
        name: Nome da Coluna
        kind: tipo do dado (Varchar, bigint, numeric)
        description: Descrição da Coluna
    """
    def __init__(self, name, kind, description=""):
        """Constructor

            Args:
                name: Nome da Coluna
                kind: tipo do dado (varchar, bigint, numeric)
                description: Descrição da Coluna
        """
        self._name = name
        self._kind = kind
        self._description = description
        self._is_pk = False

    def __str__(self):
        _str = "Col: {}: {} {}".format(
            self._name, self._kind, self._description
        )
        return _str

    def _validate(kind, data):
        if kind == "bigint":
            if isinstance(data, int):
                return True
            return False
        elif kind == "varchar":
            if isinstance(data, str):
                return True
            return False
        elif kind == "numeric":
            try:
                val = Decimal(data)
            except:
                return False
            return True
        else:
            # Eu sei, neste caso eu poderia simplemente lançar uma exceção ao invés
            # de chamar um método que faz as verificações que já foram feitas aqui....
            # Mas aqui a didática está prevalecendo sobre a elegancia...
            validate_kind()

    validate = staticmethod(_validate)

class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=None):
        super().__init__(name, kind, description=description)
        self._is_pk = True

class Relationship:
    """Classe que representa um relacionamento entre DataTables.

    Essa classe tem todas as informações que identificam um relacionamento entre
    tabelas. Em qual coluna ele existe, de onde vem e para onde vai.
    """

    def __init__(self, name, _from, to, on):
        """Constructor

        Args:
            name: Nome
            from: tabela de onde sai
            to: Tabela para onde vai
            on: Instancia de coluna onde existe
        """
        self._name = name
        self._from = _from
        self._to = to
        self._on = on
