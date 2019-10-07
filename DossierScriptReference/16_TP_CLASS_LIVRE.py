
class Livre:
    
    def __init__(self, nom, nombre_de_pages,prix):
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix
    
livre_01 = Livre("Harry Potter", 300, 10.99)
livre_02 = Livre("Le seigneur des Anneaux", 400, 13.99)

print(livre_01.nom,livre_01.prix,livre_01.nombre_de_pages)
print(livre_02.nom, livre_02.prix, livre_02.nombre_de_pages)


