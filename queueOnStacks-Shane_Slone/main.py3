class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        finished = left.isEmpty()
        while not finished:
            right.push(left.pop())
            finished = left.isEmpty()
        popped_item = right.pop()
        finished = right.isEmpty()
        while not finished:
            left.push(right.pop())
            finished = right.isEmpty()
        return popped_item

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans
