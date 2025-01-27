# User function Template for python3

# design the class in the most optimal way

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.capacity = cap
        self.cache = {}  # Dictionary to store key-node pairs
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the doubly linked list."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add(self, node):
        """Add a node to the tail of the doubly linked list."""
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    # Function to return value corresponding to the key.
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            # Move node to the tail as it is most recently used
            self._add(node)
            return node.value
        return -1

    # Function for storing key-value pair.
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            # Remove the least recently used item (head's next node)
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

        # Add the new key-value pair
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)
# {
 # Driver Code Starts
# Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends
