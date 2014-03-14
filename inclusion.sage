def inclusion(n,q,i,j):
    V = VectorSpace(GF(q),n)
    row = 0
    M = Matrix(ZZ,len(list(V.subspaces(i))),len(list(V.subspaces(j))),0)

    for U in V.subspaces(i):
        column = 0

        for W in V.subspaces(j):
            if U.is_submodule(W):
                M[row,column] = 1
            column += 1
        row += 1

    return M
