class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertBST(root,val):
    if not root:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insertBST(root.right, val)
    elif val < root.val:
        root.left = insertBST(root.left, val)
    
    return root

def minValueNode(root):
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur

def remove(root, val):
    if not root:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root