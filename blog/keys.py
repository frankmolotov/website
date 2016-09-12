import random

def get_encrypted_key(key):
    file = open(key, 'r')
    information = file.readlines()
    return information

key = 'test.txt'
print(get_encrypted_key(key))