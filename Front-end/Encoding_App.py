# Adding current folder to the system path
import os
import sys
sys.path.insert(1, os.getcwd())

# A simple script to calculate BMI
from pywebio import *
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_markdown, put_scrollable, put_scope
from Huffman.huffman_encoding import *
from Polar.Polar import *
from PGP.PGP_encrypt import *
from Ternery_ACGT.ternary2ACGT import *
from Bin_Ternery.binary2Ternary import *
from Pickle.extractData import *
from Ascii_Bin.Ascii_2_Bin import *
import random  
import string

def secret_code_generator():  
    letter_count = 6
    digit_count = 4
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))
    return str1

def main():
    txt = input("Text")
    secret_code = secret_code_generator()

    f = open("Polar/encode_code.txt", "w")
    f.write(secret_code)
    f.close()

    huffman = Huffman_encoding(txt,secret_code)
    
    fileName = "polar_length"
    fileName += secret_code+".pkl"
    create_pickle(fileName,len(huffman))
    
    polarL = encode(secret_code)
    polar = ''.join([str(x) for x in polarL[0]])
    encrypt_data(secret_code)
    PGP = ascii_2_binary(secret_code)
    Ternery = binary2ternary(secret_code)
    ACGT = ternary2acgt(secret_code)
    
    put_markdown('# Final DNA String')
    put_scrollable(put_scope('scrollable1'), height=200, keep_bottom=True)
    put_text(ACGT, scope='scrollable1')

    put_markdown('**Secret Code to be used for Decoding**')
    put_scrollable(put_scope('scrollable8'), height=100, keep_bottom=True)
    put_text(secret_code, scope='scrollable8')


    put_markdown('# Blockwise Ouput')    
    
    put_markdown('**Original Text**')
    put_scrollable(put_scope('scrollable2'), height=100, keep_bottom=True)
    put_text(txt, scope='scrollable2')
    
    put_markdown('**Huffman Compression**')
    put_scrollable(put_scope('scrollable3'), height=100, keep_bottom=True)
    put_text(huffman, scope='scrollable3')
    
    put_markdown('**Polar Encoding**')
    put_scrollable(put_scope('scrollable4'), height=100, keep_bottom=True)
    put_text(polar, scope='scrollable4')
    
    put_markdown('**PGP Encryption**')
    put_scrollable(put_scope('scrollable5'), height=100, keep_bottom=True)
    put_text(PGP, scope='scrollable5')
    
    put_markdown('**Binary to Ternery Conversation**')
    put_scrollable(put_scope('scrollable6'), height=100, keep_bottom=True)
    put_text(Ternery, scope='scrollable6')
    
    put_markdown('**Ternery to ACGT**')
    put_scrollable(put_scope('scrollable7'), height=100, keep_bottom=True)
    put_text(ACGT, scope='scrollable7')

start_server(main, port=8080, remote_access=True,debug=True)