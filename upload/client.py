import cfg
from minio import Minio
from upload.params import MinioParams


def upload_report(params: MinioParams):
    # create minio client
    client = Minio(params.endpoint, access_key=params.accessKey,
                   secret_key=params.secretKey)

    bucket = params.bucket
    filename = params.filename

    # look for existing bucket and make it if it doesn't exist
    found = client.bucket_exists(bucket)
    if not found:
        client.make_bucket(bucket)
    else:
        cfg.logger.info(f"bucket {bucket} already exists")
    # upload object to client
    client.fput_object(bucket, filename, filename)
    cfg.logger.info(f"successfully uploaded {filename} to bucket {bucket}")
