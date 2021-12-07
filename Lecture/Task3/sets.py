"""We can't create set of sets. But we can create set of frozen sets."""
s = {1, 2-1, '1'}
print(s)
s_1 = (1, 2, 3)
s_2 = {1, 1, 1}
fs_1 = frozenset(s_1)
fs_2 = frozenset(s_2)
s = {fs_1, fs_2}
print(s)