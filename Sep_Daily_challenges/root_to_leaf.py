import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def binary(l):
    s=0
    i=0
    for x in range(len(l)-1,-1,-1):
        s+=l[x]*(2**i)
        i+=1
    return s
def preOrder(root,l,s):
    if root==None:
        return 
    l.append(root.data)
    # print(root.data,end=" ")
    preOrder(root.left,l,s)
    if root.left==None and root.right==None:
        x=binary(l)
        s.append(x)
    preOrder(root.right,l,s)
    l.pop()
    return sum(s)

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
print(preOrder(root,[],[]))


# ----------------------------------OR--------------------------------------
                        # Leet Code Solution


# class Solution:
#     def sumRootToLeaf(self, root: TreeNode) -> int:
#         s=[]
#         return self.helper(root,[],s)

#     def helper(self,root,l,s):
#         if root is None:
#             return 
#         l.append(root.val)
#         self.helper(root.left,l,s)
        
#         if root.left==None and root.right==None:
#             c=self.binary_calculator(l)
#             s.append(c)
        
#         self.helper(root.right,l,s)
#         l.pop()
#         return sum(s)
#     def binary_calculator(self,l):
#         s=0
#         i=0
#         for x in range(len(l)-1,-1,-1):
#             s+=l[x]*(2**i)
#             i+=1
#         return s