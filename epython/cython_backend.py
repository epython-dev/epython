from astor import SourceGenerator

# For the Cython generator we re-use the astor code generator
# and generate Cython code instead for nodes that have type information
class CythonGenerator(SourceGenerator):
    
    pass