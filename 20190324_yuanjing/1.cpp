/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    vector<vector<int> > Print(TreeNode* pRoot) {
        stack<TreeNode*> odd;//先左后右
        stack<TreeNode*> even;//先右后左
        vector<vector<int> > result;
        if(pRoot == nullptr){
            return result;
        }
        TreeNode* p = pRoot;
        int flag = 1;
        odd.push(p);
        while(!odd.empty() || !even.empty()){
            vector<int> tmp;
            if(flag % 2){//当前奇数层
                while(!odd.empty()){
                    p = odd.top();
                    tmp.push_back(p -> val);
                    odd.pop();
                    if(p -> left != nullptr){
                        even.push(p -> left);
                    }
                    if(p -> right != nullptr){
                        even.push(p -> right);
                    }
                }
                result.push_back(tmp);
                ++flag;
            }
            else{//当前偶数层
                while(!even.empty()){
                    p = even.top();
                    tmp.push_back(p -> val);
                    even.pop();
                    if(p -> right != nullptr){
                        odd.push(p -> right);
                    }
                    if(p -> left != nullptr){
                        odd.push(p -> left);
                    }
                    
                }
                result.push_back(tmp);
                ++flag;
            }
        }
        return result;
    }
    
};