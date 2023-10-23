import hashlib

def md5(text: str):
    """MD5加密"""
    return hashlib.md5(text.encode()).hexdigest()

def sha1(text: str):
    """生成sha1摘要"""
    return hashlib.sha1(text.encode()).hexdigest()
    
def sha256(text: str):
    """生成SHA256摘要"""
    return hashlib.sha256(text.encode()).hexdigest()

print(sha256(''))
assert 1==1 
print('pass')