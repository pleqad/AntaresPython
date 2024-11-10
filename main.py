def name_x_y(x, y):
    return [x[i] + y[i] for i in range(len(x))]


print(name_x_y([1, 2, 3], [1, 2, 3]))