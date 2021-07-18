from iteration_utilities import deepflatten

multi_depth_list = [[0,1], [[2]], [3,4]]

flatten_list = list(deepflatten(multi_depth_list))

print(flatten_list)

l =  [[0,1], [[2]], [3,4]]
flatten_list = []
for subl in l:
    for item in subl:
        flatten_list.append(item)
print(flatten_list)