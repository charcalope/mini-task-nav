from TreeNode import TreeNode

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0: return
        if len(preorder) == 1: return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        div = inorder.index(preorder[0])
        root.down = self.buildTree(preorder[1:(div + 1)], inorder[0:div])
        root.right = self.buildTree(preorder[(div + 1):], inorder[(div + 1):])
        return root

    def buildTree2(self, preorder, inorder):
        if len(preorder) == 0: return
        if len(preorder) == 1: return TreeNode(preorder[0])
        return self.buildTreeRec(preorder, inorder, 0, 0, len(preorder))

    def buildTreeRec(self, preorder, inorder, P, I, element):
        if element == 0:
            return None
        root = TreeNode(preorder[P])
        div = 0;
        for i in range(I, I + element):
            if inorder[i] == preorder[P]: break
            div += 1
        root.down = self.buildTreeRec(preorder, inorder, P + 1, I, div)
        root.right = self.buildTreeRec(preorder, inorder, P + div + 1, I + div + 1, element - 1 - div)
        return root