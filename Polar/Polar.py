import matlab.engine
from Pickle.extractData import *
eng = matlab.engine.start_matlab()
eng.cd('Polar', nargout=1)



def encode(bits,secretCode):
    # Polar encoding
    # bits: input bits
    # return: encoded bits
    input_text= bits
    encoded_output = eng.encodePolar(matlab.int8(input_text),nargout=1)
    encoded_output =[[int(num) for num in x] for x in encoded_output]
    print(encoded_output)
    fileName = "polarEncoder"
    fileName+=secretCode+".pkl"
    create_pickle(fileName,encoded_output)
    eng.quit()
    return encoded_output
   

def decode(bits,secretCode):
    # Polar decoding
    # bits: input bits
    # return: decoded bits
    eng = matlab.engine.start_matlab()
    input_text= bits
    decoded_output = eng.decodePolar(matlab.int8(input_text),nargout=1)
    decoded_output =[[int(num) for num in x] for x in decoded_output]
    print(decoded_output)
    fileName = "polarDecoder"
    fileName+=secretCode+ ".pkl"
    create_pickle(fileName,decoded_output)
    eng.quit()
    return decoded_output
    