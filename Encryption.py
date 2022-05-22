from cryptography.fernet import Fernet

'''
    Encryption class
'''


class encryption:
    def __init__(self):
        '''
		@Definition: Initializes an encryption class
		@preconditions: None
		@postconditions: An encryption object is initialized along with filename argument
		@:arguments: filename
		@:return: None
		@algorithm
        		Variable @filename will be used to indicate what file is being encrypted/decrypted
	'''
        try:
            self.load_key()
        except:
            self.key = Fernet.generate_key()
            self.write_key()

    def write_key(self):
        """
		@Definition:  Creates a key that will be used in the encryption and decryption process
		@preconditions: None
		@postconditions: A file is created that contains the key
		@:arguments: None
		@:return: None
		@algorithm
                	The key is generated and then stored within a file called 'key.key'
	    """
        with open("key.key", "wb") as key_file:
            key_file.write(self.key)

    def load_key(self, filename="key.key"):
        '''
		@Definition:  Reads the key from the file 'key.key'
		@preconditions: File 'key.key' must exist
		@postconditions: Key is useable in function that it is called
		@:arguments: None
		@:return: None
		@algorithm
               		When called, the file 'key.key' is read
	'''
        self.key = open(filename, "rb").read()

    def __encrypt__(self, filename):
        '''
		@Definition:  Encrypts designated file
		@preconditions: File for encryption and 'key.key' must exist
		@postconditions: Designated file is encrypted
		@:arguments: filename
		@:return: None
		@algorithm
                	The key is read, then the designated file is read, then the file is encrypted using the key
	'''
        f = Fernet(self.key)
        with open(filename, "rb") as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)

    def __decrypt__(self, filename):
        """
		@Definition:  Decrypts designated file
		@preconditions: File for decryption and 'key.key' must exist
		@postconditions: Designated file is decrypted
		@:arguments: filename
		@:return: None
		@algorithm
                	The key is read, then the designated file is read, then the file is decrypted using the key
	    """

        f = Fernet(self.key)

        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)

        with open(filename, "wb") as file:
            file.write(decrypted_data)


def main():
    filename = 'test.py'
    encryptor = encryption()
    encryptor.__encrypt__(filename)

    # encryption.write_key()
    # encryption.load_key()
    # encryption.__encrypt__(filename)
    with open(filename, "r") as file:
        encrypted_data = file.readlines()
    print(encrypted_data)

    encryptor.__decrypt__(filename)
    # encryption.__decrypt__(filename)
    with open(filename, "r") as file:
        decrypted_data = file.readlines()
    print(decrypted_data)


if __name__ == "__main__":
    main()
