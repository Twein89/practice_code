class A():
    def foo1(self):
        print "A"

class B(A):
    def foo2(self):
        print "B"

class C(A):
    def foo3(self):
        print "C"

class D(B, C):
    pass

d = D()
d.foo1()
