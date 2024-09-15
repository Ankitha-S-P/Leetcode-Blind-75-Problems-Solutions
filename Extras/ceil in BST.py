#https://www.naukri.com/code360/problems/ceil-from-bst_920464?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION
def findCeil(root, x):
    ceil=-1
    while root:
        if root.data==x:
            return x
        elif root.data>x:
            ceil=root.data
            root=root.left
        else:
            root=root.right        
    return ceil
