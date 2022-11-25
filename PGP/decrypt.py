import gnupg
from Pickle.extractData import *
from pprint import pprint

def decryptData(encrypted_string,secretCode):
    gpg = gnupg.GPG()
    # unencrypted_string = 'Who are you? How did you get in my house?'
    # encrypted_data = gpg.encrypt(unencrypted_string, '201901026@daiict.ac.in')
    # encrypted_string = str(encrypted_data)
    decrypted_data = gpg.decrypt(encrypted_string)
    decrypted_string=str(decrypted_data)
    ileName = "pgpdecryption"
    fileName += secretCode+".pkl"
    create_pickle(fileName,decrypted_string)
    print (decrypted_string)
    return decrypted_string
