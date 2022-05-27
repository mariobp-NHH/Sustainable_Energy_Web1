import numpy as np
def quantities(ah, al, ah_go, al_go, T, cases):
    # Branch 1 spot
    q11 = ah + T
    q12 = al - T
    # Branch 2 spot
    q21 = ah - T
    q22 = al + T
    if cases == 'case1':
        # Banch 1 spot, branch 1 go1
        q1go11 = min(al_go + ah_go, q11)
        q1go12 = max(0, al_go + ah_go - q11)
        # Banch 1 spot, branch 2 go1
        q1go21 = max(0, al_go + ah_go - q12)
        q1go22 = min(al_go + ah_go, q12)
        # Banch 2 spot, branch 1 go2
        q2go11 = min(al_go + ah_go, q21)
        q2go12 = max(0, al_go + ah_go - q21)
        # Banch 2 spot, branch 2 go2
        q2go21 = max(0, al_go + ah_go - q22)
        q2go22 = min(al_go + ah_go, q22)
    elif cases == 'case2':
        # Banch 1 spot, branch 1 go1
        q1go11 = min(al_go + ah_go, ah_go + T, q11)
        q1go12 = max(0, al_go - T, al_go + ah_go - q11)
        # Banch 1 spot, branch 2 go1
        q1go21 = max(0, ah_go - T, al_go + ah_go - q12)
        q1go22 = min(al_go + ah_go, al_go + T, q12)

        # Banch 2 spot, branch 1 go2
        q2go11 = min(al_go + ah_go, ah_go + T, q21)
        q2go12 = max(0, al_go - T, al_go + ah_go - q21)
        # Banch 2 spot, branch 2 go2
        q2go21 = max(0, ah_go - T, al_go + ah_go - q22)
        q2go22 = min(al_go + ah_go, al_go + T, q22)
    # else:

    return q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22

def bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch):
    # Branch 1: p1s<=p2s:
    if branch == 1:
        b1 = pmaxgo * q1go21 / q1go11
        b2 = pmaxgo * q1go12 / q1go22
        b = max(b1, b2)
    # Branch 2: p1s>p2s:
    else:
        b1 = pmaxgo * q2go21 / q2go11
        b2 = pmaxgo * q2go12 / q2go22
        b = max(b1, b2)

    return b1, b2, b

def CDF_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, N, bgo, pmaxgo, branch):
    eps = (pmaxgo - bgo) / N
    p = np.zeros(N + 1)
    F_h = np.zeros(N + 1)
    F_l = np.zeros(N + 1)

    if branch == 1:
        for i in range(N + 1):
            p[i] = bgo + eps * (i)
            F_h[i] = ((p[i] - bgo) * q1go22) / (p[i] * (q1go22 - q1go12))
            F_l[i] = ((p[i] - bgo) * q1go11) / (p[i] * (q1go11 - q1go21))
    else:
        for i in range(N + 1):
            p[i] = bgo + eps * (i)
            F_h[i] = ((p[i] - bgo) * q2go22) / (p[i] * (q2go22 - q2go12))
            F_l[i] = ((p[i] - bgo) * q2go11) / (p[i] * (q2go11 - q2go21))
    F_h[N] = 1
    F_l[N] = 1
    return F_h, F_l, p

def bounds_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, b1go, b2go, pmaxs):
    b1 = ((pmaxs * q21) + (b2go * q2go11) - (b1go * q1go11)) / q11
    b2 = ((pmaxs * q12) + (b1go * q1go22) - (b2go * q2go22)) / q22
    b = max(b1, b2)
    return b1, b2, b

def CDF_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, N, bs, b1go, b2go, pmaxs):
    eps = (pmaxs - bs) / N
    p = np.zeros(N + 1)
    F_h = np.zeros(N + 1)
    F_l = np.zeros(N + 1)
    for i in range(N + 1):
        p[i] = bs + eps * (i)
        F_h[i] = ((p[i] - bs) * q22) / ((p[i] * (q22 - q12)) + (b2go * q2go22 - b1go * q1go22))
        F_l[i] = ((p[i] - bs) * q11) / ((p[i] * (q11 - q21)) + (b1go * q1go11 - b2go * q2go11))

    F_h[N] = 1
    F_l[N] = 1
    return F_h, F_l, p

def exp_price(F_h, F_l, p):
    F_h_diff = np.diff(F_h)
    F_l_diff = np.diff(F_l)

    E_h = sum(p[1:] * F_h_diff)
    E_l = sum(p[1:] * F_l_diff)

    return E_h, E_l

def plot_exp_price(ah, al, ah_go, al_go, T, pmaxgo, pmaxs, N, cases, branch):
    a2_lst = np.linspace(7, 8, 100)

    E_h_lst = []
    E_l_lst = []

    if branch == 1 or branch == 2:
        for a2 in a2_lst:
            q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22 = quantities(ah, a2,
                                                                                                            ah_go,
                                                                                                            al_go,
                                                                                                            T,
                                                                                                            cases)
            b1, b2, b = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo, branch)
            F_h, F_l, p = CDF_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, N, b, pmaxgo,
                                 branch)
            E_h, E_l = exp_price(F_h, F_l, p)
            E_h_lst.append(E_h)
            E_l_lst.append(E_l)
    elif branch == 0:
        for a2 in a2_lst:
            q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22 = quantities(ah, a2,
                                                                                                            ah_go,
                                                                                                            al_go,
                                                                                                            T,
                                                                                                            cases)
            b11go, b12go, b1go = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo,
                                           branch=1)
            b21go, b22go, b2go = bounds_GO(q1go11, q1go12, q1go21, q1go22, q2go11, q2go12, q2go21, q2go22, pmaxgo,
                                           branch=2)
            b1sgo, b2sgo, bsgo = bounds_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, b1go, b2go, pmaxs)
            F1sgo, F2sgo, psgo = CDF_spot(q11, q12, q21, q22, q1go11, q1go22, q2go11, q2go22, N, bsgo, b1go, b2go,
                                          pmaxs)
            E_h, E_l = exp_price(F1sgo, F2sgo, psgo)
            E_h_lst.append(E_h)
            E_l_lst.append(E_l)
    else:
        for a2 in a2_lst:
            q11, q12, q1go11, q1go12, q1go21, q1go22, q21, q22, q2go11, q2go12, q2go21, q2go22 = quantities(ah, a2,
                                                                                                            ah_go,
                                                                                                            al_go,
                                                                                                            T,
                                                                                                            cases)
            b1s, b2s, bs = bounds_spot(q11, q12, q21, q22, 0, 0, 0, 0, 0, 0, pmaxs)
            F1s, F2s, ps = CDF_spot(q11, q12, q21, q22, 0, 0, 0, 0, N, bs, 0, 0, pmaxs)
            E_h, E_l = exp_price(F1s, F2s, ps)
            E_h_lst.append(E_h)
            E_l_lst.append(E_l)

    return E_h_lst, E_l_lst, a2_lst
