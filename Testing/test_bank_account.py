import unittest
from Bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(100)
    
    def tearDown(self):
        self.account = None

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-40)

if __name__ == '__main__':
    unittest.main()