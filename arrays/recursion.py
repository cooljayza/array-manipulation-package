def sum_array(array):
    """Return the sum of n numeric items in an array.

    Args:
        array: list or array-like object containing numerical values.

    Returns:
        float/int: sum of all the elements in the array,integer value if the
        numbers are integers otherwise float.

    Examples:
        >>> sum_array([8, 3, 2, 7, 4])
        24
    """
    if len(array) == 0:
        return 0
    else:
        term = array[-1]
        array.pop()
        return  term + sum_array(array)

def fibonacci(n):
    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
     """
     Calculate factorial of a given number n

     Args:
         n (int): nth factorial

     Returns:
         int: the product of n*(n-1)...*1, n!


     Examples:
         >>> factorial(3)
         6
         >> factorial(5)
         120
         >> factorial(2)
         2
     """
     if n <= 0:
         return 1
     else:
          return n * factorial(n-1)


def reverse(word):
    """
    Return the input word in reverse

    Args:
        word (object): word as a string

    Returns:
        object: word in reverse order


    Examples:
        >>> reverse("Jacob")
        "bocaJ"
        >> reverse("Khoza")
        "azohK"
    """
    if len(word) <= 0:
        return ""
    else:
        return word[-1] + reverse(word[:-1])
