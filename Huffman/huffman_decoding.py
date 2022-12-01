import os
import sys
sys.path.insert(1, os.getcwd())
from Pickle.extractData import *

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        # freqability of symbol
        self.freq = freq
        # symbol 
        self.symbol = symbol
        # left node
        self.left = left
        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

def Huffman_Decoding(secretCode, encoded_data):
    fileName1 = "Huffman_encoder_tree"
    fileName1+=secretCode+".pkl"
    huffman_tree = extract_pickle(fileName1)
    tree_head = huffman_tree
    
    print(huffman_tree)

    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right   

        elif x == '0':
            huffman_tree = huffman_tree.left
        
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    print(decoded_output)
    string = ''.join([str(item) for item in decoded_output])
    fileName3 = "Huffman_decoder"
    fileName3+=secretCode+".pkl"
    create_pickle(fileName3,string)
    print("Hello")
    print(string)
    return string

if __name__ == "__main__":
    Huffman_Decoding("rGcpYx2740", "00101000110110")