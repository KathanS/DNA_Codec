import matlab.engine


def encode(bits):
    # Polar encoding
    # bits: input bits
    # return: encoded bits
   eng = matlab.engine.start_matlab()
   eng.cd('Polar', nargout=1)
   input_text= bits
   encoded_output = eng.encoderPolar(matlab.int8(input_text),nargout=1)
   encoded_output =[[int(num) for num in x] for x in encoded_output]
   print(encoded_output)
   eng.quit()
   return encoded_output

def decode(bits):
    # Polar decoding
    # bits: input bits
    # return: decoded bits
    import matlab.engine
    eng = matlab.engine.start_matlab()
    eng.cd(r'C:\Users\Admin\DNA_Codec\Polar', nargout=0)
    eng.decoder(bits)
    eng.quit()