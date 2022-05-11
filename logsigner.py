from shutil import copyfile
import sys
import os.path
import glob, os
import shutil
from datetime import date
from datetime import timedelta
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
    today = date.today()
    yesterday = str(today - timedelta(days = 1))
    os.rename(data_f,yesterday + "_" + data_f)


    print("Generating Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open(yesterday + "_" + data_f + ".signed", 'wb') as f: f.write(signature)
    print(data_f + " has been signed")
   

def verify_signature(key, data):
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
if (verifyCertExists!= True) or (signCertExists != True):
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

# Files are sent to signed folder
if (os.path.exists("signed") != True) and (op == "-s"):
    print("Log files and sign files are copying to Signed folder...")
    os.mkdir("signed")
    sourcepath='.'
    sourcefiles = os.listdir(sourcepath)
    destinationpath = 'signed'
    for file in sourcefiles:
        if file.endswith('.signed') or file.endswith('.bz2'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    print("Done")

elif (os.path.exists("signed") == True) and (op == "-s"):
    print("Log files and sign files are copying to Signed folder...")
    sourcepath='.'
    sourcefiles = os.listdir(sourcepath)
    destinationpath = 'signed'
    for file in sourcefiles:
        if file.endswith('.signed') or file.endswith('.bz2'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    print("Done")

else:
    print("Done")