# User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''


class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        temp1 = head1
        temp2 = head2
        ans = None
        temp = None
        while temp1 != None and temp2 != None:
            if temp1.data <= temp2.data:
                if temp1 == head1 and temp2 == head2:
                    ans = temp1
                    temp = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp1
                    temp = temp1
                    temp1 = temp1.next
            else:
                if temp1 == head1 and temp2 == head2:
                    ans = temp2
                    temp = temp2
                    temp2 = temp2.next
                else:
                    temp.next = temp2
                    temp = temp2
                    temp2 = temp2.next
        if temp1 != None:
            temp.next = temp1
        elif temp2 != None:
            temp.next = temp2
        return ans

# {
 # Driver Code Starts


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()
    print("~")


def insert_sorted(head, data):
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = list(map(int, input().split()))
        input2 = list(map(int, input().split()))

        head1 = None
        for item in input1:
            head1 = insert_sorted(head1, item)

        head2 = None
        for item in input2:
            head2 = insert_sorted(head2, item)

        obj = Solution()
        merged_head = obj.sortedMerge(head1, head2)
        print_list(merged_head)

# } Driver Code Ends
