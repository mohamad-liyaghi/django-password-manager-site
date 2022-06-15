import base64

def encode(password):
    '''
        Encode a password to base64
    '''
    return base64.b64encode(password.encode())

def decode(password):
    '''
        Decode a password from base64
    '''
    return base64.b64decode(password.replace('b','').replace("'",""))