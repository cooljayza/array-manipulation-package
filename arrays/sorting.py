def bubble_sort(items):
    """
    the bubble sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    list
        list of elements in items in ascending order
    """
    array = items.copy()
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array


def quick_sort(items, index=-1):
    """
    the quick sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers
    index: int, optional
        index number at which to choose the split value
        default set to the last item in the input list

    Returns
    -------
    list
        list of elements in items in ascending order
    """
    length = len(items)

    if length <= 1:
        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large

def merge(A, B):
    """
    the merge algorithm takes in two unsorted list of numbers.
    Merges them and returns a list in ascending order.

    Parameters
    ----------
    A : list
        list of unordered numbers
    B : list
        list of unordered numbers
    Returns
    -------
    list
        list of elements in items in ascending order
    """
    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list


def merge_sort(items):
    """
    the merge sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    list
        list of elements in items in ascending order
    """
    len = len(items)
    if len == 1:
        return items

    m = int(len / 2)
    i1 = merge_sort(items[:m])
    i2 = merge_sort(items[m:])

    return merge(i1, i2)
