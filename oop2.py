class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):

        print("B")

class C(B):
    def __init__(self):
        pass
        

o1=C()