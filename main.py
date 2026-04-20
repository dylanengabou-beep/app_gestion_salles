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

from views.view_salle import Viewsalle

app = Viewsalle()
app.mainloop()

from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Test connexion
conn = dao.get_connection()
print("Connexion réussie :", conn.is_connected())
conn.close()

# Test insert
s1 = Salle("A01", "Al-Khwârizmî", "Amphie", 250)
dao.insert_salle(s1)
print("Salle ajoutée.")

# Test get_salle
s = dao.get_salle("A01")
s.afficher_infos()

# Test update
s1.libelle = "Salle Modifiée"
dao.update_salle(s1)
print("Salle modifiée.")

# Test get_salles
salles = dao.get_salles()
for salle in salles:
    salle.afficher_infos()

# Test delete
dao.delete_salle("A01")
print("Salle supprimée.")

from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

# Ajouter
ok, msg = service.ajouter_salle(Salle("B01", "Réseaux", "Laboratoire", 16))
print(msg)

# Lister
for s in service.recuperer_salles():
    s.afficher_infos()

# Modifier
ok, msg = service.modifier_salle(Salle("B01", "Réseaux Avancés", "Laboratoire", 20))
print(msg)

# Rechercher
s = service.rechercher_salle("B01")
if s: s.afficher_infos()

# Supprimer
service.supprimer_salle("B01")
print("Supprimé.")

from views.view_salle import ViewSalle

app = ViewSalle()
app.mainloop()