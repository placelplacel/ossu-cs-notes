# MIT 6.00.1x

Programming is about three things:
1. Primitive operations provided to us by the manufacturer.
2. Doing compound computations using those primitive operations.
3. Manipulating those compound computations as if they were primitives themselves.

> **Something Interesting:** Any computation can be done with the help of just six primitive operations:
> - Move Left,
> - Move Right,
> - Scan,
> - Read,
> - Write,
> - and Do Nothing.
>
> This property is known as **Turing Complete** and the above statement was proved by Alan Turing.

## Inside a Computer
**Memory:** Remembers results (or instructions in case of a **stored program computer**).

**Arithmetic Logic Unit:** Performs the operations.

**Control Unit:** Tells the ALU what operations to do. This contains a **program counter** which keeps track of where the computer is in the list of instructions, i.e., which instruction to act on next.
- The program counter usually goes back to the start of the instruction list after the execution of the program ends.

**Input/Output:** Pretty self-explanatory.


## Meanings
**Computational Thinking:** Any problem can be thought of as a mathematical problem with expressions and formulas.

**Fixed Program Computer:** Designed for a specific purpose, i.e., only has a single set of instructions that it can execute.

**Stored Program Computer**: Can execute any set of instructions that is loaded into it. These usually have the instructions stored in their memory.

**Syntax:** The structure of the expression.

**Static Semantics**: If the expression has a meaning.

**Semantics**: The meaning of the expression.

**Memoization:** Caching the results of computations and just looking them up when we need it again instead of redoing the said computations a bajillion times. (_HASHMAAAAAPS!!!_)

# Guess-and-Check
We will try to find the square roots in the following demonstations.

## Exhaustive Enumeration
Here, we start with an initial guess and then keep making small increments hoping that we get close enough to the answer, exhaustively enumerating through a specific range of guesses.

```python
x = 25
epsilon = 0.0001
step = 0.01
guess = 0.0
guess_count = 0

while abs((guess ** 2) - x) >= epsilon:
    guess_count += 1
    if guess >= x:
        break
    else:
        guess += step

if abs((guess ** 2) - x) >= epsilon:
    print("Failed")
else:
    print(guess, "is a close enough square root of", x)
```

This has multiple problems: not only does it take thousands of guesses to get anywhere near our answer if the step size is too small; if the step size is too big, it will just step over the answer and we will spend enormous amounts of computing power and time getting farther and farther away from the answer.

## Bisection Search
We know that the square root of a positive number greater than or equal to 1, lies between 1 and that number (both inclusive). We also know that a square function follows an order: it increases as x increases. This makes it a suitable candidate for using bisection search!
- Here, we start with a range for our guess and choose the middle of it as our initial guess.
- Then we check if our answer is too big or too small.
  - If it is too big, we discard the greater half of our original range and look for it in the lesser half. If it is too small, we discard the lesser half and look for it in the larger one.
- And then we keep going like this, choosing the middle of the chosen half as our guess on every step, until we find a close enough answer.

```python
x = 0.8
epsilon = 0.0001
low = 0.0
high = 1.0
guess = (low + high) / 2
guess_count = 0

while abs((guess ** 2) - x) >= epsilon:
    guess_count += 1
    if guess ** 2 > x:
        high = guess
    else:
        low = guess
    guess = (low + high) / 2

print(guess, "is close enough to the square root of", x)
print("It took", guess_count, "guesses to get the given answer.")
```

Benchmarking this, you can immediately see the power of this algorithm. It brings down the number of guesses needed to get to the answer from the thousands to the tens, zeroing in on the answer incredibly quickly. Not only that, on every iteration, it cuts the range for our guesses in half!

So, if it took, say `g` guesses to get to an answer, the final search range will be `1/(2^g)`th the size of the original search range. This is an example of a logarithmic algorithm.

