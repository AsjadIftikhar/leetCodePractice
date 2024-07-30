from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        merged_list = list1
        list1 = list1.next
    else:
        merged_list = list2
        list2 = list2.next

    start = merged_list
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            merged_list.next = list1
            list1 = list1.next
        else:
            merged_list.next = list2
            list2 = list2.next

        merged_list = merged_list.next

    if list1 is None:
        merged_list.next = list2
    else:
        merged_list.next = list1

    return start


four = ListNode(4)
two = ListNode(2, four)
one = ListNode(1, two)

_four = ListNode(4)
_three = ListNode(3, _four)
_one = ListNode(1, _three)

node = mergeTwoLists(one, _one)
while node is not None:
    print(node.val, "-> ", end="")
    node = node.next
