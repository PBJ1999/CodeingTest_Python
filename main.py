class ListNode:
    def __init__(self, val):
        self.val = val # DATA(VALUE)
        self.next = None # NEXT POINT (NONE)

head = ListNode(12)
# first Head Node, which has data 12

head.next = ListNode(13) # ,,,,,,

# 반복문 사용
def printnodes(node:ListNode):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next

# 재귀 방법 사용
def printNodesRecur(node:ListNode):
    print(node.val, end=' ')
    if node.next is not None:
        printNodesRecur(node.next)

printnodes(head)