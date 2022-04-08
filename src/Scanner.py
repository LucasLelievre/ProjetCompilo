class Scanner :

    ops = ['->', '+', '.', '*', '[', ']', '(', ')', '(/', '/)', ',', ';']

    def __init__(self, file) :
        print("===== Scan grammaire", file)
        f = open(file, "r")
        lines = f.readlines()
        self.regles = ""
        for i in range(len(lines)) :
            self.regles += lines[i].strip()
        print(self.regles)
        self.pos = 0
    
    def scan(self) :
        output = { "code": 'null', "act": 'null', "type": 'null', "nom": 'null' }

        # Rule name
        if (self.pos == 0 or self.regles[self.pos-1] == ',') and self.regles[self.pos] not in self.ops :
            rest = self.regles[self.pos:]
            end = rest.find("->")
            output["code"] = 'IDNTER'
            output["act"] = 2
            output["type"] = 'NonTerminal'
            output["nom"] = rest[:end]
            self.pos += end
        
        # operations de taille 2 -> (/ /)
        elif self.regles[self.pos:self.pos+2] in self.ops :
            output["code"] = 'OPERATION'
            output["act"] = 0
            output["type"] = 'Terminal'
            output["nom"] = self.regles[self.pos:self.pos+2]
            if output["nom"] == '/)' :
                output["act"] = 7
            self.pos += 2

        # operations de taille 1
        elif self.regles[self.pos] in self.ops :
            output["code"] = 'OPERATION'
            output["act"] = 0
            output["type"] = 'Terminal'
            output["nom"] = self.regles[self.pos]
            if output["nom"] == ']' :
                output["act"] = 6
            if output["nom"] == ',' :
                output["act"] = 1
            self.pos += 1

        # elements terminaux
        elif self.regles[self.pos] == "'" :
            rest = self.regles[self.pos+1:]
            end = rest.find("'")
            output["code"] = 'ELTER'
            output["act"] = 5
            output["type"] = 'Terminal'
            output["nom"] = rest[:end]
            self.pos += end + 2
        
        # identifiants non terminaux
        else :
            for i in range(self.pos, len(self.regles)) :
                if self.regles[i] in self.ops :
                    output["code"] = 'IDNTER'
                    output["act"] = 5
                    output["type"] = 'NonTerminal'
                    output["nom"] = self.regles[self.pos:i]
                    self.pos += i - self.pos
                    break
        
        return output