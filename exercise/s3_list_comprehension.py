"""
Exercise 1: Market Capitalization Filter

Given a dictionary of companies and their market capitalizations in billions, use a list comprehension to produce a list
of companies with a market capitalization of more than $500 billion.
"""

market_caps = {
    'Apple': 2200,
    'Microsoft': 1980,
    'Google': 1450,
    'Amazon': 1675,
    'Tesla': 650,
    'Zoom': 120
}

# Expected Output: ['Apple', 'Microsoft', 'Google', 'Amazon', 'Tesla']


"""
Exercise 2: Normalizing Data

Given a list of numbers, normalize them so they range between 0 and 1. 
To normalize a value, you'd use the formula (value - min_value) / (max_value - min_value)

"""

data = [50, 100, 150, 200, 250]
# Step 1: Find min and max values of the list

# Step 2: Normalize the numbers

# Expected Output: [0, 0.25, 0.5, 0.75, 1]

"""
Exercise 3: Stock Price Adjustments
Given a list of stock prices and a separate list of dividend payouts, adjust the stock prices for dividends.

Hint: use zip() in the list comprehension
The zip() function is a built-in function in Python that is used to combine multiple iterables (like lists or tuples) 
element-wise. When you zip two or more iterables, it returns an iterator of tuples, where the i-th tuple contains 
the i-th element from each of the argument sequences.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped)) #output => [(1, 'a'), (2, 'b'), (3, 'c')]

In list comprehension the synthax to manipulate tuple is the following: 
[ *operation to perform* for value1, value2 in zip(list1, list2)]

example: [str(value1) + value2 for value1, value2 in zip(list1, list2)] ==> ['1a', '2b', '3c']
"""

prices = [100, 101, 102, 103, 104]
dividends = [0, 0.5, 0, 0, 1]

# expected Output: [100, 100.5, 102, 103, 103]













