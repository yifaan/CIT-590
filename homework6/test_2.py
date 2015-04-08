b = 0
while b != 1:
    try:
        a = input('a number')
        if a > 10:
            raise ValueError('abc')

    except SyntaxError:
        pass
