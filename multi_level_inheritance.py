class Grandparent:
    def family_tree(self):
        print("I am the grandparent.")

class Parent(Grandparent):
    def family_tree(self):
        print("I am the parent.")

class Child(Parent):
    def family_tree(self):
        print("I am the child.")

child = Child()
child.family_tree()

super(Parent, child).family_tree()
