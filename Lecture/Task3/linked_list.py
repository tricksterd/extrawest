class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next_value = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def is_empy(self):
        return self.head is None

    def __add(self, item):
        node = Node(item)
        node.next_value = self.head
        self.head = node

    def append(self, item):
        node = Node(item)
        if self.is_empy():
            self.head = node
        else:
            cur = self.head
            while cur.next_value:
                cur = cur.next_value
            cur.next_value = node

    def insert(self, position, item):
        if position == 0:
            self.__add(item)
        elif 0 < position <= self.len():
            node = Node(item)
            count = 0
            cur = self.head
            while cur:
                if position == count + 1:
                    node.next_value = cur.next_value
                    cur.next_value = node
                cur = cur.next_value
                count += 1
        else:
            raise 'index out of range'

    def len(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next_value
        return count

    def remove(self, item):
        prev = None
        cur = self.head
        found = False
        while cur is not None and not found:
            if cur.value == item:
                found = True
                if prev:
                    prev.next_value = cur.next_value
                else:
                    self.head = cur
            else:
                prev = cur
                cur = cur.next_value
        return found

    def pop(self, position=None):
        cur = self.head
        count = 0
        if position is None:
            while cur:
                count += 1
                if count == self.len():
                    self.remove(cur.value)
                    return cur.value
                cur = cur.next_value
        elif 0 < position < self.len():
            while cur:
                if count == position:
                    self.remove(cur.value)
                    return cur.value
                count += 1
                cur = cur.next_value
        else:
            raise 'index out of range'

    def __str__(self):
        if self.head is not None:
            cur = self.head
            out = '[' + str(cur.value)
            while cur.next_value is not None:
                cur = cur.next_value
                out += ', ' + str(cur.value)
            return out + ']'
        return '[]'
