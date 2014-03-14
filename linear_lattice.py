import random as r

class LinearLattice(VectorSpace):

    def __init__(self, f, dim):
        return VectorSpace(GF(f),dim)

    def random_family(self, k, size):
        subspaces = list(self.subspaces(k))

        xs = [for i in range(size): r.randint(0,len(subspaces))]

        return [for x in xs: subspaces[x]]
