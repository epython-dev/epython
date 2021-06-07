import ast


disallowed_nodes = [
    ast.AsyncFor,
    ast.AsyncFunctionDef,
    ast.AsyncWith,
    ast.Delete,
    ast.Raise,
    ast.Try,
    ast.GeneratorExp,
    ast.Await,
    ast.Yield,
    ast.YieldFrom,
    ast.Del,
    ast.ExceptHandler,
    ast.Starred,
    ast.With,
    ast.withitem,
    ast.Interactive,
]


def validate(code):
    for node in ast.walk(code):
        if node.__class__ in disallowed_nodes:
            info = f"Invalid node {node.__class__}"
            if hasattr(node, "lineno"):
                info += f" at line {node.lineno}"
            return ValueError, info
    return None
