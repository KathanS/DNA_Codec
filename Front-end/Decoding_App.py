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

    huffman = "1100110101011011110111110100001001100"
    polar = "1 1 0 1 1 0 0 0 1 1 1 0 0 1 0 0 1 0 0 0 0 0 1 0 0 1 1 1 0 0 1 0 0 1 0 0 1 1 1 0 1 0 1 1 1 1 1 0 1 1 0 1 1 0 0 0 1 1 1 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 0 1 0 1 0 1 1 1 0 0 0 1 1 1 0 0 0 1 0 1 0 0 0 0 1 0 0 1 1 0 1 1 1 1 0 0 1 1 1 0 1 0 0 1 1 1 0 0 0 1 0"
    PGP = "01101000010001100011010001000100011000100011000001000101011001100100001101010110010110100011000101010111011011100101000101010011010000010101000101100100010000010111010000110011001101000011001001100010001100000101100000110000011110100101011101110111010101010111100001110110011100010011000101011001011011110100000100110100010001100110110100110001001011110110010001110011011011110110011001001111011110010111001101010000010100010110001101001110010100010101100101100100001011110110001101000110011010010110101101110111000010100110110000110100010001000011011000110111011010110100001001101101001110000110101101001000010110000100011000110011011000110101100100110001010010100100111001100001001010110110000101110010010000110111011101101100010110100100110100110100011000100111001101111000010011100100000101110001010011100100000100110111011110100110111000110011001100100101000101000011010011110111011001101000010010100011010101100111001100010010101101011001001100000100011101001111010101010100011101110101011001010011000001100011010101000011100100001010001100010100110101000001011000110100000101010001011010110100001101000101010011000101100101101001010001100101010101001000010010010110011101001100011010110010101100111001010100000011011001001010010000010100110100110110001101000011010000110101010011010111100101111000010100000010111101110011011110000011100101011010011001110101100101001100011011110100001101110111011110000100000101111000011110000101000101010101011001010110001001011000010010110110001101100111010100000101001001110011011000110110000100110010001101100000101000110000011011110101000000110001001100010101010101010110001100010101011101111010001100010011100001001100010011110011011101111010010100010111101001100110011011110100110101001110010101100100010101101110011011100100011101101100010110010111011101111001001101110100110101010011011001100011100001100111010000010011011101000111001100100100011101110000010101110110111000110111001100110110110001001110010000010111000001111001011011110100001000110101001100000111011101000001010101000011010101000001011010010011000001000010000010100101100001101110011110010100101001100110010010010100001001000110011110000110001001011010001100100111011101000011011011100101100001000101010000100101100100110010011101000101011000110111001101000011100101100110010000100110011101010010010100000111100001110000011001000110001001001111010000010100111100110011010010100101010001000010011100100101001101000010011100110110111001010010011010000100010001001001010011110111011101010001011110010011010101001000010110010110110001101101001101000100110001010111001010110110101100001010010011110100100101001111001101000110111101001110010100100111000101101110010101010111010101101001011011110110000101011010001101000100101001101111010100100101010001100011010110000011011001010110011011100110011001111000010100010111100101101111010101010011000101000100011101000101011001000111010101100011000000101011011000010101001101000100011100100101011101000011011010000111101000110010011100100110101001110101010001110111011001010000011010100100111101010101011110000111011001100111011100110111000101111001011000010000101001000010011011100101100101101010010101110110101100110011001100110011100101100101010011100011100001001100001101110110100001010101011011100011000101010010001101010110100100110100011101010011100101010011010100110101010101101000010011000101011101101100010100110111100101011000011011100101100000111001011101110111101001011001011011000100000100111101001111010000101000111101010000010100101001101101011001010000101000101101001011010010110100101101001011010100010101001110010001000010000001010000010001110101000000100000010011010100010101010011010100110100000101000111010001010010110100101101001011010010110100101101"
    Ternery = "01211100011001210012111001100110012100110012100001100111112101210110001211111121011121110012100111111122112112210111100111111012111000011111100111210110011000011122111000121012101211100012101101210011001210000111210000121000012221110111112211221122111111111122210001221121012210011012100111112101112112221110000110121110011001210121121110121001101112221121011001221012112112221121012101101222112221011122101211111000011110011121001211101221011110011111210111210110001112221121001211100121012111011121111211221122100011110121121000121110011001100012112100121122112111121110001101211211101221000121111211101100011121000110012100121012112100121111210110121001111011110110122101210001101111121121000111221011011000121122112211211210011121110110121110121110012100110122101211222100011012210110000111221001111012210110000110121122112221110121122100121012101210110111100111100012111012221122112101211100011011110012111111210122101210011011111211112101101210000110012211101222111111111110012211221111112101111012100001210012111111100012210110001111001210011110121111100001112100121110000111111001112111121110001211100111111012100111210111211101111001210111111111101100011011011121012211101210012111121011111210122101111110000012112101101111011000011110121110121121001211100012111000121111111012111122210111222100011110000011122211221012112221000012210111112111012101221111210111101210012112221110001211221122112221000110000111222100012221000111100111111111112101111121001101112100011011121121001211210122111110000111101101221012112100121121000110121011001211210000111100121000012112221111100000121001101210011111111111111121001210011111112211222111001210011012210001101210011012221012112211222111011110011122211101210121012112221110121111101221011111210110011111211221012112210110012211211210011121011122112211222101101211221110121111111012112101210012210001210122111000011012112211100122101210110110012211221000011111221121122100121122101210121121121001101221011000011122100001222101112112221110001100121111101210000122112211100001111111100012111111100001112111011012100001100011000011110111210001211221012221011110111101210121011011011110001101100121012221000121001101112111001210110122112211100012112112210111210001100111111000110111210110121011012211100111112100121122101211100012210111210121011000110121012211111011011110000122210001221000012101100121001101101222111000011110122210121012111011110111111001100011012210110111101211100011012210121121122101111011012111000110011001101101111012221122112211111001112221011012111111101100011121011121121001211211101211100110121001111122101111121121111210001111011012221110110111101222101211100121122211101221011110110122100111211221011111111122111111211101112112221121000111112111001211100110111101211222111110110111111001210012111121000012112101111121012112210121012101222100011110011122210111211222111111111012100111100110012211100111112101100122111111210012100000111112112100011111101211100110012210110111112211100012112111000122211100121011012210110121111101221111111001221122112101111000012111110110122211111111112221000122112101210122112210121122100111222101112100011000111101100011012112210111210111211111011111221121111210121012101210121012210111210111111012210012210001101210001211221121110001111111112112210012100111111011001211111121110110121110012211111012210111111012111110121111111111211100011012100111112211211210011110121122210111112100012112210111210000122101112211221122211101112101112112100110000110122211101222111000111100122211111000011110111101211211112101111000111100111211101112111011121110111211101112111110011111101221011001100011000001111000011001221111100000110000011012111110011111111012111110121110000111100122111001111011121110111211101112111011121110111211"
    org = "Hello World!"

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