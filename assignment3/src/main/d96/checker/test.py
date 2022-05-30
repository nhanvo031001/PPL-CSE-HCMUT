from tokenize import Number

from numpy import size


class ComponentClass:
    def __init__(self):
        self.attribute = {}
        self.method = {}
        
    def add_attribute(self, name, type_data):
        self.attribute[name] = type_data
        
    def lookup_attribute(self, name):
        return self.attribute[name] if name in self.attribute else None
    
    def add_method(self, name, type_data):
        self.method[name] = type_data
        
    def lookup_method(self, name):
        return self.method[name] if name in self.method else None
    
    def __str__(self):
        return "Component Class: attribute: " + str(self.attribute) + " method: " + str(self.method)
    
class Test:
    global_env = [{'type_decl': {}}]
    def __init__(self):        
        self.a = 1
        
    def __str__(self):
        return "Global env: " + str(Test.global_env)
    
    def run(self):
        print(self.visitBlock(Test.global_env))
    
    def visitBlock(self, o):
        sizeVar = 0
        sizeBlocks = []
        
        for i in range(4):
            if i == 0:
                print("i == ", i)
                val = self.visitVarDecl(o, 'int')
                sizeVar += 2 if val == 'int' else 6
            if i == 1:
                print("i == ", i)
                self.visitTypeDecl(o, 'vd', 'float')
            if i == 2:
                print("i == ", i)
                o = [{'type_decl':  {}}] + o
                # val = self.visitBlock(o)
                val = self.visitVarDecl(o, 'float')
                number1 = 2 if val == 'int' else 6
                val += self.visitVarDecl(o, 'vd')
                number2 = 2 if val == 'int' else 6
                sizeBlocks.append(number1)
                sizeBlocks.append(number2)
                print(sizeBlocks)
                # o.pop(0)
            # if i == 3:
            #     val = self.visitVarDecl(o, 'float')
            #     sizeVar += 2 if val == 'int' else 6
            # if i == 4:
            #     val = self.visitVarDecl(o, 'vd')
            #     sizeVar += 2 if val == 'int' else 6
                
        sizeBlocks.sort()
        # print("len(sizeBlocks): ", len(sizeBlocks))
        return sizeVar + (sizeBlocks[len(sizeBlocks) - 1] if len(sizeBlocks) != 0 else 0)
    
    def visitVarDecl(self, o, type_data):
        
        return type_data
    
    def visitTypeDecl(self, o, name, type_data):
        o[0]['type_decl'][name] = type_data
        return type_data
    
    def visitId(self, o, name):
        found = None
        for scope in o:
            if name in scope['type_decl']:
                found = scope['type_decl'][name]
                break
        if not found:
            print("404 not found")
        return found
def maximum(lst):
    from functools import reduce
    return reduce(lambda x, y: x - x + y if y > x else x + 0, lst[1:], lst[0])

class TestFailed(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

def support():
    try:
        main()
    except TestFailed as x:
        print(x)

def main():
    # print("main function")
    # obj = Test()
    # obj.run()
    # print(maximum([3,9,7,-1,-100,100123]))
    # a = 0
    # while (a != 2):
    #     a +=1
        
    # else:
    #     print("haha")
    a = 1
    if a == 1: print("a = 1")
    a +=1
    if a == 2: raise TestFailed('sos')
    
    
main()