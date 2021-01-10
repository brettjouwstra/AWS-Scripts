import os
from pathlib import Path
import sys
import threading
import boto3

# Examples come from here: https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php

# Using Python - upload files

client = boto3.client('s3')

configuration_dir = (r'C:\some\config\path')

for root, dirs, files in os.walk(configuration_dir):
    #print(root)

    dirs[:] = [d for d in dirs if not d.startswith('.')]

    # for dir in dirs:
    #     print(os.path.join(root, dir))
    for file in files:
        #print(os.path.join(root, file))
        client.upload_file(os.path.join(root, file), 'bucket_name', file)
