class Node: 
    def __init__(self, dataval=None):
        self.dataval = dataval 
        self.nextval = None

class linkedlist: 
    def __init__(self):
        self.headval = None
    def printlinkedlist(self):
        printval = self.headval
        while printval is not None: 
            print(printval.dataval + "->")
            printval = printval.nextval
    def insert(self, newdata): 
        newNode = Node(newdata)
        newNode.nextval = self.headval
        self.headval = newNode
    def listLength(self): 
        count = 0
        while self.headval is not None: 
            count += 1 
            self.headval = self.headval.nextval
        print("the list is {} long".format(count))
    def insertEnd(self, newdata): 
        newNode = Node(newdata)
        if self.headval is None: 
            self.headval = newNode
            return 
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval 
        laste.nextval = newNode
    def insertBetween(olddata, newdata, self): 
        if olddata is None: 
            print("Current node is none")
            return 
        NewNode = Node(newdata)
        newNode.nextval = olddata.nextval
        olddata.nextval = newNode
    def remove(self, removeddata): 
        head = self.headval
        if head is not None: 
            if head.dataval == removeddata: 
                self.headval = head.nextval
                head = None 
                return 
        while (head is not None): 
            if head.dataval == removeddata: 
                break 
            prev= head 
            head = head.nextval
        if head == None: 
            return 
        prev.nextval = head.nextval
        head = None 

tahap1 = linkedlist()
tahap1.headval = Node("kenal")
tahap2 = Node("deket")
tahap3 = Node("pacaran")
tahap4 = Node("putus lu mampus")
tahap1.headval.nextval = tahap2
tahap2.nextval = tahap3 
tahap3.nextval = tahap4

tahap1.insertEnd("test ending")
tahap1.insert("test beginning")
tahap1.listLength()
tahap1.remove("test ending")
tahap1.listLength()
tahap1.printlinkedlist()



