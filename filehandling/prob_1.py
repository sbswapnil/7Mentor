files = ['file1.txt', 'file2.txt', 'file3.txt']

for file in files:

    total = 0
    list_ = []

    try:

        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                list_ += line[:-1].split(' ')

        # print(list_)

        for value in list_:
            if value.isnumeric():
                total += int(value)

        print(f'Addition of Numeric values in file {file}', total)

    except FileNotFoundError as e:
        print(e)
