import unittest

class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }

class TestCoffeeMenu(unittest.TestCase):
  def setUp(self) -> None:
    self.menu = CoffeeMenu