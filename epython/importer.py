"""
Importing this module allows import .epy files like .py files.

The main reason for naming epython files with the .epy file extension is to
avoid confusion with regular Python modules.  A package may contain a number
of (sub-) modules of which only some are epython extensions.

For development of epython packages, it is nevertheless very useful to import
.epy files just like .pt files, which is possible by simply importing epython
first.  E.g.

    import epython
    import myext    # will import myext.epy

Without importing epython first, myext will not work, which helps to avoid
using epython extensions as pure Python modules (which will be quite slow).
"""
import sys
import imp
from os.path import isfile, join


class EPY_Importer(object):

    def find_module(self, fullname, path=None):
        name = fullname.rsplit('.', 1)[-1]
        for dir_path in path or sys.path:
            self.path = join(dir_path, name + '.epy')
            if isfile(self.path):
                self.modtype = imp.PY_SOURCE
                return self
        return None

    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.modules[fullname]

        mod = imp.new_module(fullname)
        mod.__file__ = self.path
        mod.__loader__ = self
        with open(self.path, 'rb') as fi:
            code = fi.read()

        exec(code, mod.__dict__)
        sys.modules[fullname] = mod
        return mod


sys.meta_path.append(EPY_Importer())
