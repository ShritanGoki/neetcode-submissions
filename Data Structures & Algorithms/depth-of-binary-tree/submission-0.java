/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        
        int resultLeft = 1;
        int resultRight = 1;

        if (root.left != null){
            resultLeft += maxDepth(root.left);
        }
        if (root.right != null){
            resultRight +=maxDepth(root.right);
        }

        if(resultLeft>resultRight){
            return resultLeft;
        }
        else{
            return resultRight;
        }
    }
}
