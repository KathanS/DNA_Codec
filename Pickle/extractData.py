import pickle

def create_pickle(filename,obj):
    
    fileobj=open(filename,'wb')
    pickle.dump(obj,fileobj)
    fileobj=open(filename,'rb')
    fileobj.close()

def extract_pickle(filename):
    fileobj=open(filename,'rb')
    ans = pickle.load(fileobj)
    fileobj.close()
    return ans


