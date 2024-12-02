# Searching and Sorting Algorithms
## Bogo Sort
```
- Check if the list is sorted
    - If it is, great!
    - If it isn't, keep going buddy.
- Randomly order the elements the list.
- Repeat.
```
**Best Case Complexity:** `O(n)` as we only have to go through the list once, and once again to check if it's sorted.

**Worst Case Complexity:** `O(?)` as there is no guarantee when you will get to stop.

## Bubble Sort
```
- Go through the list and on your way, check if two consecutive elements are sorted.
    - If they are, keep going.
    - If they aren't, swap them.
- If we didn't have to perform any swaps, then the list was sorted and we can stop!
    - Otherwise, repeat the algorithm.
```

```python
def merge_sort(L):
    """
    Assumes that L is a list.
    Returns a new sorted copy of L.
    """
    assert type(L) == list, "L is not a list."
    swapped_this_pass = True
    while swapped_this_pass:
        swapped_this_pass = False
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                swapped_this_pass = True
                tmp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = tmp
```

**Best Case Complexity:** `O(n)` as we would only have to go through the list once.

**Worst Case Complexity:** `O(n^2)` as there would be `n-1` iterations, and `n` passes.

## Selection Sort
```
- Start out with the start of the list (empty) as a prefix and the rest of the list as the suffix.
- Find the smallest element in the suffix, and then insert it into the end of the prefix.
- Repeat until the suffix is empty, which would mean the list has been sorted.
```

```python
def selection_sort(L):
    """
    Assumes that L is a list.
    Mutates L such that all of its elements are sorted.
    """
    assert type(L) == list, "L is not a list."
    for i in range(len(L) - 1):
        min_index = i
        j = i + 1
        while j < len(L):
            if L[j] < L[min_index]:
                min_index = j
            j += 1
        L[i], L[min_index] = L[min_index], L[i]
```

**Best Case Complexity:** `O(n^2)` as we will have to go through `n` passes, making `n-1` comparisons, then `n-2`, then `n-3`, and so on... (summing them up gives us `n(n-1)/2` comparisons in total)

**Worst Case Complexity:** Same as the best case complexity as the behavior doesn't change at all.

> Notice how this makes sure that the first elements of the list are guaranteed to be sorted after each step? This can be very helpful if we want to stop the sorting after getting a given number of sorted results!

## Merge Sort
```
Easier to read the code.
```

```python
def merge(L1, L2):
    """
    Assumes that L1 and L2 are sorted lists.
    Returns a new sorted list consisting of the elements from the two lists.
    """
    assert type(L1) == list and type(L2) == list, "Invalid arguments provided."
    result = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    while i < len(L1):
        result.append(L1[i])
        i += 1
    while j < len(L2):
        result.append(L2[j])
        j += 1
    return result


def merge_sort(L):
    """
    Assumes that L is a list.
    Returns a new sorted copy of L.
    """
    assert type(L) == list, "L is not a list."
    if L == [] or len(L) == 1:
        return L
    else:
        middle = int(len(L) // 2)
        l1 = merge_sort(L[:middle])
        l2 = merge_sort(L[middle:])
        return merge(l1, l2)
```

**Best Case Complexity:** `O(nlog(n))` as there are `O(log(n))` recursion steps and the `merge()` function has a complexity of  `O(n)`.

**Worst Case Complexity:** Same as the best case complexity as the behavior doesn't change.
