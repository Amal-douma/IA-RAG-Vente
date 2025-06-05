import gradio as gr
import mysql.connector

def answer_question(question):
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
            result = "\n".join([f"{produit}: {qte}" for produit, qte in rows])
            return result
        else:
            return "Aucune donnée trouvée pour 2025."

    return "Je n'ai pas compris votre question."

iface = gr.Interface(fn=answer_question, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", server_port=7860)
