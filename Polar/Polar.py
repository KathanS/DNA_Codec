import matlab.engine
from Pickle.extractData import *
eng = matlab.engine.start_matlab()
eng.cd('Polar', nargout=1)



def encode(bits,secretCode):
    # Polar encoding
    # bits: input bits
    # return: encoded bits
    fileName1 = "Huffman_encoder"
    fileName1+=secretCode+".pkl"
    input_text= extract_pickle(fileName1)
    encoded_output = eng.encodePolar(matlab.int8(input_text),nargout=1)
    encoded_output =[[int(num) for num in x] for x in encoded_output]
    print(encoded_output)
    fileName2 = "polarEncoder"
    fileName2+=secretCode+".pkl"
    create_pickle(fileName2,encoded_output)
    eng.quit()
    return encoded_output
   

def decode(secretCode):
    # Polar decoding
    # bits: input bits
    # return: decoded bits
    fileName1 = "pgpdecryption"
    fileName1 += secretCode+".pkl"
    bits = extract_pickle(fileName1)
    
    eng = matlab.engine.start_matlab()
    input_text= bits
    decoded_output = eng.decodePolar(matlab.int8(input_text),nargout=1)
    decoded_output =[[int(num) for num in x] for x in decoded_output]
    print(decoded_output)
    
    fileName2 = "polarDecoder"
    fileName2+=secretCode+ ".pkl"
    create_pickle(fileName2,decoded_output)
    eng.quit()
    return decoded_output
