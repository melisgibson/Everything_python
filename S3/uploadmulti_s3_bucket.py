import boto3
import os
import glob

# upload multiple files

cwd = os.getcwd()
cwd=cwd+"/upload/"
files = glob.glob(cwd+"/*.py") # put in your file type
for file in files:
    s3 = boto3.client("s3")
    response = s3.upload_file(
    Filename = file,
    Bucket = "mypythonpractice2",
    Key = file.split("/")[-1]
    )
