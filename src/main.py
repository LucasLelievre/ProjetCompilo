import Forest
import Imprim
import MetaCompilo
import Compilo

def main () :
    # Créé une grammaire avec les 5 règles de la grammaire g0
    meta = MetaCompilo.meta(Forest.GenForest(), "gpl.txt")

    # Scan la GPL
    meta.scanG0()

    # Vérifie la validité des règles
    print("===== la grammaire est-elle correcte ?")
    if not meta.analyseG0(meta.foret['S']) :
        print("NON")
    else :
        print("OUI")

        # Imprime les règles
        Imprim.imprimRegles(meta.foret)

        # Créé un compilateur pour GPL
        compilo = Compilo.compilo(meta.foret, "gpl_prog.txt")

        # Scan la programme
        compilo.scanGPL()
        
        # Vérifie la validité du programme
        print("===== la programme est-il correcte ?")
        gpl_start = list(compilo.foret.keys())[5]
        if not compilo.analyseGPL(compilo.foret[gpl_start]):
            print("NON")
        else :
            print("OUI")

            #afficher pcode
            #executer pcode


main()