from __future__ import absolute_import

import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest
from pydi.exceptions import InitializationFailed
from pydi import Container
from pydi.utils import Resolve
from tests import data
from tests import services


class PydiSuite(unittest.TestCase):

    def test_multiple_error(self):
        c = Container()
        c.register(services.BarService)\
                  .depends(data.Foo)\
                  .depends(data.Bar, value='Ollie')\
                  .depends(data.Zap)

        self.assertRaises(InitializationFailed, c.BarService)

    def test_resolve(self):
        c = Container()
        c.register(services.BarService).depends(data.Foo).depends(data.Bar, value='Ollie')
        c.register(services.BazService).depends(Resolve(services.BarService))

        obj1 = c.BazService()

        self.assertTrue(isinstance(obj1, services.BazService))
        self.assertTrue(isinstance(obj1.service, services.BarService))
        self.assertEqual(obj1.action1(), 'Lucy')
        self.assertEqual(obj1.action2(), 'Ollie')

    def test_resolve_shared(self):
        c = Container()
        c.register(services.BarService).depends(data.Foo).depends(data.Bar, value='Ollie')
        c.register(services.BazService).depends(Resolve(services.BarService)).shared()

        obj1 = c.BazService()
        obj2 = c.BazService()

        self.assertEqual(obj1, obj2)

    def test_simple(self):
        c = Container()
        c.register(services.FooService).depends(data.Foo)

        obj = c.FooService()

        self.assertTrue(isinstance(obj, services.FooService))
        self.assertTrue(isinstance(obj.dep1, data.Foo))
        self.assertEqual(obj.action(), 'Lucy')

    def test_alternate_name(self):
        c = Container()
        c.register(services.FooService, 'banana').depends(data.Foo)

        obj = c.Banana()

        self.assertTrue(isinstance(obj, services.FooService))
        self.assertTrue(isinstance(obj.dep1, data.Foo))
        self.assertEqual(obj.action(), 'Lucy')

    def test_alternate_name_fail(self):
        c = Container()
        c.register(services.FooService, 'banana').depends(data.Foo)

        self.assertRaises(AttributeError,
                          getattr,
                          c, 'FooService')

        self.assertRaises(KeyError,
                          c.__getitem__,
                          'FooService')

    def test_multiple(self):
        c = Container()
        c.register(services.FooService).depends(data.Foo)
        c.register(services.BarService).depends(data.Foo).depends(data.Bar, value='Ollie')

        obj1 = c.FooService()
        obj2 = c.BarService()

        self.assertTrue(isinstance(obj1, services.FooService))
        self.assertTrue(isinstance(obj1.dep1, data.Foo))
        self.assertEqual(obj1.action(), 'Lucy')

        self.assertTrue(isinstance(obj2, services.BarService))
        self.assertTrue(isinstance(obj2.dep1, data.Foo))
        self.assertTrue(isinstance(obj2.dep2, data.Bar))
        self.assertEqual(obj2.action1(), 'Lucy')
        self.assertEqual(obj2.action2(), 'Ollie')

    def test_shared(self):
        c = Container()
        c.register(services.BarService).depends(data.Foo).depends(data.Bar, value='Ollie').shared()

        obj1 = c.BarService()
        obj2 = c.BarService()

        self.assertEqual(obj1, obj2)

    # def test_shared_difference(self):
    #     c = Container()
    #     c.register(services.BarService).depends(data.Foo).depends(data.Bar, value='Ollie').shared()

    #     obj1 = c.BarService()
    #     obj2 = c.BarService()

    #     import threading
    #     import time

    #     def thread_scope1():
    #         obj3 = c.BarService()
    #         self.assertTrue(obj1 != obj3)
    #         time.sleep(1)

    #     def thread_scope2():
    #         obj4 = c.BarService()
    #         self.assertTrue(obj1 != obj4)
    #         time.sleep(1)

    #     thread1 = threading.Thread(target=thread_scope1)
    #     thread2 = threading.Thread(target=thread_scope2)

    #     thread1.start()
    #     thread2.start()
    #     thread1.join()
    #     thread2.join()

    def test_other_init(self):
        c = Container()
        c.register(data.Bar).depends('RoboFish')

        obj = c.Bar()

        self.assertEqual(obj.value, 'RoboFish')

    def test_other_init_multi(self):
        c = Container()
        c.register(data.Baz).depends('RoboFish').depends('Lucy').depends('Ollie')

        obj = c.Baz()

        self.assertEqual(obj.value1, 'RoboFish')
        self.assertEqual(obj.value2, 'Lucy')
        self.assertEqual(obj.value3, 'Ollie')

    def test_other_init_kwargs(self):
        c = Container()
        c.register(data.Baz)

        obj = c.Baz(value1='RoboFish', value2='Lucy', value3='Ollie')

        self.assertEqual(obj.value1, 'RoboFish')
        self.assertEqual(obj.value2, 'Lucy')
        self.assertEqual(obj.value3, 'Ollie')

    def test_fancy_init_kwargs(self):
        c = Container()
        c.register(data.Fancy).depends(data.Bar, value='Tucker')

        obj = c.Fancy(value1='RoboFish', value2='Lucy', value3='Ollie')

        self.assertEqual(obj.value1, 'RoboFish')
        self.assertEqual(obj.value2, 'Lucy')
        self.assertEqual(obj.value3, 'Ollie')

        self.assertTrue(isinstance(obj.bar, data.Bar))
        self.assertEqual(obj.bar.value, 'Tucker')
