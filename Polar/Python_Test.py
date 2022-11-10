import sys
import matlab.engine

eng = matlab.engine.start_matlab()
eng.cd(r'C:\Users\Admin\DNA_Codec\Polar', nargout=0)
eng.my_main(nargout=0)
eng.quit()