## Newton-Raphson
Now we harness the power of mathematics to make the algorithm even better and even faster! This method is based on the following method presented by Sir Isaac Newton for approximating the roots of _any_ polynomial.

> Say we have a polynomial `p(r)`. Given a good guess `g`, a better guess can be calculated by evaluating the expression `g - p(g)/p'(g)`.

Here, when we say we are trying to find the square root of x, we are actually just trying to find the root of the polynomial `p(r) = r^2 - x` so our expression for a better guess will be `g - (g^2 - x)/2g`.

```python
x = 56.0
epsilon = 0.0001
guess = 1.0
guess_count = 0

while abs((guess ** 2) - x) >= epsilon:
    guess_count += 1
    guess -= ((guess ** 2) - x) / (2 * guess)

print(guess, "is close enough to the square root of", x)
print("It took", guess_count, "guesses to get the given answer.")
```

Benchmarking this made me orgasm, holyyyy. This is why I love math.

# Things I didn't know

## Things to REALLY keep in mind
```python
# This will ALWAYS return a float even if both operands are integers. Integer division is done using the // operator but it STILL returns the integer as a float. (I am wayyy too used to C-like languages)
5/4

# You can only read from variables defined outside a scope, you can't modify it in any way. The given example results in an error saying that 'x' is being used before being defined: this is because 'x' has been defined outside the scope of the function (in the global scope), but not in it!
def foo():
    x = x + 1
    print(x)
x = 5
foo()

# If you really want to modify the value of the variable from inside the function, you will have to declare it as a 'global' variable inside the function. This works as intended.
def foo():
    global x
    x = x + 1
    print(x)
x = 5
foo()

# Continuation of the previous exhibit: this is valid and prints out '6'. (This is some rather funky behavior as someone who comes from a C-like background)
def foo():
    y = x + 1
    print(y)
x = 5
foo()

# Out-of-bound ranges when slicing strings does not result in an error! It just returns an empty string! The given expressions evaluates to ''.
"hi"[2:]
"hi"[:-3]

# In case of name collisions when importing everything from modules/files, the definition from the current file will be used. In the given example, running inventory.py will print 'aa', not 'AA'.
# file: batteries.py
aa = "AA"
# file: inventory.py
from batteries import *
aa = "aa"
print(aa)

# Not something solely about programming, but **read every word of the question carefully**! There have been so many instances where I have gotten stuck on a problem for 20 minutes or smt because I missed a crucial detail.

# Tuples aren't defined using round brackets, it's the commas that python looks for. For example, the first expression given below is evaluates to (1,), which is a tuple, but the second expression evaluates to just 1!
(1,)
(1)

# Expanding on the previous exhibit, because the brackets aren't important for declaring tuples, we can omit them if we want! The expressions below are tuples.
1,
1, 2, "yep"

# Oh, and try not to do this thinking it will print out a tuple. I don't even have to explain why it's stupid...
print(1,)

# Or this... (like seriously... please don't...)
1, 2, "yep",[2]

# You can deconstruct tuples! The expression below binds the value of 2 to 'x' and 3 to 'y'.
(x, y) = (2, 3)

# list.pop() returns the value that it removes! In the given example, the last line evaluates to 3!
l = [1, 2, 3, 4]
l.pop(2)

# If you are ever confused about behaviors related to unwanted mutations and stuff, draw an environment model diagram! It really helps a lot to understand what's going on behind the scenes!

# Try to figure out why this doesn't work: we are trying to remove elements from l1 that are already in l2.
l1 = [1, 2, 3, 4]
l2 = [1, 2, 5, 6]
for i in l1:
    if i in l2:
        l1.remove(i)

# HINT: Python uses an internal counter to keep track of which index in the list the interator is at.
# HINT: Mutations.

# Extending the previous exhibit, here is how it should've been implemented. What changed?
for i in l1[:]:
    if i in l2:
        l1.remove(i)

# Python has an 'is' operator to check if two objects are the same. It doesn't check the value like '==', it checks if they are literally the same object. For example, the following expressions evalulate to True and False.
l1 is l1
l1 is l1[:]

# You can simply convert the string 'NaN' to a float or an integer to have it evaluate to 'nan'. (Fun fact: 'NaN' stands for 'Not a Number'!)
float("NaN")

# 'else' can also be used with a 'for' loop! In such a scenario, it is only executed if the 'for' loop doesn't encounter a 'break' in its execution. Given below are two examples demonstrating this behavior.
for i in range(5):
    # ...
else:
    # Will be executed

for i in range(5):
    break
else:
    # Won't be executed
```

