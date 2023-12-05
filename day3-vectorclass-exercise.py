# A CLASS is like a blueprint for an object
# classes are created by keyword class
# attributes are variables that belong to a class
# attributes are always public and can be accessed using the dot operator. e.g. myClass.myAttribute

# Object: Instance of Class
# It is a copy of the class but with actual values
# Consists of: Identity, State/Attributes, and Behaviors
# All objects of the class share the attributes and behaviors, but the values of these are unique for each object

# Example
class Dog:
    # sample class attributes
    attr1 = "mammal"
    attr2 = "dog"

    #sample method
    def fun(self):
        print(f"I'm a {self.attr1}")
        print(f"I'm a {self.attr2}")

# object instantiation
Rodger = Dog

# access class attributes and methods through objects
print(Rodger.attr1)


import numpy as np

# When a class is instantiated, 
# Python creates an empty object, which it knows to be self
# THEN Python calls the init method, passing it that object

class Vector:
    def __init__(self, *components):
        self.components = components
        # self is a convention for the first parameter name in method definition, 
            # refers to the INSTANCE of the class
            # *** gives the instance a way to reference itself in the class *** 
            # *** When you create an instance of a class, the __init__method is automatically called
            # and the instance is automatically passed as self to the __init__ method.
            # FOR THIS REASON, self is required in every method declaration ***
        # *arg is variable-length

        # methods that start and end with __ are called dunder methods or magic methods. They differ from other Python methods only in that Python can implicitly call them.
        # Since they are called implicitly, they are almost never called by name, so they don't need convenient names, 
        # so they are given funny __names__ to prevent them being reassigned on accident.

    # This method overrides the default string method
    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"
    # f: make string literal, lets you inject expressions into the string with {}
    # str: the datatype conversion built-in function
    # ', ' this is the separator for the join function. comma then space
    # map(str, self.components) applies the str function to each element in self.components

    # Vector addition method
    def __add__(self, other):
        # Check to see if dimensions are the same
        if len(self.components) != len(other.components):
            raise ValueError("Vector dimension mismatch. Cannot perform addition")
        
        result_components = [a + b for a, b in zip(self.components, other.components)]
        # zip combines 2+ iterables element-wise into a list of tuples where the i-th tuple contains the i-th element from each iterable
        # It stops when the shortest input iterable is exhausted. Any further values in the others are ignored
        # e.g. [1,2,3] zipped with ['a', 'b', 'c'] gives [(1, 'a'), (2, 'b'), (3, 'c')]

        #[... for a, b in...] <- Destructuring statement. Unpacks each tuple into the two variables from the zip
        return Vector(*result_components)
    
    def dot_product(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vector dimension mismatch. Cannot perform multiplication")
        
        vector_a = np.array(self.components)
        vector_b = np.array(other.components)
        # arrays are a data structure fundamental to numpy that are created by its nparray class.
        return np.dot(vector_a, vector_b)
    
    def scalar_multi(self, other):
        vector_a = np.array(self.components)
        return vector_a * other
    
vector1 = Vector(1, 2, 3)
print(str(vector1))
vector2 = Vector(4, 5, 6)
vector3 = Vector(2, 4, 6, 8, 7, 6, 5, 4)
vector4 = Vector(1, 3, 5, 6, 7, 8, 4, 5)

# resultV = vector1 + vector2
# print(f"{vector1} + {vector2} = {resultV}")
# resultV2 = vector3 + vector4
# print(f"{vector3} + {vector4} = {resultV2}")
# dotResult = vector1.dot_product(vector2)
# print("Dot Product", dotResult)
# scalarResult = vector2.scalar_multi(5)
# print("Scalar result", scalarResult)