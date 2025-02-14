# URL https://neetcode.io/problems/lru-cache
# Time Complexity: O(1)
# Space Complexity: O(N)

class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def _set_most_recent(self, node, new=False):
        if not new:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        prev_node = self.right.prev
        prev_node.next = node
        self.right.prev = node
        node.prev = prev_node
        node.next = self.right

    def _prune_node(self):
        node_to_remove = self.left.next
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        del self.data[node_to_remove.key]

    def get(self, key: int) -> int:
        node_requested = self.data.get(key)
        if not node_requested:
            return -1
        self._set_most_recent(node_requested)
        return node_requested.value

    def put(self, key: int, value: int) -> None:
        node = self.data.get(key)
        if node:
            node.value = value
            self._set_most_recent(node)
        else:
            node = Node(key, value)
            self.data[key] = node
            self._set_most_recent(node, new=True)
        while len(self.data) > self.capacity:
            self._prune_node()

        

