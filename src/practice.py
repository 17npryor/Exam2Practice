'''
def main():
    a = alpha()


    print()
    b = beta()

    print()
    g = gamma()

    print()
    print("main!", a, b, g)


def alpha():
    print("Alpha!")


    return 7


def beta():
    print("Beta!")


    return 15 + alpha()


def gamma():
    print(alpha(), beta(), "Gamma!")


    return alpha() + beta() + alpha()

main()
'''

'''
    class TwoPoints(object):
    def __init__(self, p1, p2):
        self.p1 = Point(p1.x, p1.y)

        self.p2 = Point(p2.x, p2.y)
        self.nswaps = 0

    def clone(self):
        p1 = Point(self.p1.x, self.p1.y)

        p2 = Point(self.p2.x, self.p2.y)
        return TwoPoints(p1, p2)

    def swap(self):
        temp = self.p1

        self.p1 = self.p2
        self.p2 = temp
        self.nswaps = self.nswaps + 1

    def number_of_swaps(self):
        return self.nswaps

    p1 = Point(10, 20)
    p2 = Point(88, 44)
    tp = TwoPoints(p1, p2)

    # Testing construction (__init__):
    print('Expected:', p1, p2)
    print('Actual:  ', tp.p1, tp.p2)

    # Testing clone:
    tp2 = tp.clone()

    # Testing swap:
    tp.swap()
    print('Expected:', p2, p1)
    print('Actual:  ', tp.p1, tp.p2)

    tp.swap()
    print('Expected:', p1, p2)
    print('Actual:  ', tp.p1, tp.p2)

    # Testing number_of_swaps:
    print('Expected:', 2)
    print('Actual:  ',tp.number_of_swaps())
    
    '''

def foo(seq):
    total = 0
    seq = [3]
    for k in range(1, len(seq), 2):
        total = total + seq[k]
    return total
