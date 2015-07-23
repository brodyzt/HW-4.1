class BinarySearchTree:

    # initializes BinarySearchTree object
    def __init__(self):
        self.root = None
        self.size = 0

    # returns the # of objects in tree
    def __len__(self):
        return self.size

    # overloads __setitem__ function to add new node
    def __setitem__(self, key, value):
        self.put(key, value)

    # overloads __str__ function to return human readable version
    def __str__(self):
        return str(self.root)

    # returns the number of objects in tree
    def length(self):
        return self.size

    # checks if tree contains any data and either adds node as root or child node
    def put(self, key, data):
        if self.root:
            self._put(key, data, self.root)
        else:
            self.root = TreeNode(key, data)
        self.size += 1

    # adds data as child node
    def _put(self, key, data, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key,data,current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, data, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, data, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, data, parent=current_node)

    # prints the binary search tree
    def print(self):
        self.root.print()


class TreeNode:

    # initializes TreeNode object
    def __init__(self, key, data, left=None, right=None, parent=None):
        self.key = key
        self.data = data
        self.left_child = left
        self.right_child = right
        self.parent = parent

    # overloads str function to output human readable version
    def __str__(self):
        if self.has_both_children():
            return '{}Data:{}, {}'.format(str(self.left_child), self.data, str(self.right_child))
        elif self.has_left_child():
            return '{}Data:{}, '.format(str(self.left_child), self.data)
        elif self.has_right_child():
            return 'Data:{}, {}'.format(self.data, str(self.right_child))
        else:
            return 'Data:{}, '.format(self.data)

    # determines whether node has left
    def has_left_child(self):
        return bool(self.left_child)

    # determines whether node has right child
    def has_right_child(self):
        return bool(self.right_child)

    # determines whether node is the left child of parent node
    def is_left_child(self):
        return bool(self.parent and self.parent.left_child == self)

    # determines whether node is the right child of parent node
    def is_right_child(self):
        return bool(self.parent and self.parent.right_child == self)

    # determines whether node is root of tree
    def is_root(self):
        return not bool(self.parent)

    # determines whether node is leaf of tree
    def is_leaf(self):
        return not bool(self.right_child or self.left_child)

    # determines whether node has any children
    def has_any_children(self):
        return bool(self.left_child or self.right_child)

    # determines whether node has both children
    def has_both_children(self):
        return bool(self.left_child and self.right_child)

    # replaces node's data with inputted data
    def replace_node_data(self,key,data,left_child,right_child):
        self.key = key
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

#

    # returns the node's level in the tree
    def level(self):
        level_num = 0
        if self.parent:
            temp_parent = self.parent
        else:
            return 0
        while temp_parent:
            temp_parent = temp_parent.parent
            level_num += 1
        return level_num

    # prints the tree in a format that can express levels of nodes
    def print(self):
        if self.level() == 0:
            print(self.level() * '|\t' + 'Root:' + str(self.data))
        else:
            print(self.level() * '|\t' + ('Right:','Left:')[self.is_left_child()] + str(self.data))
        if self.has_right_child():
            self.right_child.print()
        if self.has_left_child():
            self.left_child.print()
