from Pickle.extractData import *

def Huffman_Decoding(secretCode):
    tree_head = huffman_tree
    fileName1 = "Huffman_encoder_tree"
    fileName1+=secretCode+".pkl"
    huffman_tree = extract_pickle(fileName1)
    fileName2 = "pgpdecryption"
    fileName2 += secretCode+".pkl"
    encoded_data = extract_pickle(fileName2)
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
        
    string = ''.join([str(item) for item in decoded_output])
    fileName3 = "Huffman_decoder"
    fileName3+=secretCode+".pkl"
    create_pickle(fileName3,string)
    return string
