#how to reverse a string ie: poh -> hop
# one way is in-place


def check(pal, first, last):
    #base cases
    if first == last:
        return

    if last == first + 1:
        return

    if pal[first]==pal[last]:
        first = first+1
        last = last-1
        check(pal, first, last)
    else:
        flag=False