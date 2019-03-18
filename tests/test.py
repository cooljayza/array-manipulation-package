from array import myFunction

def test_sum_array():
    """
    make sure sum_array works correctly
    """

    assert myFunction.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'

def test_fibonacci():
    """
    make sure fibonacci works correctly
    """
    assert myFunction.fibonacci(5) == 3, 'incorrect'
    assert myFunction.fibonacci(7) == 8, 'incorrect'
    assert myFunction.ibonacci(9) == 21, 'incorrect'

def test_factorial():
    """
    make sure factorial works correctly
    """
    assert myFunction.factorial(3) == 6, 'incorrect'
    assert myFunction.factorial(5) == 120, 'incorrect'
    assert myFunction.factorial(2) == 2, 'incorrect'

def test_quick_sort():
    """
    make sure quick sort works correctly
    """
    assert myFunction.quick_sort([8, 3, 2, 7, 4]) == [2,3,4,7,8], 'incorrect'

def test_merge_sort():
    """
    make sure merge sort works correctly
    """
    assert myFunction.merge_sort([8, 3, 2, 7, 4]) == [2,3,4,7,8], 'incorrect'

def test_bubble_sort():
    """
    make sure bubble sort works correctly
    """
    assert myFunction.bubble_sort([8, 3, 2, 7, 4]) == [2,3,4,7,8], 'incorrect'
