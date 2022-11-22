import matlab.engine
eng = matlab.engine.start_matlab()
eng.cd('Polar', nargout=1)
input_text= [1, 0, 0, 1, 0, 1]
[encoded_output,decoded_output] = eng.codecPolar(matlab.int8(input_text),nargout=2)
encoded_output =[[int(num) for num in x] for x in encoded_output]
print(encoded_output)
eng.quit()
