import matlab.engine
eng = matlab.engine.start_matlab()
eng.cd('Polar', nargout=1)
input_text= [1, 0, 0, 1, 0, 1]
encoded_output = eng.encoderPolar(matlab.int8(input_text),nargout=1)
print(encoded_output)
eng.quit()
