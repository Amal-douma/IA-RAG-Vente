import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime

def load_to_mysql():
    connection = None
    cursor = None

    try:
        # Connexion à MySQL via le nom du service Docker
        connection = mysql.connector.connect(
            host="mysql",
            port=3306,
            user="appuser",
            password="appuserpassword"
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce_db")
        cursor.close()
        connection.close()

        # Reconnecter à la base créée
        connection = mysql.connector.connect(
            host="mysql",
            port=3306,
            user="appuser",
            password="appuserpassword",
            database="ecommerce_db"
        )

        cursor = connection.cursor()
        print("✅ Connexion réussie à la base de données.")

        # Charger le fichier Excel (chemin absolu dans le conteneur)
        file_path = "/app/data/bd.xlsx"  # Chemin absolu basé sur le WORKDIR /app
        if not os.path.exists(file_path):
            print(f"❌ Fichier {file_path} introuvable.")
            return
        df = pd.read_excel(file_path)

        # Debugging: Afficher les colonnes pour vérifier
        print("Colonnes du DataFrame:", df.columns.tolist())

        # Créer la table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS ventes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            produit VARCHAR(255),
            quantite INT,
            prix DECIMAL(10, 2),
            date_vente DATE
        )
        """
        cursor.execute(create_table_query)

        # Insérer les données
        for _, row in df.iterrows():
            try:
                produit = row['Désignation'] if pd.notnull(row['Désignation']) else 'Unknown'
                quantite = int(row['Quantité']) if pd.notnull(row['Quantité']) else 0
                prix = float(row['Prix Unit HT']) if pd.notnull(row['Prix Unit HT']) else 0.0
                date_vente = row['Date'] if pd.notnull(row['Date']) else None

                if isinstance(date_vente, str):
                    date_vente = datetime.strptime(date_vente, '%Y-%m-%d').date()
                elif not isinstance(date_vente, (datetime, type(None))):
                    date_vente = None

                sql = """
                INSERT INTO ventes (produit, quantite, prix, date_vente)
                VALUES (%s, %s, %s, %s)
                """
                values = (produit, quantite, prix, date_vente)
                cursor.execute(sql, values)
            except Exception as e:
                print(f"Erreur lors de l'insertion de la ligne: {e}")
                continue

        connection.commit()
        print("✅ Données importées avec succès !")

    except Error as e:
        print(f"❌ Erreur MySQL : {e}")

    except Exception as e:
        print(f"❌ Erreur générale : {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("🔌 Connexion fermée.")

if __name__ == "__main__":
    import os  # Ajouter cette ligne pour utiliser os.path.exists
    load_to_mysql()