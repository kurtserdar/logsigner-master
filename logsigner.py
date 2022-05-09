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

"""def get_all_file_paths(directory):
  
    # initializing empty file paths list
    file_paths = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
  
    # returning all file paths
    return file_paths

def main():
    # path to folder which needs to be zipped
    directory = './python_files'
  
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
  
    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
  
    # writing files to a zipfile
    with ZipFile('my_python_files.zip','w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
  
    print('All files zipped successfully!')   """      

def generate_signature(key, data):
    print("Generating Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open(data_f + ".signed", 'wb') as f: f.write(signature)
    print("Done")


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

# Check pem files are exists if not, create them
if (verifyCertExists!= True) and (signCertExists != True):
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