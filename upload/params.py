from dataclasses import dataclass


@dataclass
class MinioParams:
    endpoint: str
    accessKey: str
    secretKey: str
    bucket: str
    filename: str
