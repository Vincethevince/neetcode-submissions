class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.prev = None
        self.next = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.valStore =  {} # value : nodes
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)

        self.right.prev = self.left
        self.left.next = self.right

    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.valStore:
            self.remove(self.valStore[key])
            self.insert(self.valStore[key])

            return self.valStore[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.valStore:
            self.remove(self.valStore[key])
        
        self.valStore[key] = ListNode(value,key)
        self.insert(self.valStore[key])


        if len(self.valStore)  > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.valStore[LRU.key]
            
        