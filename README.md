# Simple Little Dependency Injection Container

[![Build Status](https://secure.travis-ci.org/aventurella/pydi.png?branch=master)](http://travis-ci.org/aventurella/pydi)

## Usage:

```python
    from pydi import Container

    class DogService(object):
        def __init__(self, dep):
            self.dep = dep

        def action(self):
            self.dep.action()

    class FooService(object):

        def __init__(self, dep1, dep2):
            self.dep1 = dep1
            self.dep2 = dep2

        def action1(self):
            self.dep1.action()

        def action2(self):
            self.dep2.action()

    class Bar(object):

        def action(self):
            print('bar')

    class Baz(object):

        def __init__(self, option):
            self.option = option

        def action(self):
            print('baz!!!', self.option)

    class Lucy(object):

        def action(self):
            print("I'm a dog!")


    container = Container()

    # shared must be called last. It will reuse an instance
    container.register(FooService).depends(Bar).depends(Baz, option="Hello World!").shared()

    # without shared, a new instance will be created each time
    container.register(DogService).depends(Lucy)

    # could also container['FoOSeRViCE']()
    obj = container.FooService()
    obj.action1()
    obj.action2()

    print('+-------------+')

    # could also container['fooservice']()
    obj2 = container.FooService()
    obj2.action1()


    print('+-------------+')

    obj3 = container.FooService()
    obj3.action1()
```


