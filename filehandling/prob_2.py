# count avg of marks and topper of the class.

def topper(d):
    value = 0
    key = ''
    for k, v in d.items():
        if v > value:
            value = v
            key = k
    return key, value


files = ['data.txt']

for file in files:

    avg = 0
    total = 0
    list_ = []
    d = dict()

    try:

        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                list_ += line[:-1].split(' ')

        for value in range(1, len(list_), 3):
            d[list_[value]] = float(list_[value + 1])
        # print(list_, d)

        print(f'Avarage Marks of the Students in file {file}', sum(list(map(float, d.values()))) / len(d.values()))

        key, value = topper(d)
        # filter(topper, d.items())

        print(f'Topper of the Class in file {file} is {key} with {value} marks.')


    except FileNotFoundError as e:
        print(e)
