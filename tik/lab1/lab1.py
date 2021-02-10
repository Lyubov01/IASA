
import collections
import math
import numpy as np
import pandas as pd


class DataAmount:

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, "rb") as f:
            self.data = f.read()

    def estimate_shannon_entropy(self):
        n = len(self.data)
        bases = collections.Counter([symbol for symbol in self.data])
        shannon_entropy_value = 0
        for base in bases:
            n_i = bases[base]
            p_i = n_i / float(n)
            entropy_i = p_i * (math.log(p_i, 2))
            shannon_entropy_value += entropy_i
        return shannon_entropy_value * -1

    def max_entropy(self):
        d = [char for char in self.data]

        return math.log(len(np.unique(d)),2)

    def absolute_redunduncy(self):
        return self.max_entropy()-self.estimate_shannon_entropy()

    def relative_reduncy(self):
        return self.absolute_redunduncy() / self.max_entropy()

    def __len__(self):
        return len(self.data)

    def amount_of_information(self):
        return self.estimate_shannon_entropy()*len(self.data)


def generate_name_of_files():
    files = []
    lang = ["ENG", "RUS", "UKR"]
    for i in range(1, 9):
        for ex in lang:
            name = "test_files/" + "TEST" + str(i) + "_" + ex + ".txt"
            files.append(name)

    return files


def main():

    files = generate_name_of_files()
    s = ""
    len_arr = []
    entropy_array = []

    for file in files:
        f = DataAmount(file)
        if "ENG" in file:
            s += "Length "+str(len(f))
            len_arr.append(s)
            s = ""
        entropy_array.append(round(f.estimate_shannon_entropy(),6))

    entropy_array = [entropy_array[i:i+3] for i in range(0,len(entropy_array), 3)]

    d = zip(len_arr, entropy_array)
    data = dict(d)

    df = pd.DataFrame(data, index=['ENG',
                                   'RUS',
                                   'UKR'
                                        ])
    print(df)


if __name__ == '__main__':
    main()