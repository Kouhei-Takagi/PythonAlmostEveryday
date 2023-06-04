import os
import binascii
from ecdsa import SigningKey, VerifyingKey, SECP256k1

# 既存の秘密鍵（16進数形式の文字列）
hex_private_key = "1000000000000000000000000000000000000000000000000000000000000001"

# 秘密鍵をバイト列に変換
private_key_bytes = binascii.unhexlify(hex_private_key)

# 秘密鍵からSigningKeyオブジェクトを生成
private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)

# 公開鍵を生成
public_key = private_key.get_verifying_key()

# 公開鍵を16進数形式で表示
print("Public key:", binascii.hexlify(public_key.to_string()).decode())
