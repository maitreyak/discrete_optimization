# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_MiniSat', [dirname(__file__)])
        except ImportError:
            import _MiniSat
            return _MiniSat
        if fp is not None:
            try:
                _mod = imp.load_module('_MiniSat', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _MiniSat = swig_import_helper()
    del swig_import_helper
else:
    import _MiniSat
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


import SatWrapper
class MiniSatSolver(SatWrapper.SatWrapperSolver):
    __swig_setmethods__ = {}
    for _s in [SatWrapper.SatWrapperSolver]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MiniSatSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [SatWrapper.SatWrapperSolver]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, MiniSatSolver, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _MiniSat.new_MiniSatSolver()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _MiniSat.delete_MiniSatSolver
    __del__ = lambda self : None;
    def create_atom(self, *args): return _MiniSat.MiniSatSolver_create_atom(self, *args)
    def validate(self): return _MiniSat.MiniSatSolver_validate(self)
    def truth_value(self, *args): return _MiniSat.MiniSatSolver_truth_value(self, *args)
    def solve(self): return _MiniSat.MiniSatSolver_solve(self)
    def solveAndRestart(self, *args): return _MiniSat.MiniSatSolver_solveAndRestart(self, *args)
    def reset(self, *args): return _MiniSat.MiniSatSolver_reset(self, *args)
    def propagate(self): return _MiniSat.MiniSatSolver_propagate(self)
    def save(self): return _MiniSat.MiniSatSolver_save(self)
    def post(self, *args): return _MiniSat.MiniSatSolver_post(self, *args)
    def undo(self, *args): return _MiniSat.MiniSatSolver_undo(self, *args)
    def deduce(self): return _MiniSat.MiniSatSolver_deduce(self)
    def branch_right(self): return _MiniSat.MiniSatSolver_branch_right(self)
    def store_solution(self): return _MiniSat.MiniSatSolver_store_solution(self)
    def setFailureLimit(self, *args): return _MiniSat.MiniSatSolver_setFailureLimit(self, *args)
    def setNodeLimit(self, *args): return _MiniSat.MiniSatSolver_setNodeLimit(self, *args)
    def setTimeLimit(self, *args): return _MiniSat.MiniSatSolver_setTimeLimit(self, *args)
    def setVerbosity(self, *args): return _MiniSat.MiniSatSolver_setVerbosity(self, *args)
    def setRandomized(self, *args): return _MiniSat.MiniSatSolver_setRandomized(self, *args)
    def setRandomSeed(self, *args): return _MiniSat.MiniSatSolver_setRandomSeed(self, *args)
    def is_sat(self): return _MiniSat.MiniSatSolver_is_sat(self)
    def is_opt(self): return _MiniSat.MiniSatSolver_is_opt(self)
    def is_unsat(self): return _MiniSat.MiniSatSolver_is_unsat(self)
    def printStatistics(self): return _MiniSat.MiniSatSolver_printStatistics(self)
    def getBacktracks(self): return _MiniSat.MiniSatSolver_getBacktracks(self)
    def getNodes(self): return _MiniSat.MiniSatSolver_getNodes(self)
    def getFailures(self): return _MiniSat.MiniSatSolver_getFailures(self)
    def getPropags(self): return _MiniSat.MiniSatSolver_getPropags(self)
    def getTime(self): return _MiniSat.MiniSatSolver_getTime(self)
MiniSatSolver_swigregister = _MiniSat.MiniSatSolver_swigregister
MiniSatSolver_swigregister(MiniSatSolver)




    
import Numberjack

class Solver(Numberjack.NBJ_STD_Solver):
    def __init__(self, model=None, X=None, FD=False, clause_limit=-1):
        Numberjack.NBJ_STD_Solver.__init__(self, "MiniSat", "SatWrapper", model, X, FD,
            clause_limit)
    
                