# 🧠 IA-RAG-Vente - Assistant IA pour Analyse des Ventes e-Commerce

Projet développé par :  
👩‍💻 Douma Amal  
👨‍💻 EMNA CHATTI

## 📌 Description

IA-RAG-Vente est une application intelligente basée sur le concept du RAG (Retrieval-Augmented Generation) pour analyser automatiquement les données de ventes e-commerce.  
Elle permet à l’utilisateur de poser des questions en français (ex. : "Qui a échoué ?", "Quels sont les meilleurs produits du mois ?") et d’obtenir des réponses précises sous forme de tableaux, visualisations ou rapports PDF.

Ce projet vise à combiner les technologies de la Data (ETL, MySQL, HDFS), du NLP (LangChain) et d’interface (Gradio) pour créer une expérience utilisateur fluide et interactive.

---

## 📂 Architecture du projet

## 📁 Architecture du projet

```text
projet-rag-ecommerce/
├── data/                  ← Fichiers Excel d’entrée (ex: ventes_ecommerce.xlsx)
│
├── backend/
│   ├── db_loader.py       ← Injection des données Excel dans MySQL
│   ├── query_executor.py  ← Exécution des requêtes SQL générées
│   ├── export_pdf.py      ← Génération de rapport PDF
│   └── hdfs_uploader.py   ← Envoi des PDF dans HDFS
│
├── frontend/
│   └── app_interface.py   ← Interface Gradio (utilisateur pose ses questions)
│
├── langchain_rag/
│   └── rag_sql_agent.py   ← Composant RAG (Langchain) pour conversion Question → SQL
│
├── Dockerfile             ← Dockerisation du projet
├── docker-compose.yml     ← Services (MySQL, HDFS, API, UI)
├── requirements.txt       ← Librairies Python requises
└── README.md              ← Description du projet

---

## ⚙️ Fonctionnalités

- 📤 Upload de fichier Excel contenant les données de vente
- 🛢️ Ingestion automatique dans une base MySQL
- 💬 L'utilisateur pose des questions en français (NLP)
- 🔍 Traduction automatique en requêtes SQL via RAG
- 📊 Visualisation des résultats dans Gradio (tableaux, graphiques)
- 📄 Export PDF des analyses
- ☁️ Archivage des PDF dans HDFS

---

## 🛠️ Technologies utilisées

- 🐍 Python
- 📦 LangChain (RAG)
- 🐳 Docker / Docker Compose
- 🧮 MySQL
- 🧾 Power BI (optionnel pour dashboard)
- 🖼️ Gradio
- 🗃️ HDFS
- 📑 Pandas, Matplotlib, ReportLab

---

## 🚀 Lancer le projet (en local)

```bash
# Cloner le dépôt
git clone https://github.com/Amal-douma/IA-RAG-Vente.git

# Se rendre dans le dossier
cd IA-RAG-Vente

# Lancer les services via Docker
docker-compose up --build
