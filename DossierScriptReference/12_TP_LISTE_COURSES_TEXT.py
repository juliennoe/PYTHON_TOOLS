
menu = ""
menu_1 = "1: Ajouter un élément"
menu_2 = "2: Enlever un élément"
menu_3 = "3: Afficher la liste"
menu_4 = "4: Vider la liste"
menu_5 = "5: Terminer"



chemin = r"C:\Users\Julien Noé\OneDrive\0_Bureau\Nouveau dossier\liste.txt"

while menu != 5:

    print(f"\n{''}choisissez une option:\n{''}\n{menu_1}\n{menu_2}\n{menu_3}\n{menu_4}\n{menu_5}")
    menu = int(input(""))
    
    if menu == 1:
        element_ajout = input('Entrez le nom de l\'élément à ajouter: ')
        with open(chemin,'a') as f:
            f.write(f"\n{element_ajout}")
            continue
                   
    elif menu == 2:
        element_retirer = input('quel élément souhaitez-vous retirer ? ')
        with open(chemin, 'r') as f:
            lines = f.readlines()
            f.seek(0)
            for element_retirer in lines:
                lines.remove(element_retirer)
        
        with open(chemin, 'w') as f:
             lines.replace(element_retirer,"")
             continue

    elif menu == 3:
        with open(chemin,'r') as f:
            contenu = f.read()
            print(contenu)
   
    elif menu == 4:
            open(chemin,'w').close()
            continue

    else: 
        pass
