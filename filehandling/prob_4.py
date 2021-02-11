with open('swapdata.txt') as f:
    for line in f.readlines():
        with open('copyswapdata.txt', 'a+') as w:
            w.write(line.swapcase())