import rsa
import base64
class RsaOperations:
    @staticmethod
    def generate_pair_of_keys():
         public_key, private_key, = rsa.newkeys(512)
         return public_key.save_pkcs1().decode("utf-8"), private_key.save_pkcs1().decode("utf-8")
    @staticmethod
    def load_public_key(public_key):
        return rsa.PublicKey.load_pkcs1(public_key)
    @staticmethod
    def load_private_key(private_key):
        return rsa.PrivateKey.load_pkcs1(private_key)
    @staticmethod
    def generate_sign(message_to_be_encoded, private_key):
        return base64.b64encode(rsa.sign(message_to_be_encoded.encode(), private_key, 'SHA-1'))
    @staticmethod
    def verify_signature(message, signature, public_key):
        verification_status = False

        if(rsa.verify(message.encode(), RsaOperations.retrieve_bytes_from_base64(signature), public_key) == 'SHA-1'):
                verification_status = True

        return verification_status
    @staticmethod
    def retrieve_bytes_from_base64(data):
            return base64.b64decode(data)