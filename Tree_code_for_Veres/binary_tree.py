class Tree:

    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        return True


    def delete(self,value):
        pass

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        return self._insert(self.root, value)


    def max_value(self):
        pass

    def min_value(self):
        pass

    def _insert(self, current_node, value):

        if (value > current_node.value):
            #add to the right
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
            return self._insert(current_node.right, value)

        else:
            # add to the left
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                return
            return self._insert(current_node.left, value)

    def _search(self, node_to_check, value):
        if (node_to_check is None) or (node_to_check.value ==value):
            return node_to_check

        if value > node_to_check.value:
            # go right
            return self._search(node_to_check.right, value)
        else:
            # go left
            return self._search(node_to_check.left, value)

    def insert_with_search(self, current_node, value):
        found_node = self._search(current_node, value)

    def print_the_tree(self):
        self._print_the_tree(self.root)

    def _print_the_tree(self, current_node):
        print(current_node.value)
        if current_node.right is not None:
            self._print_the_tree(current_node.right)
        if current_node.left is not None:
            self._print_the_tree(current_node.left)


class Node:

    def __init__(self, value, parent = None):
        self.right = None
        self.left = None
        self.parent = None
        self.value = value

tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(8)
tree.insert(6)
print (tree.search(6))
print (tree.search(7))
print (tree.search(2))
print (tree.search(5))
tree.print_the_tree()