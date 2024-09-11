"""
Table of contents :
    Part 1 : Introduction and Core concepts
        ## 1.1 - What is Object-oriented programming
        ## 1.2 - Fundamental Concepts in OOP
        ## 1.3 - Benefits of OOP
        ## 1.4 - Classes and Objects in Python
        ## 1.5 - Attributes and Methods in Python
        ## 1.6 - The self Parameter
        ## 1.7 - The `__init__` Method
        ## 1.8 - Encapsulation in Python
        ## 1.9 - Inheritance in Python


## 1.1 - What is Object-oriented programming

    ### Definition/Concept:
        Object-oriented programming (OOP) is a design paradigm where the data structures are defined as objects that
        can possess their behavior (methods) and attributes.

    ### Why do we use OOP:
        Code structured according to OOP principles is easier to manage, test, and debug, given its organized and
        modular nature.
        OOP also allows us to encapsulate (i.e., 'hide') internal state and behavior of objects, exposing only what's
        required. This provides a clean and controllable interface with the object's data and functions.

    ### When to use OOP:
        OOP is excellent for situations where you need to create multiple instances that share common behavior but
        have unique states. It also allows programmers to build complex framework while maintaining readability and
        scalability. OOP also allows multiple developers to work easily at the same time in a common project.


## 1.2 - Fundamental Concepts in OOP

    The backbone of OOP includes these four fundamental concepts:
    1. **Encapsulation:** Encapsulation is all about safe data storage. It binds together code (methods) and the data
                          it manipulates (attributes), keeping both safe from outside interferences and misuse.

    2. **Inheritance:** Inheritance allows classes to inherit commonly used state and behavior from other classes,
                        reducing repetitive code.

    3. **Polymorphism:**

    4. **Abstraction:**


## 1.3 - Benefits of OOP

    OOP brings numerous advantages to the table:
        - **Modularity for easier troubleshooting:** When an issue pops up, you can typically spot it in the
                                                     code block or 'object' in question. For example, in a complex
                                                     trading algorithm, if a calculation error appears, you can likely
                                                     isolate the problem to a specific stock object - which greatly
                                                     simplifies the debugging process.

        - **Reuse of code through inheritance:** Inheritance allows classes to inherit characteristics from existing
                                                classes. Consequently, it helps in reducing code redundancy,
                                                particularly when creating intricate financial models with common
                                                components.

        - **Flexibility through polymorphism:** This is extremely useful when implementing complex systems that
                                                require a single interface to control different inputs.

    Through these advantages, the principles of OOP allow us to model and solve complex problems more robustly,
    efficiently, and intuitively.


## 1.4 - Classes and Objects in Python
    **Definition/Concept:**
        In object-oriented programming (OOP), a class is a blueprint or template that defines the variables and
        the methods (functions) common to all objects of a certain kind. An object is a specimen of a class.

    **Why:**
        Using classes, we encapsulate data and the methods that operate on them so they are easy to reuse and maintain.
        Objects provide a simple way to access this data and methods provided by classes.

    **When to use it:**
        Classes and objects are used when we need to group relevant data and methods into a single place.


## 1.5 - Attributes and Methods in Python
    **Definition/Concept:**
        An attribute is a characteristic of an object. These are essentially variables that are bound to the
        instances of the class. Methods, on the other hand, define the behaviors of these objects. These are
        like functions defined within a class.

    **Why:**
        Attributes and methods encapsulate the state and logic of the entities modelled into a cohesive unit.

    **When to use it:**
        Attributes are used when we need information about the object that must endure for as long as the object exists.
         Methods are used when behavior or action needs to be defined for an object.


## Summary / Key take-away ##
    A Class in Python is the blueprint from which individual objects are created. It is a user-defined prototype that
    consists of attributes and methods that act on those attributes. Attributes are the characteristics of the class,
    while methods define the behaviors of the class.

"""

"""
EXAMPLE : First example of a class in Python
"""


class FinancialAsset:
    def __init__(self, ticker):
        self.ticker = ticker

    def display_ticker(self):
        print(f'Ticker Symbol: {self.ticker}')


apple_equity = FinancialAsset('AAPL')
apple_equity.display_ticker()  # Ticker Symbol: AAPL

