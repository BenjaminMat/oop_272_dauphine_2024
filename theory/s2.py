"""
Table of contents :

        ## Encapsulation in Python - Part 2
        ## Inheritance in Python - Part 2
        ## Dunder Methods

## Encapsulation in Python - Part 2

    Encapsulation is one of the fundamental principles of object-oriented programming. It involves bundling data
    (attributes) and the methods that manipulate them into a single unit (the class) and controlling access to this
    data from outside the class.

    **Definition/Concept: Public and Private attributes in Python:**
        Unlike languages like Java or C++, Python does not have a strict mechanism to define attributes or methods
        as "private" or "public." Instead, Python follows a naming convention to indicate the developer's intention
        regarding the usage of attributes and methods.

        *Public Attributes and Methods:**

        *"Private" Attributes and Methods (by convention):**

        *Name Mangling for Attributes and Methods:**

    **Why & When to use it:**

"""


class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner  # Public
        self._balance = initial_balance  # "Private" by convention
        self.__transaction_history = []  # "Private" with name mangling

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__add_transaction(f"Deposit of {amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__add_transaction(f"Withdrawal of {amount}")
            return True
        return False

    def get_balance(self):
        return self._balance

    def __add_transaction(self, transaction):
        self.__transaction_history.append(transaction)


# Usage
account = BankAccount("Someone", 1000)
print(account.owner)  # Access to a public attribute
account.deposit(500)
# The following lines are possible but not recommended:
print(account._balance)  # Access to a "private" attribute by convention
print(account.get_balance())  # Using a public method to access the balance

# print(account.__transaction_history)  # This will raise an AttributeError
print(account._BankAccount__transaction_history)  # Access to the attribute with name mangling

"""
## Inheritance in Python - Reminder

    ** Definition/Concept ** 
        Inheritance is a pillar of Object-Oriented Programming (OOP). It allows a class to inherit features 
        (methods and properties) from another class. The class being inherited from is known as the parent class, 
        superclass or base class, and the class that inherits is known as the child class, subclass or derived class.

## Multiple Inheritance in Python

    **Definition/Concept:**
        Python supports multiple inheritance, which means that a class can inherit from multiple parent classes.
        This allows a derived class to combine functionalities from several base classes.

    ** Syntax of Multiple Inheritance:**
        Python uses a straightforward syntax to define multiple inheritance by listing all parent classes
        in the parentheses after the class name.

"""


class BaseClass1:
    def method(self):
        print("Method in BaseClass1")


class BaseClass2:
    def method(self):
        print("Method in BaseClass2")


class DerivedClass(BaseClass1, BaseClass2):
    def method(self):
        print("Method in DerivedClass")
        BaseClass1.method(self)
        BaseClass2.method(self)


derived_class = DerivedClass()
derived_class.method()

"""
    **Practical Benefits of Multiple Inheritance:**
        Combining Functionality:
            Multiple inheritance allows a class to combine functionalities from different classes into one.
        Code Reuse from Multiple Sources:
            Useful when a class needs to inherit behaviors from several unrelated classes.
        Implementing Complex Designs:
            Enables creating more flexible and adaptable class structures.
"""


class BaseClass1Modified:
    def method_from_base_class_1_modified(self):
        print("Method from BaseClass1Modified")


class BaseClass2Modified:
    def method_from_base_class_2_modified(self):
        print("Method from BaseClass2Modified")


class DerivedClassModified(BaseClass1Modified, BaseClass2Modified):
    pass


derived_class_2 = DerivedClassModified()
derived_class_2.method_from_base_class_1_modified()
derived_class_2.method_from_base_class_2_modified()

"""
    **Method Resolution Order (MRO) in Detail**
        The Method Resolution Order (MRO) is crucial for understanding how Python handles inheritance, especially 
        multiple inheritance.

        The MRO defines the order in which Python searches for methods and attributes in a class hierarchy.

        This is particularly important in multiple inheritance scenarios where multiple parent classes may define 
        the same method.
"""

# Visualizing MRO:
# You can visualize the MRO of a class using the mro() method or the __mro__ attribute:
print(DerivedClass.mro())

# Detailed Example of Method Resolution: Example to illustrate how the MRO works:

class A:
    def method(self):
        print("Method in A")


class B(A):
    def method(self):
        print("Method in B")


class C(A):
    def method(self):
        print("Method in C")


class D(B, C):
    pass


d = D()
d.method()

"""
# 4. Using super()

# Definition/Concept:
# The super() function is a powerful tool in Python for managing inheritance elegantly and flexibly.

# 4.1 Definition and Utility:

# Purpose of super():
# super() allows calling methods from the parent class in a derived class. It is particularly useful for:
# - Extending the behavior of a parent method without completely rewriting it.
# - Ensuring proper management of multiple inheritance.
"""


# 4.2 Basic Syntax:
class Parent:
    def method(self):
        print("Method in Parent")


class Child(Parent):
    def method(self):
        super().method()  # Calls the method from the parent class
        print("Method in Child")


child = Child()
child.method()

# In the case of multiple inheritance, super() follows the order defined by the MRO:
class A:
    def method(self):
        print("Method in A")


class B(A):
    def method(self):
        print("Method in B")
        super().method()


class C(A):
    def method(self):
        print("Method in C")
        super().method()


class D(B, C):
    def method(self):
        print("Method in D")
        super().method()


d = D()
d.method()


# Managing Parent Method Calls in Multiple Inheritance
# Direct Call to a Parent Class Method:  In some cases, you might want to call a specific parent class method directly
# rather than following the MRO:
class A:
    def method(self):
        print("Method in A")


class B:
    def method(self):
        print("Method in B")


class C(A, B):
    def method(self):
        print("Method in C")
        A.method(self)  # Direct call to A's method
        B.method(self)  # Direct call to B's method


c = C()
c.method()
# Outputs:
# Method in C
# Method in A
# Method in B


"""
** Dunder methods**

## 1 - Overall definition
    **Definition/Concept**
        "Dunder" is short for "Double underscore" (__). Dunder methods are a set of predefined methods you can use to 
        enrich your classes in Python. You've already seen these special methods in previous class with the
        `__init__` method

    **Why**
        
   **When to use it**
       

You can find a list of dunder methods in the additional resources directory 

## 2 - Use built-in functions for classes by implementing dunder methods

    **Definition/Concept**
        The dunder method for specifying the behavior of built-in Python functions like `len` or `str` involves 
        implementing specific, predefined methods within your class using double underscores (__). 
        Such methods include `__len__`, `__str__`, and others, which Python calls when built-in functions of the same 
        name are used on instances of your class. 

    **Why**
        
    **When to use it**
       

    **How to implement it**
       
"""

"""
Example of dunder method : __len__
    __len__(self) determines the “length” of your object, which allows you to use the len(obj) syntax.
    If we do not implement the dunder method, len(instrument_list) will return the following : Error: object of 
    type 'InstrumentList' has no len()
"""


class FinancialAsset:
    def __init__(self, ticker):
        self.ticker = ticker

    def display_ticker(self):
        print(f'Ticker Symbol: {self.ticker}')


class InstrumentList:
    def __init__(self, list_of_instrument):
        self.instruments: [FinancialAsset] = list_of_instrument


class InstrumentListWithDunder:
    def __init__(self, list_of_instrument):
        self.instruments: [FinancialAsset] = list_of_instrument

    def __len__(self):
        return len(self.instruments)


asset1 = FinancialAsset('AAPL')  # create a Financial Asset object
asset2 = FinancialAsset('MSFT')  # create a Financial Asset object

# instrument_list = InstrumentList([asset1, asset2])
instrument_list = InstrumentListWithDunder([asset1, asset2])
print(len(instrument_list))

"""
## 3.2.1 -The __str__() method
    **Definition/Concept**:
        The `__str__()` method in Python is another "dunder" method associated with a class. It is meant to return a 
        string representation of an object which is intended to be informative and easily readable for end-users.

    **Why**:
        
    **When to use it**:
    
"""


class FinancialAssetWithStrDunder:
    def __init__(self, ticker, price, currency):
        self.ticker: str = ticker
        self.price: float = price
        self.currency: str = currency

    def __str__(self):
        return f'The ticker for this asset is {self.ticker} and its price is {self.price} {self.currency}'


asset_str_dunder_example = FinancialAssetWithStrDunder('AAPL', 178, 'USD')
print(str(asset_str_dunder_example))

"""
## 3.2.2 - The __repr__() Method
    **Definition/Concept**:
        The `__repr__()` method in Python is a dunder method associated with a class.  
        It should return a string that looks like a valid Python expression and could be used to recreate an object with 
        the same properties.  Ideally, using `eval(repr(obj))` should produce an object equivalent to `obj`.

    **Why**:
       
    **When to use it**:
        
    Benefits of __repr__() when implementing complex Python framework:
        Traceability: In complex financial simulations or optimizations, you might be dealing with hundreds of 
                    instrument objects. If something goes wrong, having a clear __repr__() output can help you trace 
                    back to the exact instrument causing the issue.

        Reproducibility: Sometimes you may need to send the state of your system (the exact instruments and their 
                    properties) to someone else for verification, testing, or audit purposes. With a clear __repr__() 
                    method, you can recreate the exact state of objects with ease.

        Logging: When logging system activities, having a clear representation of the objects being processed can be 
                useful for future reference or debugging.
"""


class FinancialAssetWithDunderRepr:
    def __init__(self, ticker, price, currency):
        self.ticker: str = ticker
        self.price: float = price
        self.currency: str = currency

    def __str__(self):
        return f'The ticker for this asset is {self.ticker} and its price is {self.price} {self.currency}'

    def __repr__(self):
        return f"FinancialAssetWithDunderRepr('{self.ticker}', {str(self.price)}, '{self.currency}')"


asset_str_dunder_example = FinancialAssetWithDunderRepr('AAPL', 178, 'USD')
print(repr(asset_str_dunder_example))

assetExampleEval = eval(repr(asset_str_dunder_example))
# eval() convert an "official" string representation of an object to the object. Here we create a new object.
print(str(asset_str_dunder_example))  # This new object is an instance of FinancialAssetWithDunderRepr

"""
## 3.3 - Operator overloading

    Built-in operator does not work on custom classes. For example, if we try to use "+" or any other operator such as
    "-", "*", "/", ">", ... this will raise a TypeError as the behavior for these operators are not implemented for the
    object. If we want to use built-in operator for custom objects we need to use dunder methods.
    The only exception is the "=" operator. If we don't implement the dunder method to specify the behavior of the
    equal operator for custom objects, python will check for object identity (i.e., both objects are the
    same instance). Thus even though each attributes of 2 objects are equal the "=" will return false

    Implementing dunder methods referring to built-in operator is called operator overloading. 
    **Definition/Concept**: 
        It is the ability of one operation, such as addition or multiplication, to behave in one way or more 
        according to the data or objects being operated upon.

    **Why**: 
       
    **_When to use `Operator Overloading`_**: 
        

    You will find below example of operator overloading. 
"""

"""
Example of operator overloading for "+" and "-" operator
Here the operator overloading is realized by implementing the following method : __add__ and __sub__
"""


class FinancialInstrument:
    def __init__(self, symbol, price, currency):
        self.ticker = symbol
        self.price = price
        self.currency = currency


class BankAccount:
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency

    def __add__(self, other):
        if isinstance(other, BankAccount) and other.currency == self.currency:
            self.balance = self.balance + other.balance
            return self.balance

        if isinstance(other, FinancialInstrument) and other.currency == self.currency:
            self.balance = self.balance + other.price
            return self.balance

    def __sub__(self, other):
        if isinstance(other, BankAccount) and other.currency == self.currency:
            self.balance = self.balance - other.balance
            return self.balance

        if isinstance(other, FinancialInstrument) and other.ticker == self.currency:
            self.balance = self.balance - other.price
            return self.balance


acc1 = BankAccount('Account 1', 1200, 'USD')
acc2 = BankAccount('Account 2', 800, 'USD')

print(acc1 + acc2)
print(acc1 - acc2)

asset = FinancialInstrument('USD', 300, 'USD')
print(acc1 + asset)

"""
Example of the dunder method __eq__()
"""


class FinancialAssetWithNoDunderEq:
    def __init__(self, ticker):
        self.ticker: str = ticker


print('test equality for object with no __eq__() implementation')
asset = FinancialAssetWithNoDunderEq('AAPL')
asset1 = FinancialAssetWithNoDunderEq('AAPL')
print(f'is object with same attributes equal : {asset == asset1}')  # false


class FinancialAssetWithDunderEq:
    def __init__(self, ticker):
        self.ticker: str = ticker

    def __eq__(self, other):
        # First, ensure that the other object is an instance of the same class
        if isinstance(other, FinancialAssetWithDunderEq):
            return self.ticker == other.ticker
        return False  # Return NotImplemented for types that are not of the same class


asset_eq_dunder_example = FinancialAssetWithDunderEq('AAPL')
asset_eq_dunder_example1 = FinancialAssetWithDunderEq('AAPL')
asset_eq_dunder_example2 = FinancialAssetWithDunderEq('MSFT')
print('__eq__() example')
print(f'asset_eq_dunder_example = FinancialAssetWithDunderEq("AAPL") //'
      f' asset_eq_dunder_example1 = FinancialAssetWithDunderEq("AAPL") //'
      f' asset_eq_dunder_example2 = FinancialAssetWithDunderEq("MSFT")')
print(' ')
print(f'asset_eq_dunder_example == "AAPL": {asset_eq_dunder_example == "AAPL"}')  # False
print(
    f'asset_eq_dunder_example == asset_eq_dunder_example1: {asset_eq_dunder_example == asset_eq_dunder_example1}')  # true
print(
    f'asset_eq_dunder_example == asset_eq_dunder_example2 : {asset_eq_dunder_example == asset_eq_dunder_example2}')  # false

