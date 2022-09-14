#!/usr/bin/python3
import pyAesCrypt
import sys
from argparse import ArgumentParser
class Aesmyfile:
    def encrypt_file(self,key,source):
        outfile=source+".enc"
        pyAesCrypt.encryptFile(source, outfile, key)
        return outfile
    
    def decrypt_file(self,key,source):
        decrypted_file = source.split(".")
        outfile = f"dec_{decrypted_file[0]}.{decrypted_file[1]}"
        pyAesCrypt.decryptFile(source, outfile, key)
        return outfile
    
if __name__ == '__main__':
    
    parser = ArgumentParser(description="AES file encryptor/decryptor\nBy:A$TRA", epilog="Example: %(prog)s -e -f file.txt -p xN3#@Y0!")
    parser.add_argument('-e', '--encrypt', action='store_true', help='encrypt a file')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt a file')
    parser.add_argument('-f', '--filename', help='filename')
    parser.add_argument('-p', '--password', help='password')
    args = parser.parse_args()

    aesmyfile = Aesmyfile()
    filename = args.filename
    key = args.password

    if(len(sys.argv)) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    if args.encrypt:
        try:
            aesmyfile.encrypt_file(key, filename)
            print("File encrypted successfully!")
        except Exception as err:
            print("An error occurred!")
    if args.decrypt:
        try:
            aesmyfile.decrypt_file(key, filename)
            print("File decrypted successfully!")
        except Exception as err:
            print("An error occurred!")
