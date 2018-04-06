# CMPS 201 Fall 17 HW5 #1

g_comp = 0


def extrema(A, p, r):
    if p == r:
        return A[p], A[p]
    elif p == r - 1:
        return order_pair(A[p], A[r])
    else:
        q = int((p + r) / 2)
        mi1, ma1 = extrema(A, p, q)
        mi2, ma2 = extrema(A, q + 1, r)
        return min(mi1, mi2), max(ma1, ma2)


def extrema2(A, p, r):
    if p == r:
        return A[p], A[p]
    else:
        q = int((p + r) / 2)
        mi1, ma1 = extrema2(A, p, q)
        mi2, ma2 = extrema2(A, q + 1, r)
        return min(mi1, mi2), max(ma1, ma2)


def min(x1, x2):
    global g_comp
    g_comp += 1
    if x1 < x2:
        return x1
    else:
        return x2


def max(x1,x2):
    global g_comp
    g_comp += 1
    if x1 > x2:
        return x1
    else:
        return x2


def order_pair(x1, x2):
    global g_comp
    g_comp += 1
    if x1 > x2:
        return x2, x1
    else:
        return x1, x2


if __name__ == "__main__":
    A = [7, 34, 6, 23, 67, 8, 0, 12, 45]
    print(extrema(A, 0, len(A) - 1))
    print(len(A))
    print(g_comp)