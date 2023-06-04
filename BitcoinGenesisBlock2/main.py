import hashlib
import base58

def pubkey_to_address(pubkey: str):
    # 公開鍵をバイト列に変換
    pubkey_bytes = bytes.fromhex(pubkey)

    # SHA-256ハッシュ関数を適用
    sha = hashlib.sha256()
    sha.update(pubkey_bytes)
    hash_1 = sha.digest()

    # RIPEMD-160ハッシュ関数を適用
    ripemd = hashlib.new('ripemd160')
    ripemd.update(hash_1)
    hash_2 = ripemd.digest()

    # バージョンバイトを追加（0x00 for Main Network）
    extended = b'\x00' + hash_2

    # ダブルSHA-256ハッシュ関数を適用し、最初の4バイトを取得
    sha = hashlib.sha256()
    sha.update(extended)
    hash_3 = sha.digest()
    sha = hashlib.sha256()
    sha.update(hash_3)
    checksum = sha.digest()[:4]

    # チェックサムを追加
    final = extended + checksum

    # Base58Checkエンコードを適用
    address = base58.b58encode(final)

    return address.decode()

# 公開鍵
pubkey = '678AFDB0FE5548271967F1A67130B7105CD6A828E03909A67962E0EA1F61DEB649F6BC3F4CEF38C4F35504E51EC112DE5C384DF7BA0B8D578A4C702B6BF11D5F'

print(pubkey_to_address(pubkey))
# 1BHvjdMGeyN1BWKMcCnyWEg7KM3uMWrWFB