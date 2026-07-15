/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null || head.next == null){
            return false;
        }

        ListNode leading = head;
        ListNode trailing = head;

        while(leading != null && leading.next != null){
            leading = leading.next.next;
            trailing = trailing.next;
            if(leading == trailing){
                return true;
            }
        }
        return false;
    }
}
