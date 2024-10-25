from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def searchBST(self, root:Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    
    if val == root.val:
        return root
    elif val > root.val:
        return self.searchBST(root.right, val)
    else:
        return self.searchBST(root.left, val)