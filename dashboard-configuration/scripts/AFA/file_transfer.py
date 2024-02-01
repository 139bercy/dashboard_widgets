import os
import s3fs
import pandas as pd

# To move files between datalab and your codespace 

AWS_S3_ENDPOINT = os.environ["AWS_S3_ENDPOINT"]
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_SESSION_TOKEN = os.environ["AWS_SESSION_TOKEN"]

fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': "https://" + AWS_S3_ENDPOINT},
                           key = AWS_ACCESS_KEY_ID, 
                           secret = AWS_SECRET_ACCESS_KEY, 
                           token = AWS_SESSION_TOKEN)

# Datalab > Local (Note : You can drag and drop from your computer)

def import_file(path_in ,path_out):
    # both are path to files
    print('imported : '+path_in)
    with fs.open(path_in, 'rb') as file_in:
        with open(path_out, 'wb') as file_out:
            file_out.write(file_in.read())

def import_folder(path_folder_in ,path_folder_out):
    # both are path to folders and are intended to finish by "/"
    for path_file in fs.ls(path_folder_in):
        file_name = path_file.split("/")[-1] 
        import_file(path_file ,path_folder_out+file_name)

# Local > Datalab 

def export_file(path_in,path_out):
    # both are path to files
    print('exported : '+path_in)
    with open(path_in, 'rb') as file_in :
        with fs.open(path_out,'wb') as file_out:
            file_out.write(file_in.read())

def export_folder(path_folder_in ,path_folder_out):
    # both are path to folders and are intended to finish by "/"
    for file_name in os.listdir(path_folder_in):
        export_file(path_folder_in+file_name ,path_folder_out+file_name)

#import_folder('lsoszynski/AFA/', '../files/')
#export_folder('../files/update/', 'lsoszynski/AFA/')
export_file('data.ndjson', 'lsoszynski/data/data-20-10-6-great.ndjson')
export_file('afa-2021.csv', 'lsoszynski/config/afa-2021-20-10-great.csv')
