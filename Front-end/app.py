# A simple script to calculate BMI
from pywebio.input import input, FLOAT
from pywebio.output import put_text

def main():
    binstr = input("Text")
    binstr = 'ACGTACGT'
    put_text('DNA String: %s' % (binstr))
    
if __name__ == '__main__':
    main()