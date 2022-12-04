# Adding current folder to the system path
import os
import sys
sys.path.insert(1, os.getcwd())

# A simple script to calculate BMI
from pywebio import *
from pywebio.input import input, FLOAT, input_group
from pywebio.output import put_text, put_markdown, put_scrollable, put_scope
from Huffman.huffman_encoding import *
from Polar.Polar import *
from PGP.PGP_encrypt import *
from PGP.decrypt import *
from Ternery_ACGT.ternary2ACGT import *
from Ternery_ACGT.ACGT2Ternary import *
from Bin_Ternery.binary2Ternary import *
from Bin_Ternery.ternary2Binary import *
from Pickle.extractData import *
from Ascii_Bin.Ascii_2_Bin import *
from Ascii_Bin.Bin_2_Ascii import *
from Huffman.huffman_decoding import *
import random  
import string

def main():
    info = input_group("Code Info",[
  input('DNA String', name='dna'),
  input('Secret Code', name='code')
])  
    
    ACGT = info['dna']
    secret_code = info['code']

    f = open("Polar/decode_code.txt", "w")
    f.write(secret_code)
    f.close()

    Ternery = acgt2ternary(secret_code)
    PGP = ternary2binary(secret_code)
    binary_2_ascii(secret_code)
    polar = decryptData(secret_code)
    huffman1 = decode(secret_code)
    
    print(huffman1)
    fileName = "polar_length"
    fileName += secret_code+".pkl"
    LIM = extract_pickle(fileName)

    huffman1 = huffman1[0][:LIM]
    
    huffman = ""
    for x in huffman1:
        huffman += str(x)
    print(huffman)
    org = Huffman_Decoding(secret_code, huffman)

    put_markdown('# Final Text')
    put_scrollable(put_scope('scrollable1'), height=200, keep_bottom=True)
    put_text(org, scope='scrollable1')

    put_markdown('# Blockwise Ouput')    
    
    put_markdown('**Original DNA String**')
    put_scrollable(put_scope('scrollable2'), height=100, keep_bottom=True)
    put_text(ACGT, scope='scrollable2')
    
    put_markdown('**ACGT to Ternery**')
    put_scrollable(put_scope('scrollable3'), height=100, keep_bottom=True)
    put_text(Ternery, scope='scrollable3')
    
    put_markdown('**Ternery to Binary**')
    put_scrollable(put_scope('scrollable4'), height=100, keep_bottom=True)
    put_text(PGP, scope='scrollable4')
    
    put_markdown('**PGP Decryption**')
    put_scrollable(put_scope('scrollable5'), height=100, keep_bottom=True)
    put_text(polar, scope='scrollable5')
    
    put_markdown('**Polar Decoding**')
    put_scrollable(put_scope('scrollable6'), height=100, keep_bottom=True)
    put_text(huffman, scope='scrollable6')
    
    put_markdown('**Huffman Decompression**')
    put_scrollable(put_scope('scrollable7'), height=100, keep_bottom=True)
    put_text(org, scope='scrollable7')
    


start_server(main, port=8081, remote_access=True,debug=True)
