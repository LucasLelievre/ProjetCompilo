from http.client import SEE_OTHER
from re import S

class exe :

    def __init__(self):
        self.co = 0
        self.spx = 0
        self.pilex = []
        self.pcode = []

    def exec(self, pcode) :
        print('===== Interpretation de pcode :')
        self.pcode = pcode
        while self.co < len(self.pcode) and pcode[self.co] != 'STOP' :
            self.interprete(self.pcode[self.co])
    
    def interprete(self, x) :
        if x == 'LDA' :
            self.spx += 1
            self.pilex[self.spx] = self.pcode[self.co+1]
            self.co += 2
        if x == 'LDV' :
            self.spx += 1
            self.pilex[self.spx] = self.pilex[self.pcode[self.co+1]]
            self.co += 2
        if x == 'LDC' :
            self.spx += 1
            self.pilex[self.spx] = self.pcode[self.co+1]
            self.co += 2
        if x == 'JMP' :
            self.co = self.co+1
        if x == 'JIF' :
            if(self.pilex[self.pilex] == 0) :
                self.co = self.pcode[self.co]
            else :
                self.co += 2
        if x == 'JSR' :
            pass
        if x == 'RSR' :
            pass
        if x == 'SUP' :
            if (self.pilex[self.spx - 1] > self.pilex[self.spx]):
                self.pilex[self.spx - 1] = True
            else :
                self.pilex[self.spx - 1] = False
            self.spx -= 1
            self.co += 1
        if x == 'SUPE' :
            if (self.pilex[self.spx - 1] >= self.pilex[self.spx]):
                self.pilex[self.spx - 1] = True
            else :
                self.pilex[self.spx - 1] = False
            self.spx -= 1
            self.co += 1
        if x == 'INF' :
            if (self.pilex[self.spx - 1] < self.pilex[self.spx]):
                self.pilex[self.spx - 1] = True
            else :
                self.pilex[self.spx - 1] = False
            self.spx -= 1
            self.co += 1
        if x == 'INFE' :
            if (self.pilex[self.spx - 1] <= self.pilex[self.spx]):
                self.pilex[self.spx - 1] = True
            else :
                self.pilex[self.spx - 1] = False
            self.spx -= 1
            self.co += 1
        if x == 'EG' :
            if (self.pilex[self.spx - 1] == self.pilex[self.spx]):
                self.pilex[self.spx - 1] = True
            else :
                self.pilex[self.spx - 1] = False
            self.spx -= 1
            self.co += 1
        if x == 'DIFF' :
            if (self.pilex[self.spx - 1] != self.pilex[self.spx]):
                self.pilex[self.spx - 1] = True
            else :
                self.pilex[self.spx - 1] = False
            self.spx -= 1
            self.co += 1
        if x == 'RD' :
            y = input()
            print(y)
            self.spx += 1
            self.pilex[self.spx] = y
            self.co += 1
        if x == 'RDLN' :
            y = input()
            print(y)
            self.spx += 1
            self.pilex[self.spx] = y
            self.co += 1
        if x == 'WRT' :
            print(self.pilex[self.spx], end="")
            self.co += 1
        if x == 'WRTLN' :
            print(self.pilex[self.spx])
            self.co += 1
        if x == 'ADD' :
            self.pilex[self.spx-1] = self.pilex[self.spx-1] + self.pilex[self.spx]
            self.spx -= 1
            self.co += 1
        if x == 'MOINS' :
            self.pilex[self.spx-1] = self.pilex[self.spx-1] - self.pilex[self.spx]
            self.spx -= 1
            self.co += 1
        if x == 'DIV' :
            self.pilex[self.spx-1] = self.pilex[self.spx-1] / self.pilex[self.spx]
            self.spx -= 1
            self.co += 1
        if x == 'MULT' :
            self.pilex[self.spx-1] = self.pilex[self.spx-1] * self.pilex[self.spx]
            self.spx -= 1
            self.co += 1
        if x == 'NEG' :
            self.pilex[self.spx] = 0 - self.pilex[self.spx]
            self.co += 1
        if x == 'INC' :
            self.pilex[self.spx] += 1
            self.co += 1
        if x == 'DEC' :
            self.pilex[self.spx] -= 1
            self.co += 1
        if x == 'AND' :
            self.pilex[self.spx] = self.pilex[self.spx] and self.pilex[self.spx]
            self.co += 1
        if x == 'OR' :
            self.pilex[self.spx] = self.pilex[self.spx] or self.pilex[self.spx]
            self.co += 1
        if x == 'NOT' :
            self.pilex[self.spx] = not self.pilex[self.spx]
            self.co += 1
        if x == 'AFF' :
            self.pilex[self.pilex[self.spx -1]] = self.pilex[self.spx]
        if x == 'STOP' :
            pass