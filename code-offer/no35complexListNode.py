import ComlplexListNode



def cloneNode(pHead):
    pNode = pHead
    while pNode:
        pClone = ComlplexListNode.ListNode(pNode.val)
        pClone.next = pNode.next
        pNode.next = pClone
        pNode = pClone.next

def connectSiblingNode(pHead):
    pNode = pHead

    while pNode:
        pClone = pNode.next
        # 这里要加一层判断
        if pNode.sibling:
            pClone.sibling = pNode.sibling.next
        pNode = pClone.next

def reconnectNode(pHead):
    pNode = pHead
    pCLoneHead = pCloneNode =pNode.next
    pNode.next = pCloneNode.next
    pNode = pNode.next

    while pNode:
        pCloneNode.next = pNode.next
        pCloneNode = pCloneNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next
    return pCLoneHead


def Clone(pHead):
    if not pHead:
        return None
    cloneNode(pHead)
    connectSiblingNode(pHead)
    return reconnectNode(pHead)

def Test1():
    pNode1 = ComlplexListNode.ListNode(1)
    pNode2 = ComlplexListNode.ListNode(2)
    pNode3 = ComlplexListNode.ListNode(3)
    pNode4 = ComlplexListNode.ListNode(4)
    pNode5 = ComlplexListNode.ListNode(5)

    pNode1.connectNodes(pNode2,pNode3)
    pNode2.connectNodes(pNode3,pNode5)
    pNode3.connectNodes(pNode4,None)
    pNode4.connectNodes(pNode5,pNode2)

    pNode1.printList()

    pNode1 = Clone3(pNode1)

    pNode1.printList()

def Clone2(pHead):
    # write code here
    if  pHead==None:
        return None
    # pHead.printList()

    newNode=ComlplexListNode.ListNode(pHead.val)
    newNode.random=pHead.sibling
    newNode.next=Clone2(pHead.next)
    # print("new:")
    # newNode.printList()
    return newNode

def Clone3(pHead):
    if not pHead:
        return
    pNode = pHead
    pCloneHead = newNode = ComlplexListNode.ListNode(pNode.val)
    while pNode:

        newNode.val = pNode.val
        newNode.sibling = pNode.sibling

        pNode = pNode.next
        if pNode:
            # 每一个node都要是新的节点，才是一条新的链
            newNode.next = ComlplexListNode.ListNode(None)
            newNode = newNode.next

    return pCloneHead


    return newNode



if __name__ == '__main__':
    Test1()