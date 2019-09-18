
class Employe():
	def __init__(self, id = 0, prenom ='inconnu',nomDeFamille ='inconnu'):
		self.id = id
		self.prenom = prenom
		self.nomDeFamille = nomDeFamille

	def ModifId(self, nouveauId=0):
		self.id = nouveauId


julie = Employe(id=0,prenom ="julie",nomDeFamille ="haubert")

print(julie.id)

julie.ModifId(nouveauId = 4)

print(julie.id)