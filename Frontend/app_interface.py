import gradio as gr
import mysql.connector

def answer_question(question):
    try:
        conn = mysql.connector.connect(
            host="mysql",
            port=3306,
            user="appuser",
            password="appuserpassword",
            database="ecommerce_db"
        )
        cursor = conn.cursor()

        question = question.lower()

        if "produit" in question and "vendu" in question and "2025" in question:
            cursor.execute("""
                SELECT produit, SUM(quantite) as total_vendu
                FROM ventes
                WHERE YEAR(date_vente) = 2025    
                GROUP BY produit
                ORDER BY total_vendu DESC
                LIMIT 5
            """)
            rows = cursor.fetchall()
            if rows:
                return "\n".join([f"{produit}: {qte}" for produit, qte in rows])
            else:
                return "Aucune donnée trouvée pour 2025."

        elif "chiffre" in question and "affaires" in question and "mensuel" in question:
            cursor.execute("""
                SELECT DATE_FORMAT(date_vente, '%Y-%m') AS mois,
                       SUM(quantite * prix) AS chiffre_affaires
                FROM ventes
                GROUP BY mois
                ORDER BY mois;
            """)
            rows = cursor.fetchall()
            if rows:
                return "\n".join([f"{mois} : {chiffre:.2f} TND" for mois, chiffre in rows])
            else:
                return "Aucune donnée disponible."

        else:
            return "Je n'ai pas compris votre question."

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

iface = gr.Interface(fn=answer_question, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", server_port=7860)

