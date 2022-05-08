import sys
import os.path
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from Cryptodome.Signature import PKCS1_v1_5



def usage():
    print("Usage: \n"
          "logsigner -s  <data> \n"
          "logsigner -v  <data> \n")

if (len(sys.argv) < 3):
    usage()
    quit()



op = sys.argv[1]
data_f = sys.argv[2]

def generate_signature(key, data):
    print("Generating Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open(data_f + "signed", 'wb') as f: f.write(signature)


def verify_signature(key, data):
    print("Verifying Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open(data_f + "signed", 'rb') as f: signature = f.read()
    rsp = "Success" if (signer.verify(h, signature)) else " Verification Failure"
    print(rsp)

signCertExists = os.path.isfile('sign.pem')
verifyCertExists = os.path.isfile('verify.pem')

# print(signCertExists)
# print(verifyCertExists)

# check pem files are exists if not create them
if (verifyCertExists!= True) or (signCertExists != True):
    key = RSA.generate(1024)
    privKeyString = key.export_key()

    with open ("sign.pem","w") as prvFile:
        print("{}".format(privKeyString.decode()),file=prvFile)

    pubKeyString = key.publickey().exportKey()
    with open ("verify.pem", "w") as pubFile:
            print("{}".format(pubKeyString.decode()), file=pubFile)

# Read all file contents
with open("sign.pem", 'rb') as f: key = f.read()
with open(data_f, 'rb') as f: data = f.read()

if (op == "-s"):
    # Generate Signature
    generate_signature(key, data)
elif (op == "-v"):
    # Verify Signature
    verify_signature(key, data)
else:
    # Error
    usage()
    

