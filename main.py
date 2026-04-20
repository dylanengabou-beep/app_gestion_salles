from models.salles import Salle
S1 = Salle("A345", "salle informatique", "laboratoire", 30)
S1.afficher_infos()

from Data.dao_salles import DataSalles
from models.salles import salle

dao = DataSalles()

# Test connexion
try:
    conn = dao.get_connection()
    print("Connexion réussie")
    conn.close()
except Exception as e:
    print("Erreur de connexion:", e)

# Ajouter une salle
s1 = Salle("B101", "Salle test", "Classe", 25)
dao.insert_salle(s1)

# Modifier la salle
s1.libelle = "Salle modifiée"
dao.update_salle(s1)

# Rechercher une salle
salle = dao.get_salle("B101")
if salle:
    salle.afficher_infos()

# Afficher toutes les salles
salles = dao.get_salles()
for s in salles:
    s.afficher_infos()

# Supprimer la salle
dao.delete_salle("B101")