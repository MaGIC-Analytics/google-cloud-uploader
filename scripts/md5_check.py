import hashlib
import base64
def md5_file(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    hash=hash_md5.digest()
    return base64.b64encode(hash).decode('utf-8')
