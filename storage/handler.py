import os
import importlib

from storage.backends.filesystem import FileSystemStorage
from storage.backends.s3 import S3Storage
from storage.utils import import_string
from storage.conf import settings




class StorageHandler:

    def __init__(self):
        self.default_storage = self._initialize_storage()


    def _initialize_storage(self):
        try:
            StorageClass = import_string(settings.DEFAULT_STORAGE_BACKEND)
        except:
            # TODO: raise a more specific error
            raise ValueError()

        if issubclass(StorageClass, FileSystemStorage):
            return StorageClass(
                base_path=settings.BASE_PATH,
                file_permissions=settings.FILE_PERMISSIONS,
            )
        elif issubclass(StorageClass, S3Storage):
            if not settings.S3_BUCKET_NAME:
                raise ValueError("S3_BUCKET_NAME must be set in environment variables.")

            return StorageClass(
                bucket_name=settings.S3_BUCKET_NAME
            )
        else:
            raise ValueError(f"Invalid storage backend '{settings.DEFAULT_STORAGE_BACKEND}'.")




storage_handler = StorageHandler()
default_storage = storage_handler.default_storage
