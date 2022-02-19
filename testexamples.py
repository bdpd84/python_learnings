
foo = (1, 2, 3)
bar = (4, 5, 6)
for f, b in zip(foo, bar):
    print(f, b)

input = [[1,2],[3,4],[5,6],[7,8]]
output = [i[0] for i in input], [i[1] for i in input]
print (output)