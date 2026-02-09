import time
import numpy as np

#SORTING 
def bubble_sort(arr):
    """
    Performs bubble sort on a list.

    Args:
        arr (list or np.array): List or array of numerical values to sort.

    Returns:
        list: Sorted list in ascending order.
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def measure_time(func, *args):
    """
    Measures the execution time of a function.

    Args:
        func (callable): Function to execute.
        *args: Arguments to pass to the function.

    Returns:
        tuple: (result of the function, execution time in seconds)
    """
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end-start


#SEARCH
def linear_search(arr, target):
    """
    Performs linear search on a list or array.

    Args:
        arr (list or np.array): List or array to search in.
        target (any): Value to search for.

    Returns:
        int: Index of the target if found, otherwise -1.
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr, target):
    """
    Performs binary search on a sorted list or array.

    Args:
        arr (list or np.array): Sorted list or array to search in.
        target (any): Value to search for.

    Returns:
        int: Index of the target if found, otherwise -1.

    Note:
        The input array must be sorted in ascending order.
    """
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


#PANDAS SEARCH
def pandas_search(df, column, value):
    """
    Searches for rows in a Pandas DataFrame where column matches value.

    Args:
        df (pandas.DataFrame): DataFrame to search.
        column (str): Column name to check.
        value (any): Value to search for.

    Returns:
        pandas.DataFrame: Subset of rows where df[column] == value.
    """
    return df[df[column] == value]


#NUMPY SEARCH
def numpy_search(arr, value):
    """
    Searches for indices of a value in a NumPy array.

    Args:
        arr (np.array): NumPy array to search.
        value (any): Value to search for.

    Returns:
        np.array: Indices where the array equals the target value.
    """
    return np.where(arr == value)[0]