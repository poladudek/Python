import unittest

class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
            return not self == other
    
class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node



        # Dodane metody:
    
    def search(self, data): 
        if self is None:
            return None
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

        return None
    
    def find_min(self): 
        if self.head is None:
            return None

        smallestData = self.head.data
        smallestNode = self.head 
        currentNode = self.head

        while currentNode is not None: 
            if currentNode.data < smallestData:
                smallestData = currentNode.data
                smallestNode = currentNode
            currentNode = currentNode.next

        return smallestNode

    def find_max(self):
        if self.head is None:
            return None

        biggestData = self.head.data
        biggestNode = self.head
        currentNode = self.head 

        while currentNode is not None:
            if currentNode.data > biggestData:
                biggestData = currentNode.data
                biggestNode = currentNode
            currentNode = currentNode.next

        return biggestNode


    def reverse_list(self, node):
        before = None
        current = node
        while current:
            nextNode = current.next
            current.next = before
            before = current 
            current = nextNode 
        return before


class TestSingleList(unittest.TestCase):

    def test_search(self):
        list1 = SingleList()

        node1 = Node(56)
        node2 = Node(77)
        node3 = Node(0)
        node4 = Node(2)
        node5 = Node(5)

        list1.insert_tail(node1)
        list1.insert_tail(node2)
        list1.insert_head(node3)


        self.assertEqual(list1.search(56), node1)
        self.assertEqual(list1.search(77), node2)
        self.assertEqual(list1.search(0), Node(0))

        self.assertIsNone(list1.search(2))
        list1.insert_head(node4)
        self.assertIsNotNone(list1.search(2))

        list1.insert_tail(node5)
        self.assertNotEqual(list1.search(5), node3)

    def test_find_min(self):
        list1 = SingleList()
        list2 = SingleList()
        list3 = SingleList()
        list4 = SingleList()

        self.assertIsNone(list1.find_min())

        node1 = Node(-3444)
        node2 = Node(-45676)
        node3 = Node(63)
        node4 = Node(30)
        node5 = Node(29)
        node6 = Node(28)
        node7 = Node(5.5)
        node8 = Node(5.56)
        node9 = Node(5.57)

        list2.insert_head(node1)
        self.assertEqual(list2.find_min(), node1)
        list2.insert_head(node2)
        self.assertEqual(list2.find_min(), node2)
        list2.insert_head(node3)
        self.assertEqual(list2.find_min(), node2)

        list3.insert_tail(node4)
        list3.insert_tail(node5)
        list3.insert_tail(node6)
        self.assertEqual(list3.find_min(), node6)
        self.assertNotEqual(list3.find_min(), node5)

        list4.insert_head(node7)
        list4.insert_head(node8)
        list4.insert_head(node9)
        self.assertEqual(list4.find_min(), Node(5.5))
        

    def test_find_max(self):
        list1 = SingleList()
        list2 = SingleList()
        list3 = SingleList()

        self.assertIsNone(list1.find_max())

        node1 = Node(5)
        node2 = Node(3)
        node3 = Node(2)
        node4 = Node(106)
        node5 = Node(-2000)
        node6 = Node(228)

        list2.insert_tail(node1)
        self.assertEqual(list2.find_max(), node1)
        list2.insert_tail(node2)
        list2.insert_tail(node3)
        self.assertEqual(list2.find_max(), node1)
        

        list3.insert_head(node4)
        list3.insert_head(node5)
        self.assertEqual(list3.find_max(), node4)
        list3.insert_head(node6)
        self.assertEqual(list3.find_max(), node6)

        self.assertNotEqual(list3.find_max(), Node(2))
        

    def test_reverse(self):
        # test 1:

        listFunction = SingleList()
        listManual = SingleList()

        for i in range(10):
            listFunction.insert_head(Node(i))

        for i in range(10):
            listManual.insert_tail(Node(i)) #wprowadzam liczby od konca wiec lista jest juz "odwrocona"

        headFunction = listFunction.reverse_list(listFunction.head)
        headManual = listManual.head

        for _ in range(10):
            self.assertEqual(headFunction.data, headManual.data)
            headFunction = headFunction.next
            headManual = headManual.next
        
        # test 2:
        
        listFunction2 = SingleList()
        listManual2 = SingleList()

        for i in range(1, 4, 1):
            listFunction2.insert_tail(Node(i))
        
        for i in range(3, 0, -1):
            listManual2.insert_tail(Node(i))
    
        headFunction2 = listFunction2.reverse_list(listFunction2.head)
        headManual2 = listManual2.head

        for _ in range(3):
            self.assertEqual(headFunction2.data, headManual2.data)
            headFunction2 = headFunction2.next
            headManual2 = headManual2.next

        # test 3:

        listFunction3a = SingleList()
        listFunction3b = SingleList()

        for i in range(5):
            listFunction3a.insert_head(Node(i))
            listFunction3b.insert_head(Node(i))
        
        headFunction3a = listFunction3a.reverse_list(listFunction3a.head)
        headFunction3b = listFunction3b.reverse_list(listFunction3b.head)

        for _ in range(5):
            self.assertEqual(headFunction3a.data, headFunction3b.data)
            headFunction3a = headFunction3a.next
            headFunction3b = headFunction3b.next



if __name__ == "__main__":
    unittest.main()
