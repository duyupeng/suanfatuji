class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack,res=[root],[]
        while stack:
            node=stack.pop()
            if isinstance(node,TreeNode):
                stack.extend([node.right,node.left,node.val])
            elif isinstance(node,int):
                res.append(node)
        return res