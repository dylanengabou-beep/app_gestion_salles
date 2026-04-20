import mysql.connector
import json
from models.salles import salles


class DataSalles:

    def get_connection(self):
        with open("Data/config.json") as f:
            config = json.load(f)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return conn

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type, salle.capacite)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        values = (salle.libelle, salle.type, salle.capacite, salle.code)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM salle WHERE code=%s"
        cursor.execute(query, (code,))

        conn.commit()
        cursor.close()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM salle WHERE code=%s"
        cursor.execute(query, (code,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            return salles(*result)
        return None

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM salle"
        cursor.execute(query)
        results = cursor.fetchall()

        salle = [salles(*row) for row in results]

        cursor.close()
        conn.close()

        return salles