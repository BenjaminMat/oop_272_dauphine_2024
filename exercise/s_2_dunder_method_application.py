"""
### Exercise Instructions
You are given a class `FinancialAsset` that represents a financial asset with a ticker, price, and currency.
The class currently has a method `get_description()` that prints out a description of the asset.

#### Your Tasks:
1. **Implement the `__str__` Method**: The `__str__` method should return a string representation of the
    `FinancialAsset` instance. Before implementing the `__str__` method, check if an existing method already provides
    the desired string representation behavior. If it does, rename the `get_description()` method to `__str__`.
    Make sure that the method returns a string instead of printing it directly.

2. **Implement the `__eq__` Method**: Implement the `__eq__` method to compare two `FinancialAsset` objects.
The method should return `True` if both objects have the same `ticker` and `currency`, and `False` otherwise.
You should also handle the case where the object being compared is not of the `FinancialAsset` type.

### What to Check:
- Ensure the `__str__` method correctly represents the `FinancialAsset` object.
- Confirm that the `__eq__` method accurately compares two `FinancialAsset` objects.
- Verify that all unit tests pass, confirming the correctness of your implementations.
"""
import unittest

class FinancialAsset:
    def __init__(self, ticker, price, currency):
        self.ticker: str = ticker
        self.price: float = price
        self.currency: str = currency

    def get_description(self):
        return f'The ticker for this asset is {self.ticker} and its price is {self.price} {self.currency}'



"""
Exercise Instructions
You are given a class InstrumentList that represents a collection of FinancialAsset objects. Your task is to 
implement two special methods (__add__ and __sub__) for adding and removing financial assets from the list.


Implement the __add__ Method:
    The __add__ method should enable adding a FinancialAsset object to the InstrumentList.
    If the object being added is not of the FinancialAsset type, raise a TypeError with an appropriate message.
    The method should return a new InstrumentList object with the added FinancialAsset.
    
Implement the __sub__ Method:
    The __sub__ method should allow removing a FinancialAsset object from the InstrumentList, if it exists in the list.
    If the FinancialAsset object is not found in the list, the list should remain unchanged.
    If the object being subtracted is not of the FinancialAsset type, raise a TypeError with an appropriate message.
    The method should return a new InstrumentList object with the FinancialAsset removed (if it was found).
"""

class InstrumentList:
    def __init__(self, list_of_instrument):
        self.instruments: [FinancialAsset] = list_of_instrument

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass



"""
UNIT TEST
"""

class TestFinancialAsset(unittest.TestCase):
    def test_str_method(self):
        asset = FinancialAsset("AAPL", 150.0, "USD")
        self.assertEqual(str(asset), 'The ticker for this asset is AAPL and its price is 150.0 USD')

    def test_eq_method_same_ticker_and_currency(self):
        asset1 = FinancialAsset("AAPL", 150.0, "USD")
        asset2 = FinancialAsset("AAPL", 200.0, "USD")
        self.assertTrue(asset1 == asset2)

    def test_eq_method_different_ticker(self):
        asset1 = FinancialAsset("AAPL", 150.0, "USD")
        asset2 = FinancialAsset("MSFT", 150.0, "USD")
        self.assertFalse(asset1 == asset2)

    def test_eq_method_different_currency(self):
        asset1 = FinancialAsset("AAPL", 150.0, "USD")
        asset2 = FinancialAsset("AAPL", 150.0, "EUR")
        self.assertFalse(asset1 == asset2)

    def test_eq_method_different_object(self):
        asset = FinancialAsset("AAPL", 150.0, "USD")
        self.assertFalse(asset == "Not a FinancialAsset object")


class TestInstrumentList(unittest.TestCase):
    def setUp(self):
        self.asset1 = FinancialAsset("AAPL", 150.0, "USD")
        self.asset2 = FinancialAsset("MSFT", 250.0, "USD")
        self.asset3 = FinancialAsset("GOOGL", 2800.0, "USD")
        self.instrument_list = InstrumentList([self.asset1, self.asset2])

    def test_add_method(self):
        new_list = self.instrument_list + self.asset3
        self.assertIn(self.asset3, new_list.instruments)
        self.assertEqual(len(new_list.instruments), 3)

    def test_add_method_invalid_type(self):
        with self.assertRaises(TypeError):
            _ = self.instrument_list + "Not a FinancialAsset object"

    def test_sub_method(self):
        new_list = self.instrument_list - self.asset1
        self.assertNotIn(self.asset1, new_list.instruments)
        self.assertEqual(len(new_list.instruments), 1)

    def test_sub_method_non_existing_asset(self):
        new_list = self.instrument_list - self.asset3  # asset3 is not in the list
        self.assertEqual(new_list.instruments, self.instrument_list.instruments)
        self.assertEqual(len(new_list.instruments), 2)

    def test_sub_method_invalid_type(self):
        with self.assertRaises(TypeError):
            _ = self.instrument_list - "Not a FinancialAsset object"

if __name__ == "__main__":
    unittest.main()
