import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime

def load_to_mysql():
    connection = None
    cursor = None

    try:
        # Establishing connection to MySQL
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,  # Adjust port as per your Docker configuration
            user="appuser",
            password="appuserpassword"
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce_db")
        cursor.close()
        connection.close()

        # Reconnect to the created database
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,
            user="appuser",
            password="appuserpassword",
            database="ecommerce_db"
        )

        cursor = connection.cursor()
        print("✅ Connexion réussie à la base de données.")

        # Load Excel file
        file_path = "../data/bd.xlsx"
        df = pd.read_excel(file_path)

        # Debugging: Print column names to verify
        print("Colonnes du DataFrame:", df.columns.tolist())

        # Create table with appropriate columns
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

        # Insert data into the table
        for _, row in df.iterrows():
            try:
                # Map Excel columns to table columns
                produit = row['Désignation'] if pd.notnull(row['Désignation']) else 'Unknown'
                quantite = int(row['Quantité']) if pd.notnull(row['Quantité']) else 0
                prix = float(row['Prix Unit HT']) if pd.notnull(row['Prix Unit HT']) else 0.0
                date_vente = row['Date'] if pd.notnull(row['Date']) else None

                # Ensure date_vente is in the correct format
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
    load_to_mysql()