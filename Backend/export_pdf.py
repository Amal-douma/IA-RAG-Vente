from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_report(query_results, output_path="report.pdf"):
    try:
        c = canvas.Canvas(output_path, pagesize=letter)
        c.setFont("Helvetica", 12)
        
        # Titre du rapport
        c.drawString(100, 750, "Rapport eCommerce")
        c.drawString(100, 730, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Afficher les résultats
        y = 700
        if query_results and query_results["data"]:
            # En-têtes des colonnes
            for i, col in enumerate(query_results["columns"]):
                c.drawString(100 + i * 100, y, str(col))
            y -= 20
            
            # Données
            for row in query_results["data"]:
                for i, value in enumerate(row):
                    c.drawString(100 + i * 100, y, str(value))
                y -= 20
                if y < 50:  # Nouvelle page si nécessaire
                    c.showPage()
                    y = 750
        
        c.save()
        print(f"✅ Rapport PDF généré : {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Erreur lors de la génération du PDF : {e}")
        return None

if __name__ == "__main__":
    # Test
    test_results = {
        "columns": ["produit", "total_vendu"],
        "data": [("Produit A", 100), ("Produit B", 200)]
    }
    generate_pdf_report(test_results, "test_report.pdf")