## Other Stuff
```python
## !python

# The return type will be a float if EITHER of the two operands in an expression is a float.
2 + 5.0
2.0 + 5
5.0 * 2.0

# This is syntactically correct and evaluates to 4.
a = - - 4

# This is also syntactically correct even if it might not look like it! The expression to the right evaluates to 5, and the actual expression is 'a > +5' or 'a > 5'
a > + 5

# This evaluates to False. Python evaluates conditions as it encounters them! In the below expression, it first evaluates 'not True', yielding 'False and False or False'. Then, it will evaulate the 'False and False', finally resulting in 'False or False' which evaluates to False.
not True and False or False

# This is the python equivalent of null, I knew that. What I didn't know was that it has its own type called the NoneType!
None

# The 'in' operator can also be used to check if something is in a given collection. The expressions below evaluate to true.
"foo" in "afoot"
"oof" not in "afoot"

# You can multiply ANY ordered collection, whether it is a list, a tuple, a string, whatever, with numbers to copy and paste it multiple times. In these cases, the expressions evaluate to 'hihihi' and [1, 2, 1, 2].
3 * "hi"
2 * [1, 2]

# The python print function, if used with multiple arguments, automatically adds a space in between them when printing them out. (Whyyyyyy)
print("arg1", "arg2", "arg3")

# Concatenation can be used to work around the above behavior
print("arg1" + "arg2" + "arg3")

# If a for loop is provided with a variable of the same name as an already existing variable, then the for loop uses that existing variable rather than creating a new one. For example, the code below prints out '0, 1, 2, 3, 4, 4' instead of what I expected ('0, 1, 2, 3, 4, 10').
num = 10
for num in range(5):
    print(num)
print(num)

# Strings are immutable! For example, the expression below results in an error.
s = "hello"
s[0] = "j"

# You can specify the end character of the print() function to have it be something other than '\n'. The given code prints 'helloworld' on the same line.
print("hello", end = "")
print("world")

# All ordered collections can be sliced just like strings! The expression below evaluates to ('yep', 'you')
(1, 2, "yep", "you", "can")[2:4]

# You can delete stuff in Python... yep... The following code prints out [1, 2, 4]. This also works with other mutable collections like dictionaries.
l = [1, 2, 3, 4]
del(l[2])
print(l)

# There is a separate sorted() function which returns a sorted copy of the list rather than sorting the list itself.
sorted(l)

# You can turn a string into a **list** of characters. The following expression evaluates to ['h', 'e', 'l', 'l', 'o', '!'].
list("hello!")

# You can also join the elements of a list of strings as a string as shown below. Heck, you can even decide what separator you want to use! The given expressions evaluate to "1234" and "1sep2sep3sep4". (Yes, the syntax is quite funky)
"".join(["1", "2", "3", "4"])
"sep".join(["1", "2", "3", "4"])

# Python throws a KeyError when trying to index into a dictionary with a key that is not in it rather than returning something like None. The second expression that follows causes an error.
d = {"key1": "val1", "key2": "val2"}
d["some key"]

# Dictionary keys must be hashable (all immutable types are hashable). The second expression given below causes an error.
# WARNING: Beware floating-point errors!
l = [1, 2, 3]
d = {"str": "valid", l: "invalid" }
```