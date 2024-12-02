# Object Oriented Programming
Abstacting away the implementation details and manipulating objects as singular units.

> To better understand how classes work, think of them as frames or scopes like you did with functions!

> Keep in mind the "abstracting away" part. When we create classes, we want to hide away the internal structure and only allow access to them using a defined interface. (This is where getters and setters come in)

Expanding on the above idea, suppose we have a list inside the instance of a class. We DO NOT want to allow direct access and manipulation of the list. For example, if someone asks for the list, we give them **a copy** of the list, not the actual list itself.

Similarly, whenever we want to modify the behavior of a class or an object, we should only have to modify the internal methods of that class, not something external. This helps keep the code well-structured and maintainable.

## Generators/Enumerators/Iterators
Returning a copy of a list rather than the list itself seems harmless enough. But what if the list had hundreds of thousands of elements or maybe even more than that? Then just copying the entire list and returning the copy will be incredibly inefficient.

This is where generators come in. Instead of computing the entire sequence at once, it tells us how we could generate the sequence ourselves such that we can get the next element without having to compute the entire sequence beforehand.

```python
# Given below is an example of a generator. Notice the 'yield' keyword; it tells python to **pause** the execution at that point, and then return the given value when the __next__() function is called. When it runs out of things to yield, it raises a StopIteration exception.
def genSeq():
    yield 1
    yield 2

# The below __next__() calls evaluate to 1, 2, and a StopIteration exception.
f = genSeq()
f.__next__()
f.__next__()
f.__next__()

# Notice how 'yield' differs from 'return'?
```

# Things I didn't know
```python
# Every class method or data attribute in python is static! Calling it on an instance just passes the instance that it was called on as the first (self) argument.
class SomeClass(object):
    some_var = 0
    def __init__(self, arg1, arg2):
        # ...
    def some_method(self, other):
        # ...

# Supporting the previous exhibit, the two method calls given below are equivalent!
inst1 = SomeClass()
inst2 = SomeClass()
# self = inst1 implied
inst1.some_method(inst2)
# self = inst1 explicitly stated
SomeClass.some_method(inst1, inst2)

# All special methods that can be overloaded including operator functions are enclosed with double underscores. Given below are some of them but there are so many more! Look em up.
class SomeClass(object):
    __add__(self, other):
        # adding logic
    __sub__(self, other):
        # subtraction logic
    __lt__(self, other):
        # less than test logic
    __str__(self):
        # conversion to string logic
    __len__(self):
        # length getting logic

# When looking for attributes in an instance with multiple parents, python looks for it in a left-to-right depth-first search through the superclasses. For example, when looking for an attribute for the class given below, python will first look for it in Class1, then its parent classes, then Class2, and its parent classes and so on...
class SomeClass(Class1, Class2):
    #...

# Once again, thinking of classes as frames will make it much easier to understand why the classes behave the way they do.
```