import random as r

def LinearLattice(f, dim):
    return VectorSpace(GF(f),dim)

def random_family(subspaces, size):
    xs = []

    while len(xs) < size:
        x = r.randint(0,len(subspaces)-1)
       
        if x not in xs:
            xs.append(x)

    return [subspaces[x] for x in xs]

def is3clust(fam):
    k = fam[0].dimension()
    intersect = fam[0].intersection(fam[1].intersection(fam[2]))
    vsum = sum(fam)

    return intersect.dimension() == 0 and vsum.dimension() <= 2*k

def detect_3_cluster(fam):
    m = len(fam)

    for i in range(m):
        for j in range(i+1,m):
            for k in range(j+1,m):
                if is3clust([fam[i],fam[j],fam[k]]):
                    return True, [fam[i],fam[j],fam[k]]
    
    return False, fam


#######################
# code for computing results
#######################

# L = LinearLattice(2,6)
# S = list(L.subspaces(3))
# 
# results = []
# 
# for i in range(50):
#     F = random_family(S,5)
#     results.append(detect_3_cluster(F))
# 
# count = 0
# for i in results:
#     if i[0] == True:
#         count += 1
# 
# print 100 * float(count) / len(results), "%"

