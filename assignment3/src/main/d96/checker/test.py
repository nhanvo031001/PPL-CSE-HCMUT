from tokenize import Number


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
    def __init__(self):
        self.global_env = {}
        self.global_env['global'] = {}
        
        
    def __str__(self):
        return "Global env: " + self.global_env
        
def main():
    print("main function")
    obj = Test()
    obj.global_env['global']['Program'] = ComponentClass()
    obj.global_env['global']['Program'].add_attribute('a', 'int')
    obj.global_env['global']['Program'].add_method('function', 'int')
    # print(obj.global_env)
    print(obj.global_env['global']['Program'])
    temp = obj.global_env['global']['Program'].lookup_attribute('a')
    temp = 'float'
    print(obj.global_env['global']['Program'])
    
main()