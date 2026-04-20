import customtkinter as ctk
from tkinter import ttk, messagebox
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