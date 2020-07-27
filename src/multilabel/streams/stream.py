from functools import reduce


class Stream:
    def __init__(self, seq):
        self.seq = seq

    def map(self, lambda_):
        seq = list(map(lambda_, self.seq))

        return Stream(seq)

    def filter(self, lambda_):
        seq = list(filter(lambda_, self.seq))

        return Stream(seq)

    def as_list(self):
        return self.seq

    def first(self):
        return self.seq[0]

    def reduce(self, lambda_, init_val):
        return reduce(lambda_, self.seq, init_val)

    def foreach(self, lambda_):
        for index in range(0, len(self.seq)):
            lambda_(self.seq[index], index)

    def append_list(self, seq):
        return Stream(self.seq + seq)

    def append_elem(self, elem):
        return Stream(self.seq + [elem])