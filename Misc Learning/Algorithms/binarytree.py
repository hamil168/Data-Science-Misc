#  bINARY TREE RULES
# -hIERARCHICAL

# Root: topost node
# Parent: Node that has nodes below it
# Child: Node beneath the Parent
# Subtree: the tree below a child
# Leave: node with mo children
# Height: max nodes from root to leaf

# FULL tree: every node has either 0 or 2 children
# COMPLETE tree: all levels are completely filled (except last) and
#    last level all nodes are far to the left
# PERFECT tree: all nodes except leaves have 2 children andd
#     all leaves are same Height

# Efficient insertion and searching
# Flexible, subtrees can be moved around


##########################################
########### BINARY SEARCH TREE
##########################################

# Key of each node is greater or equal to any key in left subtree
# and less than or equal to any stored in right subtree
# main operations are Search, Insert, and Delete

# SEARCH: Input target Key
# Check root, if equal, return; if greater or equal to root, right; if less, left

# STEP 1: CREATE A NODE
class node:
    def __init__(self, key):
        self.key = key
        self.address = -key
        self.right =  None
        self.left = None


# STEP 2: Create tree:
base = node(5)

base.right = node(8)
base.right.right = node(9)
base.right.right.right = node(10)

base.right.left = node(7)
base.right.left.left = node(6)

base.left  = node(3)
base.left.right = node(4)
base.left.left = node(1)
base.left.left.right = node(2)
base.left.left.left = node(0)

print(base.key)


# SEARCH
# Names correspond to positive node numbers
# Sounds for names are their negative

# STEP 3: CREATE A "LOOKUP"
animal_dict = {"Cow": 1, -1: "Moo", "Dog": 2, -2: "Woof", "Cat": 3, -3: "Meow"}

# STEP 4: USER INPUT
animal = input("Pick your animal: ")

# STEP 5 Initialize and search
current_node = base

animal_sound = -999
animal_key = animal_dict[animal]

# print("animal_key_test: " + str(animal_key))
# print("animaal_sound_test " + str(animal_dict[-1 * animal_key]))
# print(str(current_node.key == animal_key))
#print(animal_dict[current_node.address])

for level in range(1,5,1):

    # print("current node key test: " + str(current_node.key))
    # print("current node address test: " + str(current_node.address))

    if current_node.key == animal_key:
            animal_sound = animal_dict[current_node.address]
            break

    elif current_node.key < animal_key:
        current_node = current_node.right

    elif current_node.key > animal_key:
        current_node = current_node.left

# RESULT
print("A/An " + animal + " says " + str(animal_sound))



























#base.left = node(3)
