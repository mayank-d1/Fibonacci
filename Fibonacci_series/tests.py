from django.test import TestCase
from .views import fibonacci


class FibonacciTestCase(TestCase):
    def test_fibonacci(self):
        self.assertEquals(fibonacci(6), 8)
        self.assertEquals(fibonacci(0), 0)
        self.assertEquals(fibonacci(1), 1)
        self.assertEquals(fibonacci(10), 55)
