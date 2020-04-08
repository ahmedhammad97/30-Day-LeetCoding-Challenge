struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fastRunner = head;
        ListNode* slowRunner = head;
        while(fastRunner && fastRunner->next) {
            fastRunner = fastRunner->next->next;
            slowRunner = slowRunner->next;
        }
        return slowRunner;
    }
};

/*
    If a fast runner takes 2 hops per turn, while a
    slow runner takes only one, the slow pointer will
    be at the middle of the list when the fast runner
    reaches the end of it.
*/