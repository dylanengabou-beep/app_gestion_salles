from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Test connexion
try:
    conn = dao.get_connection()
    print("Connexion réussie")
    conn.close()
except:
    print("Erreur de connexion")

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

from views.view_salle import ViewSalle

app = ViewSalle()
app.mainloop()

from views.view_salle import ViewSalle

app = ViewSalle()
app.mainloop()