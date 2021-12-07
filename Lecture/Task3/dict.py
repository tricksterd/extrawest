"""Can't create dict with duplicates keys. It's overwrites value for this key."""

test = 2 - 1

d = {
    int('1'): '1',
    test: '2 - 1',
    1: '3'
}
# d[1] = 3, 2, 1

print(d)