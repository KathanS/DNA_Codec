def encode(bits):
    # Polar encoding
    # bits: input bits
    # return: encoded bits
    import matlab.engine
    eng = matlab.engine.start_matlab()
    eng.cd(r'C:\Users\Admin\DNA_Codec\Polar', nargout=0)
    eng.encoder(bits)
    eng.quit()

def decode(bits):
    # Polar decoding
    # bits: input bits
    # return: decoded bits
    import matlab.engine
    eng = matlab.engine.start_matlab()
    eng.cd(r'C:\Users\Admin\DNA_Codec\Polar', nargout=0)
    eng.decoder(bits)
    eng.quit()