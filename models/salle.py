class Salle:
    def __init__(self, code, libelle, type, capacite):
        self.code = code
        self.libelle = libelle
        self.type = type
        self.capacite = capacite

    def afficher_infos(self):
        print(f"Code :, {self.code}")
        print("Libellé :, {self.libelle}")
        print("Type :, {self.type}")
        print("Capacité :, {self.capacite}")
