def inclusion(n,q,i,j):
    V = VectorSpace(GF(q),n)
    row = 0

    i_subs = list(V.subspaces(i))
    j_subs = list(V.subspaces(j))
    
    M = Matrix(ZZ,len(i_subs),len(j_subs),0)

    for U in i_subs:
        column = 0

        for W in i_subs:
            if U.is_submodule(W):
                M[row,column] = 1
            column += 1
        row += 1

    return M
