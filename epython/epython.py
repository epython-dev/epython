"""
EPython is a code-transformer that translates a statically typed subset of
Python syntax into an extension of Python for a particular backend.

The .epy file is first compiled into an AST
The AST is validated to ensure it uses only the allowed subset of Python
The AST is then fed to a transformer specific to the backend.

"""
import argparse
import ast
import os.path

# See https://greentreesnakes.readthedocs.io/en/latest/nodes.html

_registry = {}

disallowed_nodes = [ast.AsyncFor, ast.AsyncFunctionDef, 
            ast.AsyncWith, ast.Delete, ast.Raise, ast.Try,
            ast.GeneratorExp, ast.Await, ast.Yield, ast.YieldFrom, 
            ast.Del, ast.ExceptHandler, ast.Starred, ast.ListComp,
            ast.SetComp, ast.DictComp, ast.comprehension,
            ast.Try, #ast.TryFinally, ast.TryExcept, 
            ast.With, ast.withitem, ast.Interactive]

def register_func(name_or_func):
    if isinstance(name_or_func, str):
        name = name_or_func
        func = None
    else:
        func = name_or_func
        name = func.__name__
    if func is None:
        def decorator(new_func):
            _registry[name] = new_func
            return new_func
        return decorator
    else:
        _registry[name] = func
        return func

# A transformation function needs to take as agruments
#  ast: the validated ast of the code 
#  filename: the name to generate the artefacts
#
# It returns the PATH (or URL) of the created artefact

@register_func('cpython')
def transform(ast, name):
    return name + '.so'

# @register_func
# def pypy(mine):
#     return mine       

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
    parser.add_argument("--name", default="none")
    args = parser.parse_args()

    if args.name == 'none':
        name = os.path.splitext(args.file)[0]
    else:
        name = args.name

    with open(args.file) as myfile:
        source = myfile.read()
 
    code = compile(source, name, 'exec', flags=ast.PyCF_ONLY_AST)
    result = validate(code)
    if result is not None:
        raise result[0](result[1])

    try:
        transformer = _registry[args.backend]
    except KeyError:
        raise RuntimeError(f"There is no epython backend registered for {args.backend}.")

    ouput = transformer(code, name)

    return code

# importing the backend should be sufficient to call the decorator 
# that registers the function.
def find_backends():
    import importlib
    import pkgutil

    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg in pkgutil.iter_modules()
                if name.startswith('epython-')
    }

    
if __name__ == "__main__":
    find_backends()
    code = main()