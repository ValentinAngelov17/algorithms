def merge_in_between(list1: list, a: int, b: int, list2: list):
    prev = list1
    temp1 = list1
    curr = list1
    a -= 1  # Adjust a to match zero-based indexing

    # Traverse list1 to find the node at position (a-1)
    while temp1 and a > 0:
        temp1 = temp1.next
        prev = temp1
        a -= 1

    temp1 = list1  # Reset temp1 to traverse list1 again

    # Traverse list1 to find the node at position (b+1)
    while temp1 and b > 0:
        temp1 = temp1.next
        curr = temp1
        b -= 1

    temp2 = list2  # Initialize pointer to traverse list2

    # Traverse list2 to find the last node
    while temp2.next:
        temp2 = temp2.next

    prev.next = list2  # Connect the node before position 'a' to the head of list2
    temp2.next = curr.next  # Connect the last node of list2 to the node after position 'b'

    return list1  # Return the head of list1


print(merge_in_between(list1=[0, 1, 2, 3, 4, 5, 6], a=2, b=5, list2=[1000000, 1000001, 1000002, 1000003, 1000004]))
