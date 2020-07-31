# epython
EPython is a typed-subset of the Python language useful for extending the language with new builtin types and methods. 

The goal is to be able to write things like NumPy, SciPy, Pandas, bitarray, and any other extension module of Python in this language and get equivalent or better perfomance than writing it using the C-API typically provided. 

This project is in development and extremely alpha.   You should not use this for anything.

Learn more on this talk [Travis Oliphant gave at PyData Austin 2019](https://www.youtube.com/watch?v=Z8vsTxzmorE).


If you are interested in contributing to the design and goals, then join the Discussion at [OpenTeams Slack](https://openteams.com/projects/epython)


# Installation

    pip install epython

# Usage

    epython extmodule.epy --runtime=cpython  
    
Produces a compiled extension module for the given Python runtime.




