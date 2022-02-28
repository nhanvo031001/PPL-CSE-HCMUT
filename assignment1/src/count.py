import ast
class CountFunc(ast.NodeVisitor):
    func_count = 0
    def visit_FunctionDef(self, node):
        self.func_count += 1


p = ast.parse(open("./test/ParserSuite.py").read())
f = CountFunc()
f.visit(p)
print(f.func_count)