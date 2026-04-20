import json
import mysql.connector
from models.salle import Salle

class DataSalle:
    def get_connection(self):
        with open("data/config.json", "r") as f:
            config = json.load(f)
        return mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)",
            (salle.code, salle.libelle, salle.type, salle.capacite)
        )
        conn.commit()
        cursor.close()
        conn.close()

        def update_salle(self, salle):
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s",
                (salle.libelle, salle.type, salle.capacite, salle.code)
            )
            conn.commit()
            cursor.close()
            conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM salle WHERE code=%s", (code,))
        conn.commit()
        cursor.close()
        conn.close()

        def get_salle(self, code):
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM salle WHERE code=%s", (code,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            if row:
                return Salle(row[0], row[1], row[2], row[3])
            return None

        def get_salles(self):
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM salle")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return [Salle(r[0], r[1], r[2], r[3]) for r in rows]
