from mypackage import myModule

def test_top_n ():
    """
    make top n work correctly
    """
assert myModule.top_n([8,3,2,7,4], 3) == [8,7,4], 'incorrect'
assert myModule.top_n([9,3,4,5,8,2,4] 3) == [9,8,5], 'incorrect'
assert myModule.top_n([1,2,3,4,5,67,], 3) == [67, 5, 4], 'incorrect'