import sys

sys.stdin = open("08-7.txt", "r")


def inorder_traverse(N, indexNode, value, listNode):
    if indexNode > N:
        return value

    listNode[indexNode] = inorder_traverse(
        N, indexNode * 2, value, listNode) + 1

    return inorder_traverse(N, indexNode * 2 + 1, listNode[indexNode], listNode)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    listNode = [None for _ in range(N + 1)]

    inorder_traverse(N, 1, 0, listNode)

    print(f"#{test_case} {listNode[1]} {listNode[N//2]}")

# def inorder_traverse(node, count):
#     if node == None:
#         return
#     inorder_traverse(node.left, count)
#     visit(node.data, count)
#     inorder_traverse(node.right, count)


# class BinarySearchTree(object):
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         self.root = self._insert_value(self.root, data)
#         return self.root is not None

#     def _insert_value(self, node, data):
#         if node is None:
#             node = Node(data)
#         else:
#             if data < node.data:
#                 node.left = self._insert_value(node.left, data)
#             elif data > node.data:
#                 node.right = self._insert_value(node.right, data)
#             else:
#                 print('error - 같은 값을 가질 수 없음')
#                 return None
#         return node

#     def find(self, key):
#         return self._find_value(self.root, key)

#     def _find_value(self, root, key):
#         if root is None or root.data == key:
#             return root is not None
#         elif key < root.data:
#             return self._find_value(root.left, key)
#         else:
#             return self._find_value(root.right, key)

#     def delete(self, key):
#         self.root, deleted = self._delete_value(self.root, key)
#         return deleted

#     def _delete_value(self, node, key):
#         if node is None:
#             return node, False

#         deleted = False
#         if key == node.data:
#             deleted = True
#             if node.left and node.right:
#                 # replace the node to the leftmost of node.right
#                 parent, child = node, node.right
#                 while child.left is not None:
#                     parent, child = child, child.left
#                 child.left = node.left
#                 if parent != node:
#                     parent.left = child.right
#                     child.right = node.right
#                 node = child
#             elif node.left or node.right:
#                 node = node.left or node.right
#             else:
#                 node = None
#         elif key < node.data:
#             node.left, deleted = self._delete_value(node.left, key)
#         else:
#             node.right, deleted = self._delete_value(node.right, key)
#         return node, deleted
