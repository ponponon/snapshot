from minio import Minio
from minio.error import S3Error
import io

client = Minio(
    "192.168.31.245:9000",
    access_key="ponponon",
    secret_key="ponponon",
    secure=False
)


def upload_snapshot(jpg_image: bytes, jpg_path_name: str):
    upaload_image(
        bucket_name='snapshot',
        object_name=jpg_path_name,
        jpg_stream=jpg_image
    )


def upaload_image(bucket_name: str, object_name: str, jpg_stream: bytes):
    file_like_obj_jpg_stream = io.BytesIO(jpg_stream)
    client.put_object(
        bucket_name=bucket_name,
        object_name=object_name,
        data=file_like_obj_jpg_stream,
        length=len(jpg_stream),
        content_type='image/jpeg'
    )
