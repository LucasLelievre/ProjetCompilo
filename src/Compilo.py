
class compilo :

    def __init__(self, foret, file) :
        self.lastScan = {}
        self.foret = foret
        self.prog = ""
        self.pos = 0
        self.line = 0

        print("===== Scan Programme")
        f = open(file, "r")
        lines = f.readlines()
        f.close()
        for l in lines :
            self.prog += l
        print(self.prog)

        
    def scanGPL(self) :
        output = { "code": 'null', "type": 'null', "nom": 'null' }
        
        # Scan d'un element
        elem = ""
        while self.pos < len(self.prog) and self.prog[self.pos] not in [' ', '\n']:
            elem += self.prog[self.pos]
            self.pos+=1
        self.pos+=1
        output['nom'] = elem
        self.lastScan = output
    
    def analyseGPL(self, p):
        if p.classe == 'Conc' :
            if self.analyseGPL(p.left) :
                return self.analyseGPL(p.right)
            else :
                return False
        if p.classe == 'Union' :
            if self.analyseGPL(p.left) :
                return True
            else :
                return self.analyseGPL(p.right)
        if p.classe == 'Star' :
            while self.analyseGPL(p.stare) :
                pass
            return True
        if p.classe == 'Un' :
            self.analyseGPL(p.une)
            return True
        if p.classe == 'Atom' :
            if p.atyp == 'Terminal' :
                # print(p.nom, self.lastScan['nom'], self.lastScan['code'])
                if p.nom == self.lastScan['nom'] or (p.nom == self.lastScan['code']) :
                    if p.act != 0 :
                        self.actionGPL(p.act)
                    if self.lastScan['nom'] != ';':
                        self.scanGPL()
                    return True
                else :
                    return False
            else :
                if self.analyseGPL(self.foret[p.nom]) :
                    # print('idnter :', p.nom)
                    if p.act != 0 :
                        self.actionGPL(p.act)
                    return True
                else :
                    return False
        return False


    def actionGPL(self, act):
        pass
    