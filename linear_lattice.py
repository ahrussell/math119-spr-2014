import random as rand
# from inclusion import inclusion

def inclusion(n,q,i,j):
    V = VectorSpace(GF(q),n)
    row = 0

    i_subs = list(V.subspaces(i))
    j_subs = list(V.subspaces(j))
    
    M = Matrix(ZZ,len(i_subs),len(j_subs),0)

    for U in i_subs:
        column = 0

        for W in j_subs:
            if U.is_submodule(W):
                M[row,column] = 1
            column += 1
        row += 1

    return M

def LinearLattice(f, dim):
    return VectorSpace(GF(f),dim)

def random_family(subspaces, size):
    xs = []

    while len(xs) < size:
        x = rand.randint(0,len(subspaces)-1)
       
        if x not in xs:
            xs.append(x)

    return [subspaces[x] for x in xs]

# def is3clust(fam):
#     k = fam[0].dimension()
#     intersect = fam[0].intersection(fam[1].intersection(fam[2]))
#     vsum = sum(fam)
# 
#     return intersect.dimension() == 0 and vsum.dimension() <= 2*k

def detect_3_cluster(fam,inc,k):
    m = len(fam)

    for i in range(m):
        for j in range(i+1,m):
            for k in range(j+1,m):
                if is_3clust([fam[i],fam[j],fam[k]],inc,k):
                    return True    
    
    return False

def is_3clust(xs, inc, k):
    col = VectorSpace(QQ,inc.nrows()).zero_vector()

    for i in xs:
        col += inc.column(i)

    weight = sum([1 for x in col if x != 0])
    height = max(col)

    return weight < 2*k and height <= 2

def bracket(n,q):
    return (q**n - 1) / (q - 1)

def choose(n,k,q):
    num = 1
    denom = 1

    # [n]!
    for i in range(1,n+1):
        num *= bracket(i,q)

    # [k]!
    for j in range(1,k+1):
        denom *= bracket(j,q)

    # [n-k]!
    for j in range(1,(n-k)+1):
        denom *= bracket(j,q)
    
    # [n]! / ([n-k]![k]!)
    return num / denom

def cluster_density(s, size, q):
    results = []

    for n in range(3,7):
        r = []

        for k in range(2,4):
            if choose(n,k,q)-1 < size or k > n/2:
                r.append(0)
                continue

            # generate inclusion matrix
            inclusion_matrix = inclusion(n,q,1,k)
            families = []
            count = 0

            # generate s random families of size l
            for i in range(s):
                families.append(rand.sample(range(choose(n,k,q)-1), size))

            # check which families have a 3 cluster
            for f in families:
                count += 1 if detect_3_cluster(f,inclusion_matrix,k) else 0

            r.append(count)

        results.append(r)

    return results

def pretty_print(results,ns,ks):
    top_line = "--------" + "-"*len(ks) + "-" + "\n"
    lines = []

    for i in range(ns):
        l = "   "+ns[i]+"   " + "|"
        for r in results[i]:
            l += " %.2f\% |"

        lines.append(l)
    
    for l in lines:
        print lines

    ###############
    # TODO
    ###############


    


# -------------------
#  n \ k | 1 | 2 | 3 |
#    3   |


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

