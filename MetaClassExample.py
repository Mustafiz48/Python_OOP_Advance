
"""
    This example is an usecase of metaclass. Look at the code, you will understand it. 
"""

class MetaClass(type):
    """
    Initialize a Meta Class and Defining Rules.
    """
    def __init__(cls, name, base, attr):
        """
        Class names should use the CapWords convention. Start each word with a capital letter.
        Do not separate words with underscores. Example: Class, MyClass.
        """
        if cls.__name__[0].isupper():
            """
            Class Method should start with underscore (-) or use a lowercase word or words 
            separating with underscores to improve readability. Example: method, class_method, _method.
            """
            for key, val in attr.items():
                if hasattr(val, '__call__'):
                    if val.__name__[0] == '_' or val.__name__[0].islower():
                        """
                        Each Function should contain Docstring.
                        """
                        if val.__doc__ is None and val.__name__ != '__init__':
                            raise ValueError("Provide Documentation of this Function: {}".format(val.__name__))
                    else:
                        """
                        Function Name starts with Upper case will throw error.
                        """
                        raise ValueError("Function Name should start with Lower case letter: {}".format(val.__name__))
        else:
            raise ValueError("Class Name should use the CapWords convention: {}".format(cls.__name__[0]))