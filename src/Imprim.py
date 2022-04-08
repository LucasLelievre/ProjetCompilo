def imprimArbre (a, buffer = "") :
    # print(buffer, end="")
    if a.classe == 'Conc' :
        print('.')
        print(buffer, '├─ ', end='')
        imprimArbre(a.left, buffer+" │ ")
        print(buffer, '└─ ', end='')
        imprimArbre(a.right, buffer+"   ")
    if a.classe == 'Union' :
        print('+')
        print(buffer, '├─ ', end='')
        imprimArbre(a.left, buffer+" │ ")
        print(buffer, '└─ ', end='')
        imprimArbre(a.right, buffer+"   ")
    if a.classe == 'Star' :
        print('*')
        print(buffer, '└─ ', end='')
        imprimArbre(a.stare, buffer+"   ")
    if a.classe == 'Un' :
        print('Un')
        print(buffer, '└─ ', end='')
        imprimArbre(a.une, buffer+"   ")
    if a.classe == 'Atom' :
        if a.atyp == 'Terminal' :
            print("'", a.nom, "'", sep="")
        else :
            print(a.nom)

def imprimRegles (a) :
    print("===== Règles grammaire")
    for i in a :
        print(i, "\n└─ ", end='')
        imprimArbre(a[i], '  ')