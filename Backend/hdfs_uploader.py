from hdfs import InsecureClient

def upload_to_hdfs(local_path, hdfs_path):
    client = InsecureClient('http://hdfs-namenode:9870', user='hdfs')
    client.upload(hdfs_path, local_path, overwrite=True)
