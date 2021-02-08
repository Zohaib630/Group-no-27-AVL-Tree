#Github link: https://github.com/Zohaib630/Group-no-27-AVL-Tree/upload/main


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class Avl_Tree:

    def __init__(self):
        self.s = None

    def Insert_tion(self, s, key):
        if s == None:
            return Node(key)
        elif key < s.value:
            s.left = self.Insert_tion(s.left, key)
        else:
            s.right = self.Insert_tion(s.right, key)

        s.height = 1 + max(self.__Height_0f_Node(s.left), self.__Height_0f_Node(s.right))

        #  Left-Left Rotation
        if self.__Balance_factor(s) > 1 and key < s.left.value:
            return self.Right_of_subtree(s)

        # Right-Right Rotation
        elif self.__Balance_factor(s) < -1 and key > s.right.value:
            return self.Left_of_subtree(s)

        # Left-Right Rotation
        elif self.__Balance_factor(s) > 1 and key > s.left.value:
            s.left = self.Left_of_subtree(s.left)
            return self.Right_of_subtree(s)

        # Right-Left Rotation
        elif self.__Balance_factor(s) < -1 and key < s.right.value:
            s.right = self.Right_of_subtree(s.right)
            return self.Left_of_subtree(s)

        return s

    def Right_of_subtree(self, i):
        sub = i.left
        temp = sub.right
        sub.right = i
        i.left = temp
        i.height = 1 + max(self.__Height_0f_Node(i.left), self.__Height_0f_Node(i.right))
        sub.height = 1 + max(self.__Height_0f_Node(sub.left), self.__Height_0f_Node(sub.right))
        return sub

    def Left_of_subtree(self, i):
        sub = i.right
        temp = sub.left
        sub.left = i
        i.right = temp
        i.height = 1 + (max(self.__Height_0f_Node(i.left), self.__Height_0f_Node(i.right)))
        sub.height = 1 + max(self.__Height_0f_Node(sub.left), self.__Height_0f_Node(sub.right))
        return sub

    def __Height_0f_Node(self, s):
        if s == None:
            return 0
        return s.height

    def __Balance_factor(self, s):
        if s == None:
            return 0
        return self.__Height_0f_Node(s.left) - self.__Height_0f_Node(s.right)

    def __Miin(self, node):
        if node == None:
            raise Exception
        else:
            if node.left == None:
                return node.value
            else:
                return self.__Miin(node.left)

    def Delete_of_node(self, s, value):

        if s.value == value:
            # leaf case
            if s.left == None and s.right == None:
                return None
            # only right child
            if s.left == None and s.right != None:
                return s.right
            # only left child
            if s.left != None and s.right == None:
                return s.left
        elif value < s.value:
            s.left = self.Delete_of_node(s.left, value)
            return s

        elif value > s.value:
            s.right = self.Delete_of_node(s.right, value)
            return s

        else:
            if s.left is None:
                node = s.right
                s = None
                return s
            elif s.right is None:
                node = s.left
                s = None
                return s
            node = self.__Miin(s.right)
            s.value = node.value
            s.right = self.Delete_of_node(s.right, node.value)

        # update the height of the node
        s.height = 1 + max(self.__Height_0f_Node(s.left), self.__Height_0f_Node(s.right))

        # Get the balance factor
        balance = self.__Balance_factor(s)

        # left left rotation
        if balance > 1 and self.__Balance_factor(s.right) >= 0:
            return self.Right_of_subtree(s)

        # right right rotation
        if balance < -1 and self.__Balance_factor(s.right) <= 0:
            return self.Left_of_subtree(s)

        # left right rotation
        if balance > 1 and self.__Balance_factor(s.left) < 0:
            s.left = self.Left_of_subtree(s.left)
            return self.Right_of_subtree(s)

        # Right left rotation
        if balance < -1 and self.__Balance_factor(s.right) > 0:
            s.right = self.Right_of_subtree(s.right)
            return self.Left_of_subtree(s)
        return s

    def Pre_Order(self, s):
        if s:
            print(s.value)
            self.Pre_Order(s.left)
            self.Pre_Order(s.right)

    def Post_Order(self,s):
        if s:
            self.Pre_Order(s.left)
            self.Pre_Order(s.right)
            print(s.value)

    def In_Order(self,s):
        if s:
            self.Pre_Order(s.left)
            print(s.value)
            self.Pre_Order(s.right)

def Driver_code():
    l = Avl_Tree()

    s = None
    s = l.Insert_tion(s, 50)
    s = l.Insert_tion(s, 60)
    s = l.Insert_tion(s, 70)
    s = l.Insert_tion(s, 80)
    s = l.Insert_tion(s, 90)
    s= l.Insert_tion(s, 85)

    command = input("Select the Number\n1)PostOrder\n2)PreOrder\n3)InOrder\n")
    print("Tree After Insertion")
    if command == "1":
        l.Post_Order(s)
    elif command == "2":
        l.Pre_Order(s)

    elif command == "3":
        l.In_Order(s)

    print("Tree After Deletion")
    l.Delete_of_node(s, 80)
    if command == "1":
        l.Post_Order(s)
    elif command == "2":
        l.Pre_Order(s)
    elif command == "3":
        l.In_Order(s)

    return l

Driver_code()
