"""
EPython is a code-transformer that translates a statically typed subset of
Python syntax into an extension of Python for a particular backend.

The .epy file is first compiled into an AST
The AST is validated to ensure it uses only the allowed subset of Python
The AST is then fed to a transformer specific to the backend.

"""
import argparse
import ast

# See https://greentreesnakes.readthedocs.io/en/latest/nodes.html

disallowed_nodes = [ast.AsyncFor, ast.AsyncFunctionDef, 
            ast.AsyncWith, ast.Delete, ast.Raise, ast.Try,
            ast.GeneratorExp, ast.Await, ast.Yield, ast.YieldFrom, 
            ast.Del, ast.ExceptHandler, ast.Starred, ast.ListComp,
            ast.SetComp, ast.DictComp, ast.comprehension,
            ast.Try, #ast.TryFinally, ast.TryExcept, 
            ast.With, ast.withitem, ast.Interactive]

def validate(code):
    for node in ast.walk(code):
        if node.__class__ in disallowed_nodes:
            err = ValueError
            info = f"Invalid node {node.__class__}"
            if hasattr(node, "lineno"):
                info += f" at line {node.lineno}"
            return err, info
    return None

def main():
    parser = argparse.ArgumentParser(prog='epython', 
            description="Compile statically typed subset of Python to a backend.")

    parser.add_argument("file")
    parser.add_argument("--backend", default="cpython")

    args = parser.parse_args()

    with open(args.file) as myfile:
        source = myfile.read()

    code = compile(source, args.file, 'exec', flags=ast.PyCF_ONLY_AST)

    result = validate(code)

    if result is not None:
        raise result[0](result[1])

    return code

if __name__ == "__main__":
    code = main()