""" 
## 1.6 - The self Parameter

    **Definition/Concept:** 
        `self` is a parameter in the instance method and is a reference to the instance of the class. 
    
    **Why:** 
        The `self` represents the instance of the class and by using the `self` keyword we can access the attributes 
        and methods associated with the instance.
    
    **When to use it:** 
        `self` is also used as a parameter in instance methods notably in object initializers which are 
        established by the `__init__` method.
    
    **1.6.1 - Understanding self in Depth
        self as a Reference to the Instance: When a method is called on an instance, Python automatically passes this 
        instance as the first argument to the method.
        self is a Convention: Although self is a convention, you can technically use any name. However, using self is 
        highly recommended for readability and to adhere to standard conventions.


## 1.7 - The `__init__` Method

    **Definition/Concept**: 
        The `__init__` method is one of Python's special methods used for initializing the attributes of a class.
    
    **Why**: 
        The `__init__` method when declared in a class, is automatically invoked when the object of the class is 
        instantiated.
    
    **When to use it:** 
        `__init__` is handy when we need to initialize our object's attributes when the object is  being created.


In the above example, we see that `self` is used as the first parameter of the `__init__` method as well as 
being used to define the `display_ticker()` method.


## 1.8 - Encapsulation in Python

    ** Definition/Concept **    
        Encapsulation is a core concept in Object-Oriented Programming (OOP). It refers to restricting access to
        certain details of an object and only exposing what is necessary for the outside world to interact with. 
        Essentially, it involves bundling the data (attributes) and the methods (functions) that operate on the data 
        into a single unit, or class, and controlling the access to that data. Encapsulation helps to safeguard the 
        internal state of the object and protects it from unauthorized direct access and modification.
    
    ** Why to use it **  
        There are a couple of main benefits to utilizing encapsulation in your code:
        1. Security: Encapsulation protects the integrity of the data by allowing only authorized functions to 
                    access and modify it. This means the internal state of the object is shielded from unintended 
                    alterations.
        2. Ease of Use and Maintenance: By limiting the interface to an object, encapsulation makes the object easier 
                                        to understand and use correctly. Furthermore, by hiding the internal workings, 
                                        changes can be made to the internal structure without affecting the code that 
                                        uses the object.


## 1.9 - Inheritance in Python

    ** Definition/Concept ** 
        Inheritance is a pillar of Object-Oriented Programming (OOP). It allows a class to inherit features 
        (methods and properties) from another class. The class being inherited from is known as the parent class, 
        superclass or base class, and the class that inherits is known as the child class, subclass or derived class.

    ** Why and When to Use Inheritance **
        Inheritance is primarily used to enhance code reusability. Instead of writing repetitive code, common 
        features can be defined in a base class, and other classes can inherit these features. Inheritance should
        be used when there's a clear hierarchical relationship among classes. 
         
    ** Additional Properties **
        An additional feature of inheritance is that a subclass could be considered as the parent class in the code.
        When checking for the type of a subclass, the subclass will return true when we test the following equality:
        isinstance(bond, FinancialAsset) with bond an instance of the Bond class. However, a parent class could not
        be considered as a subclass. This principle is the class hierarchy principle
        
"""

"""
EXAMPLE : In finance, we deal with different types of financial instruments such as bonds and stocks. 
          Each of these instruments can be modeled as a class, inheriting from a base class `FinancialAsset`.

'Bond` class inherit from the `FinancialAsset` class and add additional attributes specific to each instrument. 
It also contain its own methods.
"""


# Base Class
class FinancialAsset:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price


# Derived Class
class Bond(FinancialAsset):
    def __init__(self, symbol, price, face_value, maturity_date):
        super().__init__(symbol, price)
        self.face_value = face_value
        self.maturity_date = maturity_date

    def calculate_ytm(self):
        pass  # Implement YTM calculation logic here


asset = FinancialAsset("USD", "1.0")  # create financial asset object
bond = Bond('T 5 15/09/2045', 100, 100000000, '2023-10-12')  # create bond object
print(f' is bond instance of Bond : {isinstance(bond, Bond)}')  # True
print(f' is bond instance of FinancialAsset : {isinstance(bond, FinancialAsset)}')  # True
print(f' is asset instance of Bond : {isinstance(asset, Bond)}')  # False


