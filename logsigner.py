import sys
import codecs
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from Cryptodome.Signature import PKCS1_v1_5


def usage():
    print("Usage: \n"
          "logsigner -s  <priv-key> <data> <signature-file> \n"
          "logsigner -v  <pub-key> <data> <signature-file> \n")

if (len(sys.argv) < 5):
    usage()
    quit()

op = sys.argv[1]
key_f = sys.argv[2]
data_f = sys.argv[3]
sig_f = sys.argv[4]

def generate_signature(key, data, sig_f):
    print("Generating Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open(sig_f, 'wb') as f: f.write(signature)


def verify_signature(key, data, sig_f):
    print("Verifying Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open(sig_f, 'rb') as f: signature = f.read()
    rsp = "Success" if (signer.verify(h, signature)) else " Verification Failure"
    print(rsp)


# Read all file contents
with open(key_f, 'rb') as f: key = f.read()
with open(data_f, 'rb') as f: data = f.read()

if (op == "-s"):
    # Generate Signature
    generate_signature(key, data, sig_f)
elif (op == "-v"):
    # Verify Signature
    verify_signature(key, data, sig_f)
else:
    # Error
    usage()

