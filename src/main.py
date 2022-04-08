import Forest
import Imprim
import MetaCompilo

def main () :
    # Créé une grammaire
    meta = MetaCompilo.meta("gpl.txt")
    # Génère les 5 règles de la grammaire g0
    meta.a = Forest.GenForest()

    # Scan la GPL
    meta.scanG0()


    # Vérifie la validité des règles
    print("===== la grammaire est-elle correcte ?")
    if meta.analyseG0(meta.a['S']) :
        print('OK')
    else :
        print('NOT OK')

    # Imprime les règles
    Imprim.imprimRegles(meta.a)



main()