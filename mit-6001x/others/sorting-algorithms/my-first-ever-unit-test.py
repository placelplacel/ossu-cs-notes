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


TEST_CASES = [([], []), ([2], [2]), ([6, 4, 3, 2, 1], [1, 2, 3, 4, 6])]
def test_selection_sort():
    print("Testing selection_sort():", end=" ")
    for test_case in TEST_CASES:
        test_input = test_case[0][:]
        selection_sort(test_input)
        if test_input != test_case[1]:
            print("FAILED")
            print("- Input:", test_case[0])
            print("- Expected Output:", test_case[1])
            print("- Actual Output:", test_input)
            return
    print("SUCCESS")


if __name__ == "__main__":
    test_selection_sort()