import gnupg
from Pickle.extractData import *
from pprint import pprint

def encrypt_data(secretCode):
    gpg = gnupg.GPG()
    #unencrypted_string = 'Who are you? How did you get in my house?'
    fileName1 = "polarEncoder"
    fileName1+=secretCode+".pkl"
    unencrypted_string = extract_pickle(fileName1)
    
    encrypted_data = gpg.encrypt(''.join([str(x) for x in unencrypted_string[0]]), '201901026@daiict.ac.in')
    encrypted_string = str(encrypted_data)
    fileName2 = "pgpencryption_"
    fileName2 += secretCode+".pkl"
    create_pickle(fileName2,encrypted_string)
    return encrypted_string