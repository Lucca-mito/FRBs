import pickle
def pload(filename):
    return pickle.load(open('pickles/'+filename, 'rb'))

def pdump(obj, filename):
    pickle.dump(obj, open('pickles/'+filename, 'wb'))
