start_tower = []
transit_tower = []
finish_tower = []

def foldPyramid(n):
    temp = list(range(1, n+1))
    print(temp)
    return temp


def printTowers():
    print('first: ', start_tower, 'transit: ', transit_tower, 'finish: ', finish_tower)


def changePyramid(a, b):
    b.append(a.pop())
    printTowers()
    return a, b

def hanoyTower(n, first, last):
    if n == 1:
        print('move disk 1 from', first, 'to', last)
    else:
        temp = 6 - first - last
        hanoyTower(n - 1, first, temp)
        print("Перенести диск", n, "со стержня", first, "на стержень", last)
        hanoyTower(n - 1, temp, last)

hanoyTower(3, 1, 2)
