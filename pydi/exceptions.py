import types


class PydiError(Exception):
    pass


class InitializationFailed(PydiError):
    def __init__(self, target, target_args=None, target_kwargs=None):
        self.target_name = target.__name__
        self.target_args = target_args
        self.target_kwargs = target_kwargs

        target_type = type(target)

        if target_type == types.TypeType:
            self.target_code = target.__init__.__code__
        else:
            self.target_code = target.__code__

    def __str__(self):
        return "Failed to call %s. Allowed arguments (%i) are %s but was provided %i positional args: %s and %i keyword args: %s" % \
                    (self.target_name,
                     len(self.target_code.co_varnames),
                     self.target_code.co_varnames,
                     len(self.target_args),
                     self.target_args,
                     len(self.target_kwargs),
                     self.target_kwargs)
