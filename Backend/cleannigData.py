import pandas as pd

# Charger les données Excel
df = pd.read_excel("../data/bd.xlsx")

# Afficher les 5 premières lignes
print("=== 5 premières lignes ===")
print(df.head())

# Afficher les 5 premières lignes, ligne par ligne, avec le type de chaque colonne
print("\n=== Types de données par colonne ===")
print(df.dtypes)

# Vérifier s'il y a des valeurs nulles dans chaque colonne
print("\n=== Nombre de valeurs nulles par colonne ===")
print(df.isnull().sum())

# Optionnel : afficher si le DataFrame contient des valeurs nulles quelque part
if df.isnull().values.any():
    print("\nAttention : Il y a des valeurs nulles dans le DataFrame.")
else:
    print("\nAucune valeur nulle détectée dans le DataFrame.")
