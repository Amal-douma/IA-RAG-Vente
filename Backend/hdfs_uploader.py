# from hdfs import InsecureClient
# import os

# def upload_to_hdfs(file_path, hdfs_url='http://localhost:9870', hdfs_dir='/reports/', user='hadoop'):
#     try:
#         # Connexion WebHDFS via HTTP
#         client = InsecureClient(hdfs_url, user=user)
        
#         # Construire le chemin complet sur HDFS
#         hdfs_path = os.path.join(hdfs_dir, os.path.basename(file_path))
        
#         # Upload avec overwrite autorisé
#         client.upload(hdfs_path, file_path, overwrite=True)
        
#         print(f"✅ Fichier {file_path} envoyé vers {hdfs_path}")
#         return hdfs_path
#     except Exception as e:
#         print(f"❌ Erreur lors de l'upload vers HDFS : {e}")
#         return None

# if __name__ == "__main__":
#     upload_to_hdfs("test_report.pdf")
from hdfs import InsecureClient

def upload_to_hdfs(local_path, hdfs_path):
    client = InsecureClient('http://hdfs-namenode:9870', user='hdfs')
    client.upload(hdfs_path, local_path, overwrite=True)
