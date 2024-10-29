def top_n():
    """Return the top n items in an array in descending order

    Args:
    items (array): list or array like objects
    n (int): num of items to be returned

    Return:
    array: Top n items, in desc order

    Egs:
    >>> top_n([8, 9, 4, 7, 8, 2,], 3)
    [9, 8, 7]
    """
for i in range(n):
    for j in range(len(items)-1-i):
        if items[j] > items[j+1]:
            items[j], items[j+1] = items[j+1], items[j]
top_n = items[-n:]

return top_n[::-1]
