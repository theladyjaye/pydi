class FooService(object):

    def __init__(self, dep1):
        self.dep1 = dep1

    def action(self):
        return self.dep1.action()


class BarService(object):

    def __init__(self, dep1, dep2):
        self.dep1 = dep1
        self.dep2 = dep2

    def action1(self):
        return self.dep1.action()

    def action2(self):
        return self.dep2.action()


class BazService(object):
    def __init__(self, service):
        self.service = service

    def action1(self):
        return self.service.action1()

    def action2(self):
        return self.service.action2()

