# input()
import itertools as it
"""
WORK IN PROGRESS (solution not quite complete)

arrangement
ways of arranging 2 and 3 that sum to w
how many permutations of 2's and 3's

"""
#X = input()
#w,h,m = [int(x) for x in X.split()]
w,h,m = [9, 3, 1000]

#print("*** w: ", w)#,h,m)

#max number of blocks possible: w / 2
#arrangements = it.permutations('23', w//2)

#print("A | arr list: ", list(arrangements))

arr_comp = [list(it.permutations('23',i)) for i in range(1, w//2)]
#print("B | arr comp: ", arr_comp)

perm_list = []
for i in range(w//2+1):
    for j in range(w//3+1):
        if 2 * i + 3 * j == w:
            perm_list.append([str(2)*i + str(3)*j])

print("C | permperm_list: ", perm_list)
print("  --> len: ", len(perm_list))

print("  --> [0][0]3", set(list(it.permutations(perm_list[0][0],3))))
print("  --> [1][0]4", set(list(it.permutations(perm_list[1][0],4))))

the_set = set([()])

# check ranges
# i in range(w//2+1)  is 0 to w//2 inclusive
# if w = 9, w//2 is 4, so i is 0 to 5
# if i = 0, permlist[0][0], which is ['333']
# now permute that over range (len(perm_list))
# which is 0 to 2, exclusive.
# permutation is ... I have my indices backwards.
# does permuting [0] do something special?
for permute_times in range(1, w//2+1):
    for group in perm_list:
        if permute_times <= len(group[0]) and (permute_times > 0):
            #print("group_idx, permute_times: ", group, permute_times)
            _set = set(it.permutations(group[0], permute_times))
            #print(_set)
            # union does not work inplace
            the_set = the_set.union(_set)



#print("\nthe_set: ", the_set)

set_list = list(the_set)


#print("\nset_list: ", set_list)
set_list = [list(element) for element in set_list]
#print("\nset_list: ", set_list)

for i in range(len(set_list)):
    for j in range(len(set_list[i])):
        set_list[i][j] = int(set_list[i][j])
#print("\nset_list: ", set_list)
#sum_list = [sum(set_list[i]) for i in range(len(set_list))]
#print("\nsum_list: ", sum_list)

# get only the permutations where the length exactly matches the length
# of the wall
filtered_set_list = [element for element in set_list if sum(element) == w]
print('\nfiltered set list: ', filtered_set_list)

# crack locations
# don't count 0 or w (inclusive)
crack_locations = []

def mini_sum(X):
    Y = []
    #print(X[0])
    for i in range(0,len(X)-1): #skip the last one because it will always be w and screw up the outcome
        #print(i, X[i], Y)
        if i == 0:
            Y.append(X[i])
        else:
            Y.append(Y[i-1] + X[i])
    return Y

mini_sum([2,2,3,2])

crack_locations = sorted([mini_sum(element) for element in filtered_set_list])
print("crack_locations: ", crack_locations)

################## NOW we have all possible brick combinations for any
# single row and the crack locations assocaited therewith
# NEXT need to compare locations

def have_overlapping_cracks(a,b):
    return (len(set(a) & set(b)) > 0)

print(have_overlapping_cracks(crack_locations[0], crack_locations[1]))
print(have_overlapping_cracks(crack_locations[0], crack_locations[3]))
"""
prior_cracks = []
current_cracks = []
wall_cracks = []
rows_ok = 0


            #rows_ok += 1
    wall_cracks.append(current_cracks)
    print(wall_cracks)
"""
