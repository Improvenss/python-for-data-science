# LINK: https://docs.python.org/3/library/functions.html#filter
# LINK: https://realpython.com/python-filter-function/
# Args:
# function (callable or None): A function to test each item or None.
# iterable (iterable): The iterable whose items will be filtered.
# Returns:
# generator: A generator yielding items for which function(item) is True.
def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    # Check iterable parameter is iterable? If not, will throw exception...
    iter(iterable)
    if function is not None and not callable(function):
        raise TypeError(f"'{type(function).__name__}' object is not callable")
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
