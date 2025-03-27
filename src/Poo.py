class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant > self.solde:
            print("Imposible de retirer")
        else:
            self.solde -= montant

    def afficher_sold(self):
        print(self.solde)
