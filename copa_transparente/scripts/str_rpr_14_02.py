class TestWithoutStr:
    def __init__(self, name):
        print("Creating a test witout str...")
        self.name = name


class TestWithStr:
    def __init__(self, name):
        print("Creating a test with str")
        self.name = name

    def __str__(self):
        return "Experiment %s"%(self.name)


class TestWithRepr:
    def __init__(self, name):
        print("Creating a test with repr")
        self.name = name

    def __repr__(self):
        return "Experiment %s"%(self.name)
