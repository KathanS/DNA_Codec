# A Huffman Tree Node
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

""" A helper function to print the codes of symbols by traveling Huffman Tree"""
codes = dict()

def Calculate_Codes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)
    
    if(node.left):
        Calculate_Codes(node.left, newVal)
    if(node.right):
        Calculate_Codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal
         
    return codes        

""" A helper function to calculate the freqabilities of symbols in given data"""
def Calculate_freqability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else: 
            symbols[element] += 1     
    return symbols

""" A helper function to obtain the encoded output"""
def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
      #  print(coding[c], end = '')
        encoding_output.append(coding[c])
        
    string = ''.join([str(item) for item in encoding_output])    
    return string
        
def Huffman_Encoding(data):
    symbol_with_freqs = Calculate_freqability(data)
    symbols = symbol_with_freqs.keys()
    freqabilities = symbol_with_freqs.values()
    print("symbols: ", symbols)
    print("freq: ", freqabilities)
    
    nodes = []
    
    # converting symbols and freqabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_freqs.get(symbol), symbol))
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their frequency
        nodes = sorted(nodes, key=lambda x: x.freq)
        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]
    
        left.code = 0
        right.code = 1
    
        # combine the 2 smallest nodes to create new node
        newNode = Node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
            
    huffman_encoding = Calculate_Codes(nodes[0])
    print("symbols with codes", huffman_encoding)
    encoded_output = Output_Encoded(data,huffman_encoding)
    return encoded_output, nodes[0]  
    
 
   


def Huffman_encoding(data,secretCode):

    encoding, tree = Huffman_Encoding(data)
    fileName1 = "Huffman_encoder"
    fileName1+=secretCode+".pkl"
    create_pickle(fileName1,encoding)
    fileName2 = "Huffman_encoder_tree"
    fileName2+=secretCode+".pkl"
    create_pickle(fileName2,encoding)
    return encoding


