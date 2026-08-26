class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        old_head = head
        new_head = Node(old_head.val)
        temp = new_head
        
        node_map = {old_head: new_head}

        while old_head and old_head.next:
            old_head = old_head.next
            temp.next = Node(old_head.val)
            temp = temp.next
            node_map[old_head] = temp 

        old_head = head
        temp = new_head

        while old_head :
            if old_head.random == None:
                temp.random = None
            else:
                temp.random = node_map[old_head.random]

            temp = temp.next
            old_head = old_head.next

        return new_head