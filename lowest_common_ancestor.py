from treenode import TreeNode
from tree_builder import build_tree, get_node
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """use dfs to build path between root and given node"""
        def traverse(v, w, a):
            a.append(w)
            if v is w:
                return True
            if w.left and traverse(v, w.left, a):
                return True
            if w.right and traverse(v, w.right, a):
                return True
            a.pop()
            return False
            
        a = []
        b = []
        traverse(p,root,a)
        traverse(q,root,b)
        for u,v in zip(a,b):
            if u is v:
                res = u
            else:
                break
        return res.val
       
tree = build_tree([3,5,1,6,2,0,8,None,None,7,4])
pp,qq=5,1
pp=get_node(tree,pp)
qq=get_node(tree,qq)
assert Solution().lowestCommonAncestor(tree,pp,qq) == 3
# pp,qq=5,4
# pp=get_node(tree,pp)
# qq=get_node(tree,qq)
# assert Solution().lowestCommonAncestor(tree,pp,qq) == 5