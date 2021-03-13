for i in range(5):
    print(i)

for i in range(10):
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

# endless loop
# myLife = 5
# while myLife:
#     myLife -= 4
#     print(myLife)

for item in ["a", "b", "c"]:
    print(item)

idx = 0
while True:
    if idx > 5:
        break
    idx += 1
    print(idx)
