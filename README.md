# encrypting_image_pixels (main.py)

Encrypting part: (main.py)
A code that shuffles pixels of an image by a value that is input from the user, also a decrypting code is included.
When the user inputs an integer value,  it will be used as a seed value to generate another random hash that will move pixels according to it. 

Decrypting part: (unrandom.py)
With this code, the seed value is multiplied by -1, so if the same value used to encrypt is inserted in the decryption part we will retrieve the original image.


NOTE: Loss of color gradings will occur after the decryption process.
