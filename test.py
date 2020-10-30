i = 1
liste = []
for num in range(10):
    # liste.append(i)
    liste.append([i,'essai ' + str(i)])
    i += 1

# print(liste)

for bla in liste:
    print(bla[0], ' ', bla[1])