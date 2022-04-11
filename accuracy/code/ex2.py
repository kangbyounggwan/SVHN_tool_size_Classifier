while True :
    a = int(input('세로사이즈'))
    b = int(input('가로사이즈'))
    height = int(input('h'))
    left = int(input('l'))
    top = int(input('t'))
    width = int(input('w'))

    col_ratio = 64 / a
    row_ratio = 128 / b

    re_left = left * row_ratio
    re_width =width * row_ratio
    re_height = height * col_ratio
    re_top = top * col_ratio

    print(re_height, re_left, re_top, re_width)