"""
Convert hex to base64

Input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

"""
import base64

def main():
    data = raw_input('enter hex input: ')
    convert(data)

def convert(data):
    bitData = int(data, 16)
    print bitData
    encoded = base64.b64encode(bitData)
    
    return '%s' % encoded 


if __name__ == '__main__':
    main()
