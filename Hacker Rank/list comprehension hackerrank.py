# x, y, z, n = int(input()), int(input()), int(input()), int(input())
# print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1)
#       for c in range(0, z+1) if a + b + c != n])

# x = int(input())
# y = int(input())
# z = int(input())
# k = int(input())
# p = []
# for i in range(0, x+1):
#     for l in range(0, y+1):
#         for j in range(0, z+1):
#             p.append([i, l, j])

# print(p)

# for i in p:
#     d = 0
#     for q in i:
#         d = d + q
#     if d == k:
#         p.remove(i)
# print(p)