import Forest

class meta :

    def __init__(self, foret, file) :
        self.foret = foret
        self.pileAction = []
        self.ops = ['->', '+', '.', '*', '[', ']', '(', ')', '(/', '/)', ',', ';']
        self.lastScan = {}
        self.gram = ""
        self.pos = 0

        print("===== Scan fichier grammaire", file)
        f = open(file, "r")
        lines = f.readlines()
        f.close()
        for i in range(len(lines)) :
            self.gram += lines[i].strip()
        print(self.gram)

    def scanG0 (self) :
        output = { "code": 'null', "act": 'null', "type": 'null', "nom": 'null' }
        # Rule name
        if (self.pos == 0 or self.gram[self.pos-1] == ',') and self.gram[self.pos] not in self.ops :
            rest = self.gram[self.pos:]
            end = rest.find("->")
            output["code"] = 'IDNTER'
            output["type"] = 'NonTerminal'
            output["nom"] = rest[:end]
            self.pos += end
        
        # operations de taille 2 -> (/ /)
        elif self.gram[self.pos:self.pos+2] in self.ops :
            output["code"] = 'OPERATION'
            output["type"] = 'Terminal'
            output["nom"] = self.gram[self.pos:self.pos+2]
            self.pos += 2

        # operations de taille 1
        elif self.gram[self.pos] in self.ops :
            output["code"] = 'OPERATION'
            output["type"] = 'Terminal'
            output["nom"] = self.gram[self.pos]
            self.pos += 1

        # elements terminaux
        elif self.gram[self.pos] == "'" :
            rest = self.gram[self.pos+1:]
            end = rest.find("'")
            output["code"] = 'ELTER'
            output["type"] = 'Terminal'
            output["nom"] = rest[:end]
            self.pos += end + 2
        
        # identifiants non terminaux
        else :
            for i in range(self.pos, len(self.gram)) :
                # print(self.gram[i], self.gram[i:i+2])
                if self.gram[i] in self.ops or self.gram[i:i+2] in self.ops :
                    output["code"] = 'IDNTER'
                    output["type"] = 'NonTerminal'
                    output["nom"] = self.gram[self.pos:i]
                    self.pos += i - self.pos
                    break
        
        # Detection de l'action
        if '#' in output['nom'] :
            hash = output['nom'].find('#')
            output['act'] = output['nom'][hash+1:]
            output['nom'] = output['nom'][:hash]
        else :
            output['act'] = 0

        self.lastScan = output
    
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
                    if self.lastScan['nom'] != ';' or self.lastScan['code'] != 'OPERATION':
                        self.scanG0()
                    return True
                else :
                    return False
            else :
                if self.analyseG0(self.foret[p.nom]) :
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
            self.foret[t2.nom] = t1
        if act == 2 :
            self.pileAction.append(Forest.GenAtom(self.lastScan["nom"], self.lastScan['act'], self.lastScan["type"]))
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
                self.pileAction.append(Forest.GenAtom(self.lastScan["nom"], self.lastScan['act'], 'Terminal'))
            else :
                self.pileAction.append(Forest.GenAtom(self.lastScan["nom"], self.lastScan['act'], 'NonTerminal'))
        if act == 6 :
            t1 = self.pileAction.pop()
            self.pileAction.append(Forest.GenStar(t1))
        if act == 7 :
            t1 = self.pileAction.pop()
            self.pileAction.append(Forest.GenUn(t1))