import gnupg
from Pickle.extractData import *
from pprint import pprint

def encrypt_data(unencrypted_string,secretCode):
    gpg = gnupg.GPG()
    #unencrypted_string = 'Who are you? How did you get in my house?'
    encrypted_data = gpg.encrypt(unencrypted_string, '201901026@daiict.ac.in')
    encrypted_string = str(encrypted_data)
    fileName = "pgpencryption"
    fileName += secretCode+".pkl"
    create_pickle(fileName,encrypted_string)
    return encrypted_string