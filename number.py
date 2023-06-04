import pickle

class Number:
    @staticmethod
    def oct_number(a):
        b = oct(a)
        return b

    @staticmethod
    def hex_number(a):
        b = hex(a)
        return b

    @staticmethod
    def bin_number(a):
        b = bin(a)
        return b

    @staticmethod
    def save(a):
        with open('file.txt', 'wb') as f:
            pickle.dump(a, f)

    @staticmethod
    def read():
        with open('file.txt', 'rb') as f:
            pickle.load(f)

