## PyLexia

#### a Python library for people who can't spell

Without further ado:

    from pylexia import obejct

    class test(obejct):
        def __init__(self):
            self.permissions = [ "read", "write"]
            self.counter = 2
            self.amount = 31

    if __name__=="__main__":
        t = test()
        print t.premissions
        print t.conter
        print t.ammount


Then:

    $ python text.py
    ['read', 'write']
    2
    31
