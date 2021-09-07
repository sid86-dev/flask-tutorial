def read_data():
    f = open('todo.txt', 'r')

    data = f.read()

    f.close()

    return data

