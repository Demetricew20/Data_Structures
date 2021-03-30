

class Nodes:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def insert(root, key):
    #Check if Node exist
    if root is None:
        return Nodes(key)
    else:
        #If node already exist return node
        if root.value == key:
            return root
        #If key more than value of root insert node to right
        elif root.value < key:
            root.right = insert(root.right, key)
        # If key less than value of root insert node to left
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    #Left, Root, Right values
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def preorder(root):
    #Root, Left, Right values
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)


def search(root, key):
    #If node does not exist or equals root, return root
    if root.value is None or root.value == key:
        return root.value
    #Search right
    elif root.value < key:
        return search(root.right, key)
    #Search left
    return search(root.left, key)


r = Nodes(100)

insert(r, 110)
insert(r, 70)
insert(r, 75)
insert(r, 60)
insert(r, 40)
insert(r, 55)

search(r, 70)
inorder(r)
preorder(r)
