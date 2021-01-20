class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def add_to_head(self, n):
        n.next = self.head
        self.head = n
    def del_from_head(self):
        if self.head is None:
            return None
        old_head = self.head
        self.head = self.head.next
        old_head.next = None
        return old_head
    def push(self, n):
        self.add_to_head(n)
    def pop(self):
        return self.del_from_head()
    def isEmpty(self):
        return self.head == None
    def print_list(self):
        cur = self.head
        while cur is not None:
            print(cur.value, end="")
            if cur.next is not None:
                print(" -> ", end="")
            cur = cur.next
        print()

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return f"ListNode({repr(self.value)})"
        
def validBracketSequence(sequence):
    stack = LinkedList()
    for bracket in sequence:
        if bracket == "(":
            stack.push(ListNode(bracket))
        elif bracket == "[":
            stack.push(ListNode(bracket))
        elif bracket == "{":
            stack.push(ListNode(bracket))
        elif bracket == ")":
            if stack.isEmpty() is True:
                return False
            else:
                last_opening = stack.pop()
                if last_opening.value != "(":
                    return False
                
        elif bracket == "]":
            if stack.isEmpty() is True:
                return False
            else:
                last_opening = stack.pop()
                if last_opening.value != "[":
                    return False
        elif bracket == "}":
            if stack.isEmpty() is True:
                return False
            else:
                last_opening = stack.pop()
                if last_opening.value != "{":
                    return False
    return stack.isEmpty()

