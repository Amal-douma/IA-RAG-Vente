from hdfs import InsecureClient
import os

def upload_to_hdfs(file_path, hdfs_url='http://localhost:9870', hdfs_dir='/reports/', user='hadoop'):
    try:
        client = InsecureClient(hdfs_url, user=user)
        hdfs_path = os.path.join(hdfs_dir, os.path.basename(file_path))

        # Upload du fichier
        client.upload(hdfs_path, file_path, overwrite=True)

        print(f"✅ Fichier {file_path} envoyé vers {hdfs_path}")
        return hdfs_path
    except Exception as e:
        print(f"❌ Erreur lors de l'upload vers HDFS : {e}")
        return None

if __name__ == "__main__":
    upload_to_hdfs("test_report.pdf")
