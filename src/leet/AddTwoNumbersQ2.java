

/*

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

*/


import java.util.ArrayList;

class AddTwoNumbersQ2 {
    public static void main(String[] args) {

        ListNode one = new ListNode(9);
        ListNode two = new ListNode(9);
        ListNode three = new ListNode(9);

        one.next = two;
        two.next = three;

        addTwoNumbers(one, one);

    }

    static ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        LinkedList list = new LinkedList();
        int lastNum = 0;

        while (l1 != null || l2 != null) {
            if (l1 != null && l2 != null) {

                int sum = l1.val + l2.val + (lastNum / 10);
                lastNum = sum;

                list.addLast(new ListNode(sum % 10));

                l1 = l1.next;
                l2 = l2.next;

            } else if (l1 != null) {

                int sum = l1.val + (lastNum / 10);
                lastNum = sum;

                list.addLast(new ListNode(sum % 10));
                l1 = l1.next;

            } else {

                int sum = l2.val + (lastNum / 10);
                lastNum = sum;

                list.addLast(new ListNode(sum % 10));
                l2 = l2.next;

            }
        }

        if (lastNum > 9) list.addLast(new ListNode(1));

        System.out.println(list.toList());
        return list.head;
    }

    static class LinkedList {
        ListNode head;
        ListNode tail;

        void addLast(ListNode element) {
            if (head == null) {
                head = element;
                tail = head;
            } else {
                tail.next = element;
                tail = tail.next;
            }
        }

        ArrayList toList() {
            ArrayList l = new ArrayList();
            ListNode temp = head;
            while (temp != null) {
                l.add(temp.val);
                temp = temp.next;
            }
            return l;
        }
    }

    static class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }
}
