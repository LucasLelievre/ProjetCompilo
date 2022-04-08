import Forest
import Imprim
import Grammaire0

def main () :
    # Créé une grammaire
    gram = Grammaire0.g0("gpl.txt")
    # Génère les 5 règles de la grammaire g0
    gram.a = Forest.GenForest()

    # Scan la GPL
    gram.scanG0()


    # Vérifie la validité des règles
    print("===== la grammaire est-elle correcte ?")
    if gram.analyseG0(gram.a['S']) :
        print('OK')
    else :
        print('NOT OK')

    # Imprime les règles
    Imprim.imprimRegles(gram.a)



main()