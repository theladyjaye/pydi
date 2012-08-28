from __future__ import absolute_import

import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest
from pydi import Container
from tests import data
from tests import services


class PydiSuite(unittest.TestCase):

    def test_simple(self):
        c = Container()
        c.register(services.FooService).depends(data.Foo)

        obj = c.FooService()

        self.assertTrue(isinstance(obj, services.FooService))
        self.assertTrue(isinstance(obj.dep1, data.Foo))
        self.assertEqual(obj.action(), 'Lucy')

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
