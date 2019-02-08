class Clazz:
    def __init__(self, args="default"):
        """
            constructor of a clazz instance
            parameters may have a default value
        """
        print("__init__ called")
        self.args = args

    def __str__(self):
        """ use str to receive a human readible string for this instance """
        print("__str__ called")
        return self.args

    def __repr__(self):
        """
            use repr to receive an unambigious representations,
            e.g. for debugging
        """
        print("__repr__ called")
        return "Clazz("+self.args+")"

    def __eq__(self, other):
        """equals"""
        print("__eq__ called")
        return self.args == other.args

    def __ne__(self, other):
        """not equals
            as eq and ne do not necessarily return booleans it may be wise to
            define the respective opposite rather than returning a boolean
            negation
            see https://stackoverflow.com/a/9455214/10761360
        """
        print("__ne__ called")
        return not self == other

    def __len__(self):
        """
            returns the length of this object
            usually invoked by giving an instance of string or list
            to the function 'len', e.g. len('12345') => 5
        """
        print("__len__ called")
        return len(self.args)


def printAndExecute(operation):
    """ prints and executes the given operation"""
    print("### print({0}) ###".format(operation))
    print(str(eval(operation))+"\n")


print()
print("### x = Clazz('value') ###")
x = Clazz('value')
print()
printAndExecute("x")
printAndExecute("x == x")
printAndExecute("x != x")
printAndExecute("Clazz()")
printAndExecute("len(x)")
