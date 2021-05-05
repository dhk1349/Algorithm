def swap(lst, idx1, idx2):
    tmp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = tmp


def bubble_sort(lst):
    for end in range(len(lst)-1):
        for idx in range(len(lst)-1-end):
            if lst[idx] > lst[idx+1]:
                swap(lst, idx, idx+1)
    return lst


def insertion_sort(l):
    for bound in range(1, len(l)):
        cursor = l[bound] # assign key var to cursor
        for idx, elem in enumerate(l[:bound]):
            if elem > cursor: # from idx to bound, insert cursor value in the front and push back the elements.
                for i in range(bound, idx, -1):
                    l[i] = l[i-1]
                l[idx] = cursor
                break

    return l


def merge_sort(l):
    center = int(len(l)//2)

    if len(l) > 1:
        left = merge_sort(l[:center])
        right = merge_sort(l[center:])
    else:  # if l can't be divided
        return l

    #left and right are sorted
    left_cur = 0
    right_cur = 0
    cur = 0
    # print(f"merging...\n {left}\n{right}")
    while right_cur != len(right) and left_cur != len(left):
        if right[right_cur] < left[left_cur]:
            l[cur] = right[right_cur]
            right_cur += 1
        else:
            l[cur] = left[left_cur]
            left_cur += 1
        cur += 1

    if right_cur == len(right):
        for idx in range(left_cur, len(left)):
            l[cur] = left[idx]
            cur += 1

    if left_cur == len(left):
        for idx in range(right_cur, len(right)):
            l[cur] = right[idx]
            cur += 1
    # print(f"{l}\n")
    return l


def quick_sort(l):
    if len(l) <= 1:
        return l
    # print(f"To sort: {l}")
    pivot = l[0]
    ### partition ###
    lo_idx = 1
    hi_idx = len(l)-1

    lo_bool = True
    hi_bool = True
    while True:
        # print(f"{lo_idx}, {hi_idx}")

        if hi_idx < lo_idx:  # when both idxs cross each other.
            swap(l, hi_idx, 0)
            pivot_idx = hi_idx
            break

        if l[lo_idx] <= pivot:
            lo_idx += 1
        else:
            lo_bool = False

        if l[hi_idx] > pivot:
            hi_idx -= 1
        else:
            hi_bool = False

        if not(lo_bool or hi_bool): #if both idx don't move anymore,
            swap(l, lo_idx, hi_idx)
            lo_bool = True
            hi_bool = True


    # print(f"Smaller than {pivot}: {l[:pivot_idx]}\nLarger than {pivot}: {l[pivot_idx+1:]}\n{l}\n\n")

    ### partition end ###


    l[:pivot_idx] = quick_sort(l[:pivot_idx])
    l[pivot_idx+1:] = quick_sort(l[pivot_idx+1:])

    return l


def radix_sort(l, d):
    # Stable sort
    for r in range(0, d):
        c = [0] * 10
        m = d - r - 1  # m = d - r -1
        for i in l:
            key = int(str(i).zfill(d)[m])
            c[key] += 1
        for j in range(1, 10):
            c[j] = c[j-1] + c[j]
        n = len(l)
        t = [0] * n
        for i in range(n-1, -1, -1):
            key = int(str(l[i]).zfill(d)[m])
            t[c[key]-1] = l[i]
            c[key] = c[key]-1
        for i in range(0, n):
            l[i] = t[i]
    return l


