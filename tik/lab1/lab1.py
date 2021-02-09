import collections
import math


def estimate_shannon_entropy(filename):
    f = open(filename, 'r')
    data = f.read()
    print(len(data))

    total = len(data)

    bases = collections.Counter([symbol for symbol in data])
    print(bases)
    shannon_entropy_value = 0
    for base in bases:
        n_i = bases[base]
        p_i = n_i / float(total)
        entropy_i = p_i * (math.log(p_i, 2))
        shannon_entropy_value += entropy_i

    print(f.read())

    return shannon_entropy_value * -1


if __name__ == '__main__':
    n = 'test.txt'
    f = open(n)

    print(estimate_shannon_entropy(n))
    print()