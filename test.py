# a = ['1', '1500', '2050']
# a = [int(s) for s in a]
# print(a)

# L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# L = list(zip(*L))
# print(L)

S = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
T_S = list(zip(*S))
new_arr = []
for x in T_S[::-1]:
    u = list(x)
    new_arr.append(u)
print(new_arr)



