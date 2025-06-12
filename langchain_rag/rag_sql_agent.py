from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_sql_query(question):
    try:
        # Initialiser le modèle de langage (remplacez par votre modèle préféré)
        llm = OpenAI(api_key="votre-clé-api")  # Configurez votre clé API ou utilisez un modèle local
        
        # Définir le prompt pour générer des requêtes SQL
        prompt = PromptTemplate(
            input_variables=["question"],
            template="""
            Vous êtes un assistant SQL expert. À partir de la question suivante, générez une requête SQL compatible avec une table MySQL nommée 'ventes' ayant les colonnes : id, produit, quantite, prix, date_vente.
            
            Question : {question}
            
            Fournissez uniquement la requête SQL, sans explication.
            """
        )
        
        # Créer la chaîne LangChain
        chain = LLMChain(llm=llm, prompt=prompt)
        
        # Générer la requête SQL
        sql_query = chain.run(question=question)
        return sql_query.strip()
    
    except Exception as e:
        print(f"❌ Erreur lors de la génération de la requête SQL : {e}")
        return None

if __name__ == "__main__":
    # Test
    test_question = "Quels sont les produits les plus vendus en 2024 ?"
    sql_query = generate_sql_query(test_question)
    print("Requête SQL générée:", sql_query)