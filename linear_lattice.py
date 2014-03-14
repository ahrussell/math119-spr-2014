import random as r

class LinearLattice(VectorSpace):

    def __init__(self, f, dim):
        return VectorSpace(GF(f),dim)

    def random_family(self, k, size):
        subspaces = list(self.subspaces(k))

        xs = [for i in range(size): r.randint(0,len(subspaces))]

        return [for x in xs: subspaces[x]]

    def is3clust(self,fam):
    	k = fam[0].dimension()
    	intersect = fam[0].intersection(fam[1].intersection(fam[2]))
    	vsum = sum(fam)

    	return intersection.dimension() == 0 and vsum.dimension() <= 2*k

