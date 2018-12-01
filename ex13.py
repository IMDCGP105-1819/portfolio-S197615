def remove_dups (L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]

runner = len(L1) + len(L2)
counter = 0

while counter < runner:
    remove_dups(L1, L2)
    counter = counter + 1

print(L1)
print(L2)
print(counter)
print(runner)