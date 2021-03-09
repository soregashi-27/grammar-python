for i in range(5):
    print(i)

# break
for i in range(5):
    if i == 3:
        break
    print(i)
# display output goes to '012'.

# continue means 'skip'
for i in range(5):
    if i == 3:
        continue
    print(i)
# display output goes to '0124'.
