import os
import binascii
from ecdsa import SigningKey, SECP256k1

# 秘密鍵を生成
private_key = SigningKey.generate(curve=SECP256k1)

# 公開鍵を生成
public_key = private_key.get_verifying_key()

# 秘密鍵と公開鍵を16進数形式で表示
print("Private key:", binascii.hexlify(private_key.to_string()).decode())
print("Public key:", binascii.hexlify(public_key.to_string()).decode())
