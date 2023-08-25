from enum import Enum


class CreationMode(Enum):
    INSERT = "INSERT"
    COPY = "COPY"
    PARQUET = "PARQUET"
    PARQUET_S3 = "PARQUET_S3"
    PARQUET_ARRAY = "PARQUET_ARRAY"