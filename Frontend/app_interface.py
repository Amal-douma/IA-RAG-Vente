# import gradio as gr
# import mysql.connector

# def answer_question(question):
#     try:
#         conn = mysql.connector.connect(
#             host="mysql",
#             port=3306,
#             user="appuser",
#             password="appuserpassword",
#             database="ecommerce_db"
#         )
#         cursor = conn.cursor()

#         question = question.lower()

#         if "produit" in question and "vendu" in question and "2025" in question:
#             cursor.execute("""
#                 SELECT produit, SUM(quantite) as total_vendu
#                 FROM ventes
#                 WHERE YEAR(date_vente) = 2025    
#                 GROUP BY produit
#                 ORDER BY total_vendu DESC
#                 LIMIT 5
#             """)
#             rows = cursor.fetchall()
#             if rows:
#                 return "\n".join([f"{produit}: {qte}" for produit, qte in rows])
#             else:
#                 return "Aucune donnée trouvée pour 2025."

#         elif "chiffre" in question and "affaires" in question and "mensuel" in question:
#             cursor.execute("""
#                 SELECT DATE_FORMAT(date_vente, '%Y-%m') AS mois,
#                        SUM(quantite * prix) AS chiffre_affaires
#                 FROM ventes
#                 GROUP BY mois
#                 ORDER BY mois;
#             """)
#             rows = cursor.fetchall()
#             if rows:
#                 return "\n".join([f"{mois} : {chiffre:.2f} TND" for mois, chiffre in rows])
#             else:
#                 return "Aucune donnée disponible."

#         else:
#             return "Je n'ai pas compris votre question."

#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

# iface = gr.Interface(fn=answer_question, inputs="text", outputs="text")
# iface.launch(server_name="0.0.0.0", server_port=7860)
import sys
import os

print("sys.path before:", sys.path)

# Ajouter le dossier parent au path pour accéder à backend/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("sys.path after:", sys.path)

from backend import hdfs_uploader
import gradio as gr
import mysql.connector
from backend import hdfs_uploader  # Assure-toi que backend est un package (avec __init__.py)
from backend.Logger import save_question_answer_log

def save_question_answer_log(question, answer):
    import os
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"/app/logs/log_{timestamp}.txt"

    os.makedirs("/app/logs", exist_ok=True)

    content = f"Question: {question}\nRéponse: {answer}\nTimestamp: {timestamp}\n"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename

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

        question_lower = question.lower()

        if "produit" in question_lower and "vendu" in question_lower and "2025" in question_lower:
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
                answer = "\n".join([f"{produit}: {qte}" for produit, qte in rows])
            else:
                answer = "Aucune donnée trouvée pour 2025."

        elif "chiffre" in question_lower and "affaires" in question_lower and "mensuel" in question_lower:
            cursor.execute("""
                SELECT DATE_FORMAT(date_vente, '%Y-%m') AS mois,
                       SUM(quantite * prix) AS chiffre_affaires
                FROM ventes
                GROUP BY mois
                ORDER BY mois;
            """)
            rows = cursor.fetchall()
            if rows:
                answer = "\n".join([f"{mois} : {chiffre:.2f} TND" for mois, chiffre in rows])
            else:
                answer = "Aucune donnée disponible."

        else:
            answer = "Je n'ai pas compris votre question."

        # Sauvegarder le log localement
        log_file = save_question_answer_log(question, answer)

        # Uploader sur HDFS (dans dossier /logs sur HDFS)
        hdfs_path = f"/logs/{os.path.basename(log_file)}"
        hdfs_uploader.upload_to_hdfs(log_file, hdfs_path)

        return answer

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

iface = gr.Interface(fn=answer_question, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", server_port=7860)
