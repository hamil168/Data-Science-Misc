### Implement Gini Index

"""
Gini Score

QUALITY OF SPLIT measured by how mixed classes are in the 2 groups of the split

PERFECT SEPARATION scores 0

WORST SEPARATION (50/50)  scores 0.5    ... for a 2 class problem

2 groups of data, 2 rows in each group
rows in first group all belong to class 0, rows in 2nd group to class 1
==> perfect split


Gini Index = sum(i=1 to n) (proportion(i) x (1.0 - proportion(i) ) )

reweighted by relative sizes of groups, and rearranged:

           =  ( 1 - sum(i=1 t n) (proportion(i)^2) ) x current_group_size/total_samples

proportion(i) = count(class number) / count (rows)
    --- group 1 class 0 = (1 - (1 x 1 + 0 x 0)) x 2/4 = 0
    --- group 1 class 1 = 0/2 = 0
    --- group 2 class 0 = 0/2 = 0
    --- group 2 class 1 = (1 - (0 x 0 + 1 x 1)) x 2/4 = 0
    ...so gini index for perfect separation is 0

REFERENCE: "Machine Learning Algorithms from Scratch by Jason Brownlee"

"""

def gini_index(groups, classes):
    """
    gini_index(groups, classes)

    given a list of lists "groups", which are the groups corresponding to
    the training classification values as they are split by the current tree.

    and the "classes" is the number of classes, calculate gini index
    """

    # calculate 'n' for the summation
    # "sum of group"
    n_instances = float(sum([len(group) for group in groups]))

    gini = 0.0

    for group in groups:
        size = float(len(groups))

        # Divide by 0 CYA
        if size == 0:
            continue
        score = 0.0

        for class_val in classes:
            # calculates p for each class/group pair
            # last element of row, count the class val values
            # divide by total number of groups
            p = [row[-1] for row in group].count(class_val) / size

            score += p * p

        gini += (1.0 - score) * (size / n_instances)

    return gini

# Test it out
print(gini_index([ [[1, 1], [1, 0]], [[1, 1], [1, 0]] ], [0, 1]))  #0.5
print(gini_index([ [[1, 0], [1, 0]] , [[1, 1], [1, 1]] ], [0, 1] ))  #0.0
