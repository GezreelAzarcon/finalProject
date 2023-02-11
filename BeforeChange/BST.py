

#I WILL BE USING A SIMPLE BINARY SEARCH TREE!

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addNode(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addNode(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.addNode(data)
            else:
                self.right = BinarySearchTree(data)

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()
        
        return elements

    def preOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()
        
        return elements

    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.data)

        return elements
    
    def find(self, data):
        if data < self.data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
        else: 
            return True

    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()

    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            minVal = self.right.findMin()
            self.data = minVal
            self.right = self.right.delete(minVal)
        return self
        
def buildTree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.addNode(elements[i])

    return root

def mainMenu(longList):
    myTree = buildTree(longList)
    print()
    print("find, findMax, findMin, sort")
    print()
    while True:
        menu = input("Choose what to do: ")
        if menu == "find":
            num3 = int(input("What number do you want to find: "))      
            print(myTree.find(num3))
            break
        elif menu == "findmax": 
            print(myTree.findMax())
            break
        elif menu == "findmin":
            print(myTree.findMin())
            break
        elif menu == "sort":
            print("This is the sorted list:")
            print(myTree.inOrderTraversal())
            break
        else:
            print("Wrong input!")
            continue

