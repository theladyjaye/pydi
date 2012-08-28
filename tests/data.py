class Foo(object):
    def __init__(self):
        self.name = "Lucy"

    def action(self):
        return self.name


class Bar(object):

    def __init__(self, value):
        self.value = value

    def action(self):
        return self.value


class Baz(object):

    def __init__(self, value1, value2, value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3


class Fancy(object):

    def __init__(self, bar, value1, value2, value3):
        self.bar = bar
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
