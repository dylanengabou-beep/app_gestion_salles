import customtkinter as ctk
from tkinter import ttk, messagebox

import self

from models.salle import Salle
from services.services_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des salles")
        self.resizable(False, False)
        self.service_salle = ServiceSalle()

        # Cadre A : Informations Salle
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.cadreInfo, text="Code :").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_code = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Libellé :").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Type :").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_type = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_type.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Capacité :").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=5)

        # Cadre B : Actions
        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=5, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.cadreActions, text="Ajouter")
        self.btn_ajouter.pack(side="left", padx=10, pady=8)

        self.btn_modifier = ctk.CTkButton(self.cadreActions, text="Modifier")
        self.btn_modifier.pack(side="left", padx=10, pady=8)

        self.btn_supprimer = ctk.CTkButton(self.cadreActions, text="Supprimer")
        self.btn_supprimer.pack(side="left", padx=10, pady=8)

        self.btn_rechercher = ctk.CTkButton(self.cadreActions, text="Rechercher")
        self.btn_rechercher.pack(side="left", padx=10, pady=8)

        def ajouter_salle(self):
            salle = Salle(
                self.entry_code.get(),
                self.entry_libelle.get(),
                self.entry_type.get(),
                self.entry_capacite.get()
            )
            ok, msg = self.service_salle.ajouter_salle(salle)
            messagebox.showinfo("Info", msg) if ok else messagebox.showerror("Erreur", msg)
            self.lister_salles()

    # Associer le bouton
    self.btn_ajouter.configure(command=self.ajouter_salle)

    def modifier_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            self.entry_capacite.get()
        )
        ok, msg = self.service_salle.modifier_salle(salle)
        messagebox.showinfo("Info", msg) if ok else messagebox.showerror("Erreur", msg)
        self.lister_salles()


# Associer le bouton
self.btn_modifier.configure(command=self.modifier_salle)


def supprimer_salle(self):
    code = self.entry_code.get()
    self.service_salle.supprimer_salle(code)
    messagebox.showinfo("Info", f"Salle '{code}' supprimée.")
    self.lister_salles()


# Associer le bouton
self.btn_supprimer.configure(command=self.supprimer_salle)


def rechercher_salle(self):
    code = self.entry_code.get()
    salle = self.service_salle.rechercher_salle(code)
    if salle:
        self.entry_code.delete(0, "end");
        self.entry_code.insert(0, salle.code)
        self.entry_libelle.delete(0, "end");
        self.entry_libelle.insert(0, salle.libelle)
        self.entry_type.delete(0, "end");
        self.entry_type.insert(0, salle.type)
        self.entry_capacite.delete(0, "end");
        self.entry_capacite.insert(0, salle.capacite)
    else:
        messagebox.showwarning("Introuvable", f"Aucune salle avec le code '{code}'.")


# Associer le bouton
self.btn_rechercher.configure(command=self.rechercher_salle)

