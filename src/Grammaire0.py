import Forest
from Imprim import imprimArbre
import Scanner

class g0 :

    def __init__(self, file) :
        self.a = {}

        self.scanner = Scanner.Scanner(file)
        self.lastScan = {}

        self.pileAction = []
        self.dicoT = {}
        self.dicoNT = {}

    def scanG0 (self) :
        self.lastScan = self.scanner.scan()
        # print("scan  :\t", self.lastScan['nom'], self.lastScan['code'], self.lastScan['act'], self.lastScan['type'])
    
    def analyseG0 (self, p) :
        if p.classe == 'Conc' :
            if self.analyseG0(p.left) :
                return self.analyseG0(p.right)
            else :
                return False
        if p.classe == 'Union' :
            if self.analyseG0(p.left) :
                return True
            else :
                return self.analyseG0(p.right)
        if p.classe == 'Star' :
            while self.analyseG0(p.stare) :
                pass
            return True
        if p.classe == 'Un' :
            self.analyseG0(p.une)
            return True
        if p.classe == 'Atom' :
            if p.atyp == 'Terminal' :
                if p.nom == self.lastScan['nom'] or (p.nom == self.lastScan['code']) :
                    if p.act != 0 :
                        self.actionG0(p.act)
                    if self.lastScan['nom'] != ';':
                        self.scanG0()
                    return True
                else :
                    return False
            else :
                if self.analyseG0(self.a[p.nom]) :
                    if p.act != 0 :
                        self.actionG0(p.act)
                    return True
                else :
                    return False
        return False
        
        
    def actionG0 (self, act) :
        if act == 1 :
            t1 = self.pileAction.pop()
            t2 = self.pileAction.pop()
            self.a[t2.nom] = t1
        if act == 2 :
            self.pileAction.append(Forest.GenAtom(self.lastScan["nom"], act, self.lastScan["type"])) #TODO what is DICONT
        if act == 3 :
            t1 = self.pileAction.pop()
            t2 = self.pileAction.pop()
            self.pileAction.append(Forest.GenUnion(t2, t1))
        if act == 4 :
            t1 = self.pileAction.pop()
            t2 = self.pileAction.pop()
            self.pileAction.append(Forest.GenConc(t2, t1))
        if act == 5 :
            if self.lastScan["type"] == 'Terminal' :
                self.pileAction.append(Forest.GenAtom(self.lastScan["nom"], act, 'Terminal'))
            else :
                self.pileAction.append(Forest.GenAtom(self.lastScan["nom"], act, 'NonTerminal'))
        if act == 6 :
            t1 = self.pileAction.pop()
            self.pileAction.append(Forest.GenStar(t1))
        if act == 7 :
            t1 = self.pileAction.pop()
            self.pileAction.append(Forest.GenUn(t1))        
