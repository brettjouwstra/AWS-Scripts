# Only a portion of something useful, would need another function to deal with auth, etc.

import boto3


s3_paginator = boto3.client('s3').get_paginator('list_objects_v2')


def keys(bucket_name, prefix, delimiter='/', start_after='/'):
    prefix = prefix[1:] if prefix.startswith(delimiter) else prefix
    start_after = (start_after or prefix) if prefix.endswith(delimiter) else start_after
    for page in s3_paginator.paginate(Bucket=bucket_name, Prefix=prefix, StartAfter=start_after):
        for content in page.get('Contents', ()):
            yield content['Key']

def list_generator(list_prefix):

    groupings = {}

    for prefix in list_prefix:
        res = keys(bucket_name, prefix)
        
        temp_list = []
        for x in res:
            if x[-1] == '/':
                pass
            else:
                tmp = temp_list.append('https://some-bucket.s3.us-east-2.amazonaws.com/%s' % x)
        
        groupings[prefix] = temp_list

    return groupings
