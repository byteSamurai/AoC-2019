import collections

nos = []

for no in range(153517, 630395):
    str_no = str(no)
    if not "".join(sorted(list(str_no))) == str_no:
        continue

    if 2 not in collections.Counter(str_no).values():
        continue

    nos.append(no)

print(len(nos))

# 1172 ?
