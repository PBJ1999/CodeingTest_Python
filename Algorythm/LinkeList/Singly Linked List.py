class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def printNodes(node: ListNode):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next


class SLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):  # O(1)
        node = ListNode(val)
        node.next = self.head
        self.head = node

    # but when the list
    def addBack(self, val):  # O(n)
        node = ListNode(val)
        crnt_node = self.head
        while crnt_node.next:
            crnt_node = crnt_node.next
        crnt_node.next = node

    def findNode(self, val):  # O(n)
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.val == val:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node not found')

    def addAfter(self, node, val):  # O(1)
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node

    def deleteAfter(self, prev_node):  # O(1)
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next





linked_list = SLinkedList()

# 머리에 노드 추가
linked_list.addAtHead(1)
linked_list.addAtHead(2)
linked_list.addAtHead(3)

# 노드 출력
print("연결 리스트의 노드:")
printNodes(linked_list.head)  # 출력: 3 2 1

# 끝에 노드 추가
linked_list.addBack(4)

# 다시 노드 출력
print("끝에 노드를 추가한 후의 연결 리스트의 노드:")
printNodes(linked_list.head)  # 출력: 3 2 1 4

# 값이 2인 노드 찾기
node = linked_list.findNode(7)
print("값이 2인 노드를 찾았습니다:", node.val)  # 출력: 값이 2인 노드를 찾았습니다: 2

# 값이 2인 노드 뒤에 값이 5인 노드 추가
linked_list.addAfter(node, 5)

# 다시 노드 출력
print("특정 노드 뒤에 노드를 추가한 후의 연결 리스트의 노드:")
printNodes(linked_list.head)  # 출력: 3 2 5 1 4

# 값이 2인 노드 뒤의 노드 삭제
linked_list.deleteAfter(node)

# 다시 노드 출력
print("노드를 삭제한 후의 연결 리스트의 노드:")
printNodes(linked_list.head)  # 출력: 3 2 1 4