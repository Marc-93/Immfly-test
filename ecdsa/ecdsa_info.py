from hashlib import sha256

from ecdsa.util import sigencode_der
import ecdsa


def get_ecdsa_info():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
    vk = sk.get_verifying_key()
    sig = sk.sign(b"password", hashfunc=sha256, sigencode=sigencode_der)

    public_key = f"04{vk.to_string().hex()}"
    signature = sig.hex()

    return {"private_key": sk,
            "public_key": public_key,
            "signature": signature}


def sign_message(private_key, resource_id):
    return private_key.sign(resource_id, hashfunc=sha256, sigencode=sigencode_der).hex()
