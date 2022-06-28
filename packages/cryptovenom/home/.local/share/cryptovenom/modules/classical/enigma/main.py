#!/usr/bin/python

#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#                    [====={ CRYPTO VENOM }=====]
#
#     | ATTENTION!: THIS SOFTWARE IS PART OF THE "CRYPTOVENOM FRAMEWORK" |
#
#              ( https://github.com/lockedbyte/cryptovenom )
#
#           << GNU PUBLIC LICENSE >>
#
#                               / CREATED BY LOCKEDBYTE /
#
#                  [ CONTACT => alejandro.guerrero.rodriguez2@gmail.com ]
#                  [ CONTACT => @LockedByte (Twitter) ]
#
#
# AND NOW...HERE THE CODE
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#

import base64
import base58
import binascii
from pycipher import Enigma
    

def text_to_bits(text, encoding='utf-8'):

    bits = bin(int(binascii.hexlify(text.encode(encoding)), 16))[2:]
    
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8'):

    n = int(bits, 2)
    
    return int2bytes(n).decode(encoding)

def int2bytes(i):

    hex_string = '%x' % i
    
    n = len(hex_string)
    
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
    
    

def enigmaencode(importx, infilepath, outfilepath, inputformat, exportx, settings, rotors, reflector, ringstellung, steckers, raw):

    if importx == 'file':
    
        f = open(infilepath, 'r')
        raw = f.read()
        f.close()
        
    elif importx == 'print':
    
        raw = raw
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    inp = raw
    
    if inputformat == 'base64':
    
        iput = base64.b64decode(inp)
        
    elif inputformat == 'raw':
    
        iput = inp 
    
    elif inputformat == 'base32':
    
        iput = base64.b32decode(inp)
    
    elif inputformat == 'base16':
    
        iput = base64.b16decode(inp)
    
    elif inputformat == 'base58':
    
        iput = base58.b58decode(inp)
    
    elif inputformat == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'hex':
    
        iput = inp.decode('hex')
    
    elif inputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'binary':
    
        iput = text_from_bits(inp)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    settings = settings.split(',')
    rotors = rotors.split(',')
    settings = tuple(settings)
    rotors = tuple(rotors)
    ringstellung = ringstellung.split(',')
    ringstellung = tuple(ringstellung)
    steckers = steckers.split(',')
    s = []
    x = 0
    for i in range(0,5):
        s1 = (steckers[x], steckers[x+1])
        s.append(s1)
        x += 2
        
    steckers = s
    
    output = Enigma(settings=settings,rotors=rotors,ringstellung=ringstellung,steckers=steckers).encipher(iput)

    if exportx == 'file':
    
        f = open(outfilepath, 'w')
        f.write(output)
        f.close()
        return True
        
    elif exportx == 'print':
    
        return output
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
        
        
def enigmadecode(importx, infilepath, outfilepath, outputformat, exportx, settings, rotors, reflector, ringstellung, steckers, raw):

    if importx == 'file':
    
        f = open(infilepath, 'r')
        raw = f.read()
        f.close()
        
    elif importx == 'print':
    
        raw = raw
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    settings = settings.split(',')
    rotors = rotors.split(',')
    settings = tuple(settings)
    rotors = tuple(rotors)
    ringstellung = ringstellung.split(',')
    ringstellung = tuple(ringstellung)
    steckers = steckers.split(',')
    s = []
    x = 0
    for i in range(0,5):
        s1 = (steckers[x], steckers[x+1])
        s.append(s1)
        x += 2
        
    steckers = s
    
    out = Enigma(settings=settings,rotors=rotors,ringstellung=ringstellung,steckers=steckers).decipher(raw)
    
    if outputformat == 'base64':
    
        output = base64.b64decode(out)
        
    elif outputformat == 'raw':
    
        output = out 
    
    elif outputformat == 'base32':
    
        output = base64.b32decode(out)
    
    elif outputformat == 'base16':
    
        output = base64.b16decode(out)
    
    elif outputformat == 'base58':
    
        output = base58.b58decode(out)
    
    elif outputformat == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'hex':
    
        output = out.decode('hex')
    
    elif outputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'binary':
    
        output = text_from_bits(out)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        

    if exportx == 'file':
    
        f = open(outfilepath, 'w')
        f.write(output)
        f.close()
        return True
        
    elif exportx == 'print':
    
        return output
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False

