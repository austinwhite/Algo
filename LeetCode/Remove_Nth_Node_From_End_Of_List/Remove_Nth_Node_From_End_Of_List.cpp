// Time: O(n) where n is equal to the number of nodes in the linked list
// Space: O(1)

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* runner = head;
        ListNode* walker = head;
        ListNode* prev = head;
        
        for (int i=0; i<n; i++) {
            runner = runner->next;
        }
        
        if (!runner) {
            return head->next;
        }
        
        while (runner) {
            prev = walker;
            walker = walker->next;
            runner = runner->next;
        }
        
        if (prev == walker) {
            head->val = head->next->val;
            head->next = head->next->next;
        } else {
            prev->next = walker->next;
        }
        
        return head;
    }
};