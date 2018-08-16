
def find(l, v):
    if not l:
        return False
    mid = len(l) // 2
    left = l[0:mid]
    right = l[mid+1:]
    if v == l[mid]:
        return True
    elif v > l[mid]:
        return find(right, v)
    else:
        return find(left, v)

l = [1,5,7,12,17,20]
r = find(l, 20)
print(r)
