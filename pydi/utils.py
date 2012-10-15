class Resolve(object):

    def __init__(self, cls, container=None):
        self.cls = cls.__name__
        self.container = container

    def __call__(self):
        return getattr(self.container, self.cls)()
