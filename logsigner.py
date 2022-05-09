import sys
import os.path
import glob, os
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
logFiles = sys.argv[2:]


def generate_signature(key, data):
    #zipping
    print("Generating Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open(data_f + ".signed", 'wb') as f: f.write(signature)
    print(data_f + " has been signed")
    print("Done")


def verify_signature(key, data):
    #unzipping
    print("Verifying Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open(data_f + ".signed", 'rb') as f: signature = f.read()
    rsp = data_f + " has been successfully verified" if (signer.verify(h, signature)) else data_f + " Verification Failure"
    print(rsp)

signCertExists = os.path.isfile('sign.pem')
verifyCertExists = os.path.isfile('verify.pem')


# Check pem files are exists if not, create them
if (verifyCertExists!= True) and (signCertExists != True):
    key = RSA.generate(1024)
    privKeyString = key.export_key()

    with open ("sign.pem","w") as prvFile:
        print("{}".format(privKeyString.decode()),file=prvFile)

    pubKeyString = key.publickey().exportKey()
    with open ("verify.pem", "w") as pubFile:
            print("{}".format(pubKeyString.decode()), file=pubFile)


for data_p in logFiles:
    for data_f in glob.glob(data_p):

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