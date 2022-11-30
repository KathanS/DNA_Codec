# Adding current folder to the system path
import os
import sys
sys.path.insert(0, os.getcwd())

import matlab.engine
from Pickle.extractData import *
eng = matlab.engine.start_matlab()
eng.cd('Polar', nargout=1)



def encode(secretCode):
    # Polar encoding
    # bits: input bits
    # return: encoded bits
    fileName1 = "Huffman_encoder"
    fileName1+=secretCode+".pkl"
    input_text= extract_pickle(fileName1)

    input_t = []
    for i in range(len(input_text)):
        input_t.append(ord(input_text[i]) - ord('0'))
    
    encoded_output = eng.encodePolar(matlab.int8(input_t),nargout=4)
    encoded_output =[[int(num) for num in x] for x in encoded_output]
    #print(encoded_output)
    fileName2 = "polarEncoder"
    fileName2+=secretCode+".pkl"
    create_pickle(fileName2,encoded_output)
    eng.quit()
    return encoded_output
   

def decode(secretCode):
    # Polar decoding
    # bits: input bits
    # return: decoded bits
    fileName1 = "ternary2binary"
    fileName1+=secretCode+".pkl"
    bits= extract_pickle(fileName1)
    eng = matlab.engine.start_matlab()
    input_text= bits
    
    # f=
    # k=
    # A=

    input_list = [int(x) for x in input_text]

    print(input_list)

    fileName1 = "Huffman_encoder"
    fileName1+=secretCode+".pkl"
    input_text= extract_pickle(fileName1)

    input_t = []
    for i in range(len(input_text)):
        input_t.append(ord(input_text[i]) - ord('0'))
    
    print(input_t)

    encoded_output = eng.encodePolar(matlab.int8(input_t),nargout=4)
    

    decoded_output = eng.encodePolar(matlab.int8(input_list), nargout=1)
    decoded_output =[[int(num) for num in x] for x in decoded_output]
    #print(decoded_output)
    
    fileName2 = "polarDecoder"
    fileName2+=secretCode+ ".pkl"
    create_pickle(fileName2,decoded_output)
    eng.quit()
    return decoded_output

if __name__ == "__main__":
    out = encode("12345")
    # print(out)