"""
Table of contents :
    ## How to organize a project
    ## Unit test
    ## OOP design patterns
"""

"""
## How to organize your code / your project

A typical Python project might have the following directory structure:
    my_project/
    │
    ├── my_package/
    │   ├── __init__.py
    │   ├── module1.py
    │   └── module2.py
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_module1.py
    │   └── test_module2.py
    │
    ├── docs/
    │   └── ...
    │
    ├── scripts/
    │   └── ...
    │
    ├── setup.py
    ├── README.md
    ├── .gitignore
    └── requirements.txt


Explanation:
    - my_package: This directory contains the actual Python package of your project.
    - tests: This directory contains unit tests for your package.
    - docs: This is where your documentation files reside.
    - scripts: This directory might contain standalone scripts related to your project that don’t belong in the 
      package. (Example of how to use the package should be store there).
    - setup.py: This file allows you to install your project using pip.
    - README.md: A markdown file containing basic information about the project.
    - .gitignore: A file telling Git which files or patterns to ignore. 
    - requirements.txt: A file listing all of the Python packages that your project depends on.
"""

"""
## unit test
     ** Definition/Concept** 
        
     ** Why to use it** 
        
    **  When to use it ** 
        
"""

"""
Example of Unit test usage
Class: TestSquareFunction
    Purpose: To containerize tests for the square function.
    Inheritance: Inherits from unittest.TestCase, allowing it to use testing methods and assertions provided by the 
    framework.

    Method: test_positive_number(self)
       
    Method: test_zero(self)

4. Run the Tests
You can either launch the test by clicking to the play/run button next to the class or use unittest.main()
Note: Running this as-is in a regular Python script might raise an error because unittest.main() takes command 
line arguments. If you're running this in a script, you might want to use if __name__ == "__main__": 

"""


def square(n):
    return n ** 2


import unittest

class TestSquareFunction(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(square(2), 4)

    def test_zero(self):
        self.assertEqual(square(0), 0)


""" *** Output of unit test in the Pyhton Console **
============================= test session starts ==============================
collecting ... collected 2 items

all_classes_extended_version.py::TestSquareFunction::test_positive_number 
all_classes_extended_version.py::TestSquareFunction::test_zero 

============================== 2 passed in 1.15s ===============================

Process finished with exit code 0
PASSED [ 50%]PASSED    [100%]
"""


"""
## Design Pattern
    ** Descriptors : Descriptors provide a way to customize attribute access in Python classes. 
    
    A descriptor is a special type of object in Python that customizes the behavior of attribute access (getting, 
    setting, and deleting). To implement a descriptor, you define a class that implements any of these methods:
        
        __get__(self, obj, objtype): Called when you retrieve the attribute (i.e., when you access financial_asset.price).
        
        __set__(self, obj, value): Called when you assign a value to the attribute (i.e., instrument.volatility = value).
        
        __delete__(self, obj): (optional) Called when you delete the attribute.
"""

class PriceDescriptor:
    def __init__(self, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < -273.15:
            raise ValueError("Price below zero should not be possible")
        setattr(obj, self.name, value)

class FinancialAsset:
    price = PriceDescriptor("price")

    def __init__(self, ticker: str, price: float):
        self.ticker = ticker
        self.price = price

# Usage
asset = FinancialAsset("AAPL",250)
print(asset.price)
#asset.price = -300  # Raises ValueError

""" another example: The LazyProperty
The idea behind lazy loading is that the value for the attribute is only computed when it's accessed for the first time,
 rather than when the object is initialized.
"""

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = self.function(obj)
        setattr(obj, self.name, value)
        return value

class DataProcessor:
    def __init__(self, filename):
        self.filename = filename

    @LazyProperty
    def data(self):
        print("Loading data...")
        with open(self.filename, 'r') as f:
            return f.read()

processor = DataProcessor('insert the path of your project here/Built-in error in python.txt')
# Data is not loaded yet
print(processor.data)  # Prints "Loading data..." and then the content
print(processor.data)  # Prints the content without "Loading data..."

"""
Let’s break down how this works step by step:
When @LazyProperty is applied to the data method in DataProcessor:
    
When we create a DataProcessor instance:
    
The first time processor.data is accessed:
    
The second time processor.data is accessed:
   
The key point is that after the first access, the LazyProperty descriptor is effectively replaced by the computed value.
This is why the “Loading data…” message only appears once.
"""

"""
## Creational Design Patterns in Python
Creational design patterns provide various object creation mechanisms, which increase flexibility and reuse of existing
code.

## 4.8 - singleton
    ** Definition/Concept** 
        
    ** Why to use it** 
        
    ** When to use it ** 
        
In Python, we can create Singleton using the `__new__` method.
"""


class SingletonExample:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def another_method(self):
        pass


a = SingletonExample()
b = SingletonExample()
print(a is b)


"""
You can also dissociate the implementation of the singleton logic from the implementation of the class by 
creating a decorator
"""

def singleton(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        # Initialize the database connection
        pass

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)

"""
## 4.5 - factory

    ## Definition/Concept

    ### 2. Why to use it
        Here are some reasons to use the Factory Pattern:
        - **Decoupling**: 
        - **Handling Complexity**:
        - **Code Reusability**: 

    ### 3. When to use it
    The Factory Pattern is particularly beneficial in the following scenarios:

    - **Dynamic Implementation**:
    
    - **Complex Object Creation**: 

    - **Family of Related Objects**: 

    - **Enhanced Control Over Object Creation**: 

==> Use Factory when you're unsure about the exact types and dependencies of the objects your code should work with, 
    or when you want to delegate the responsibility of deciding which class to instantiate.
"""

""" 
Example
The Stock class requires a ticker symbol and price. It has a method get_market_value that returns a string indicating 
its market value per share.
The Bond class needs an issuer and face value. It has a method get_face_value that returns a string indicating its 
face value.
The FinancialInstrumentFactory class creates either a Stock or a Bond instance depending on the instrument_type 
parameter. The **kwargs argument allows us to pass the keyword arguments needed to instantiate the desired 
financial instrument.

This pattern enables you to manage the creation of various financial instrument objects systematically, even when the 
precise types of financial instruments are not known until runtime. The factory method can be extended to handle 
additional financial instrument types as needed, enhancing modularity and scalability in the software design.
"""


class FinancialInstrumentFactory:
    @staticmethod
    def create_financial_instrument(instrument_type, **kwargs):
        if instrument_type.lower() == "stock":
            return StockFactoryExample(**kwargs)
        elif instrument_type.lower() == "bond":
            return BondFactoryExample(**kwargs)
        else:
            raise ValueError("Invalid financial instrument type")


class StockFactoryExample:
    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price

    def get_market_value(self):
        return f"The market value of {self.ticker} is ${self.price} per share."


class BondFactoryExample:
    def __init__(self, issuer, face_value):
        self.issuer = issuer
        self.face_value = face_value

    def get_face_value(self):
        return f"The face value of bond issued by {self.issuer} is ${self.face_value}."


# Create a Stock
stock = FinancialInstrumentFactory.create_financial_instrument("stock", ticker="AAPL", price=150)
print(stock.get_market_value())  # Output: The market value of AAPL is $150 per share.

# Create a Bond
bond = FinancialInstrumentFactory.create_financial_instrument("bond", issuer="US Government", face_value=1000)
print(bond.get_face_value())  # Output: The face value of bond issued by US Government is $1000.

