def imprimArbre (arbre, buffer = "") :
    if arbre.classe == 'Conc' :
        print('.')
        print(buffer, '├─ ', end='')
        imprimArbre(arbre.left, buffer+" │ ")
        print(buffer, '└─ ', end='')
        imprimArbre(arbre.right, buffer+"   ")
    if arbre.classe == 'Union' :
        print('+')
        print(buffer, '├─ ', end='')
        imprimArbre(arbre.left, buffer+" │ ")
        print(buffer, '└─ ', end='')
        imprimArbre(arbre.right, buffer+"   ")
    if arbre.classe == 'Star' :
        print('*')
        print(buffer, '└─ ', end='')
        imprimArbre(arbre.stare, buffer+"   ")
    if arbre.classe == 'Un' :
        print('Un')
        print(buffer, '└─ ', end='')
        imprimArbre(arbre.une, buffer+"   ")
    if arbre.classe == 'Atom' :
        if arbre.atyp == 'Terminal' :
            print("'", arbre.nom, "'", sep="")
        else :
            print(arbre.nom)

def imprimRegles (foret) :
    print("===== Règles grammaire")
    for i in foret :
        print(i, "\n└─ ", end='')
        imprimArbre(foret[i], '  ')