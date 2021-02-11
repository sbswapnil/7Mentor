try:

    with open('file3.txt') as f:
        lines = f.readlines()
        for line in lines:
            list_ = []
            # print(line)
            list_ += line[:-1].split(' ')

            for value in list_:
                if value.isnumeric():
                    with open('copyfile3.txt', 'a+') as w:
                        w.write(value+' ')
            w = open('copyfile3.txt', 'a+')
            w.write('\n')
            w.close()

            print(list_)




except FileNotFoundError as e:
    print(e)
