# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

        if l1 == None and l2 == None: return ListNode(None)
        l3head = ListNode(None)
        l3tail = l3head
        compleat = False

        while not compleat:
            if l1 != None and l2 != None:
                if l1.val <= l2.val:
                    l3tail.next = l1
                    l3tail = l1
                    l1 = l1.next
                else:
                    l3tail.next = l2
                    l3tail = l2
                    l2 = l2.next

            elif l1 != None:
                compleat = True
                l3tail.next = l1
                l3tail = l1

            elif l2 != None:
                compleat = True
                l3tail.next = l2
                l3tail = l2

        return l3head.next





head1 = ListNode(1)

one = ListNode(2)
one1 = ListNode(2)
one2 = ListNode(2)
one3 = ListNode(3)
one4 = ListNode(4)
one5 = ListNode(6)
one6 = ListNode(8)
one7 = ListNode(9)

head1.next = one
one.next = one1
one1.next = one2
one2.next = one3
one3.next = one4
one4.next = one5
one5.next = one6
one6.next = one7

head2 = ListNode(1)

two = ListNode(2)
two1 = ListNode(2)
two2 = ListNode(3)
two3 = ListNode(3)
two4 = ListNode(4)

head2.next = two
two.next = two1
two1.next = two2
two2.next = two3
two3.next = two4

s = Solution
l = s.mergeTwoLists(head1, head2)

while l != None:
    print(l.val)
    l = l.next