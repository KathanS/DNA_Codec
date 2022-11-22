import matlab.engine

eng = matlab.engine.start_matlab()
eng.cd('Polar', nargout=1)



def encode(bits):
    # Polar encoding
    # bits: input bits
    # return: encoded bits
    input_text= bits
    encoded_output = eng.encodePolar(matlab.int8(input_text),nargout=1)
    encoded_output =[[int(num) for num in x] for x in encoded_output]
    print(encoded_output)
    eng.quit()
    return encoded_output
   

def decode(bits):
    # Polar decoding
    # bits: input bits
    # return: decoded bits
    eng = matlab.engine.start_matlab()
    input_text= bits
    decoded_output = eng.decodePolar(matlab.int8(input_text),nargout=1)
    decoded_output =[[int(num) for num in x] for x in decoded_output]
    print(decoded_output)
    eng.quit()
    return decoded_output
    