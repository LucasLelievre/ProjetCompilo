class Conc :
    def __init__(self, left, right):
        self.classe = 'Conc'
        self.left = left
        self.right = right

class Union :
    def __init__(self, left, right):
        self.classe = 'Union'
        self.left = left
        self.right = right

class Star :
    def __init__(self, stare):
        self.classe = 'Star'
        self.stare = stare

class Un :
    def __init__(self, une):
        self.classe = 'Un'
        self.une = une

class Atom :
    def __init__(self, val, action, atyp):
        self.classe = 'Atom'
        self.nom = val
        self.act = action
        self.atyp = atyp
        if atyp == 'NonTerminal' or val == 'IDNTER' :
            self.cod = 'IDNTER'
        else :
            self.cod = 'ELTER'

def GenConc (p1, p2) :
    return Conc(p1, p2)

def GenUnion (p1, p2) :
    return Union(p1, p2)

def GenStar (p) :
    return Star(p)

def GenUn (p) :
    return Un(p)

def GenAtom (val, action, atyp) :
    return Atom(val, action, atyp)

def GenForest () :
    return {
        'S': GenConc(
                GenStar(
                    GenConc(
                        GenConc(
                            GenConc(
                                GenAtom('N', 0, 'NonTerminal'),
                                GenAtom('->', 0, 'Terminal')
                            ),
                            GenAtom('E', 0, 'NonTerminal')
                        ),
                        GenAtom(',', 1, 'Terminal')
                    )
                ),
                GenAtom(';', 0, 'Terminal')
            ),
        'N' : GenAtom('IDNTER', 2, 'Terminal'),
        'E' : GenConc(
                GenAtom('T', 0, 'NonTerminal'),
                GenStar(
                    GenConc(
                        GenAtom('+', 0, 'Terminal'),
                        GenAtom('T', 3, 'NonTerminal')
                    )
                )
        ),
        'T' : GenConc(
                GenAtom('F', 0, 'NonTerminal'),
                GenStar(
                    GenConc(
                        GenAtom('.', 0, 'Terminal'),
                        GenAtom('F', 4, 'NonTerminal')
                    )
                )
        ),
        'F' : GenUnion(
                GenAtom('IDNTER', 5, 'Terminal'),
                GenUnion(
                    GenAtom('ELTER', 5, 'Terminal'),
                    GenUnion(
                        GenConc(
                            GenConc(
                                GenAtom('(', 0, 'Terminal'),
                                GenAtom('E', 0, 'NonTerminal')
                            ),
                            GenAtom(')', 0, 'Terminal')
                        ),
                        GenUnion(
                            GenConc(
                                GenConc(
                                    GenAtom('[', 0, 'Terminal'),
                                    GenAtom('E', 0, 'NonTerminal')
                                ),
                                GenAtom(']', 6, 'Terminal')
                            ),
                            GenConc(
                                GenConc(
                                    GenAtom('(/', 0, 'Terminal'),
                                    GenAtom('E', 0, 'NonTerminal')
                                ),
                                GenAtom('/)', 7, 'Terminal')
                            )
                        )
                    )
                )
            )
    }