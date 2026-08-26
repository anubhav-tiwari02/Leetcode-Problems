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
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy=new ListNode(0);
        ListNode curr=head;
        ListNode ptr=dummy;
        ListNode next=null;
       
        while(curr!=null){
            next=curr.next;
            while(ptr.next!=null && ptr.next.val<curr.val){
                ptr=ptr.next;
            }
            curr.next=ptr.next;
            ptr.next=curr;
            ptr=dummy;
            curr=next;
        }
        return dummy.next;
    }
}