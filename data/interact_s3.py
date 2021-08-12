import boto3
import pandas as pd
import glob
import os

s3_client = boto3.client('s3')

csv_files = glob.glob("data/*.csv")

for filename in csv_files:
    key = "%s/%s" % ("raw-data", os.path.basename(filename))
    print("Putting %s as %s" % (filename,key))
    s3_client.upload_file(filename, "datalake-psalomao-155914520574", key)

# s3_client.upload_file("data/*.csv",
#                         "datalake-psalomao-155914520574",
#                         "raw-data/")