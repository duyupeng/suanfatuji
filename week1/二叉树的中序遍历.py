class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white,gray=1,0
        stack=[(white,root)]
        res=[]
        while stack:
            colar,node=stack.pop()
            if not node:
                continue
            if colar==white:
                stack.append((white,node.right))
                stack.append((gray,node))
                stack.append((white,node.left))
            else :
                res.append(node.val)
        return res