# Computational Complexity
Figuring out what happens to the efficiency or runtime of a program as the size of the input grows. This leads us to consider three cases:
- **Best Case:** The smallest amount of time that the algorithm will take.
- **Average Case:** How long the algorithm will take on average.
- **Worst Case:** The longest amount of time the algorithm will take.
> We generally care more about the worst case scenario.

> We do not time the algorithms to compare them as it not only evaluates the algorithm but also its implementation and the machine that it is running on. Not very helpful when we only care about the efficiency of the algorithm!

## Big Oh Notation
Determining how the complexity of a program grows as the size of the input approaches infinity, in the worst case. (_Asymptotic Growth_)

Listed below are the different classes of complexities, ranked from the lowest to the highest in terms of how complex they are. We strive to get as far up as possible.
```python
# n is the size of the input and c is a constant.
- O(1)
- O(log(n))
- O(n)
- O(nlog(n))
- O(n^c)
- O(c^n)
```

> Sometimes, the algorithm to find an answer cannot be simplified any more than the exponential class and we are stuck with a rather inefficient procedure. In such a situation, we prefer to come up with a faster algorithm to find an approximate answer rather than using the very slow one to get an exact one.

> If two functions f(n) and g(n) are being executed in a sequence, then we use the law of addition to figure out their resultant complexity.
> ```python
> O(f(n)) + O(g(n)) = O(f(n) + g(n))
>
> # For example, the code below has a complexity of
> #     O(3n^2 + 1) + O(3n) = O(3n^2 + 3n + 1)
> # which will be simplified to O(n^2).
> for j in range(n * n):
>     some_var += j
> for i in range(n):
>     some_var += i
> ```
>
> If the two functions are nested, however, then we use the law of multiplication:
>
> ```python
> O(f(n)) * O(g(n)) = O(f(n) * g(n))
>
> # For example, the code below has a complexity of
> #     O(n) * O(3n^2 + 1) = O(3n^3 + n)
> # which will be simplified to O(n^2).
> for i in range(n):
>     for j in range(n * n):
>         some_var = i + j
> ```
>
> Notice how we are dropping the multiplicative and additive constants, and are focusing only on the **dominant term**, i.e., the term that grows the fastest with the size of the input.

# Things I got wrong
```python
# The code given below, in the best case, takes 2 steps to execute, not 3! This is because if the list L1 is empty, then the line 'for obj in L1' doesn't perform any assignments! (Weird, I know)
def some_func(L1):
    copy = []
    for obj in L1:
        copy.append(obj)
    return copy

# You can see how vague the definition of a 'step' can be. This is why we prefer the Big Oh notation over the number of operations: it preserves the analysis of how the complexity of the program grows with the size of the input, while simultaneously simplifying the process of the analysis in question.
```
