from storage.handler import StorageHandler


__version__ = '0.1.0'
storage_handler = StorageHandler()
default_storage = storage_handler.default_storage
handler = storage_handler
