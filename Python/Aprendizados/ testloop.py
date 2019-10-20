def test(x, y):
    print(x)
    test(x+1, y) if x < y else print('') 

test(0, 10)