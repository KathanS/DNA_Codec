import gnupg
from Pickle.extractData import *
from pprint import pprint

def decryptData(secretCode):
    gpg = gnupg.GPG()
    # unencrypted_string = 'Who are you? How did you get in my house?'
    # encrypted_data = gpg.encrypt(unencrypted_string, '201901026@daiict.ac.in')
    # encrypted_string = str(encrypted_data)
    fileName1 = "binary2ascii"
    fileName1+=secretCode+".pkl"
    encrypted_string = extract_pickle(fileName1)
    #fileName1 = "polarDecoder"
    #fileName1+=secretCode+ ".pkl"
    #encrypted_string = extract_pickle(fileName1)
    decrypted_data = gpg.decrypt(encrypted_string)
    decrypted_string=str(decrypted_data)
    fileName2 = "pgpdecryption"
    fileName2 += secretCode+".pkl"
    create_pickle(fileName2,decrypted_string)
    print (decrypted_string)
    return decrypted_string
