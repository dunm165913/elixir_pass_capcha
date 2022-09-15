import base64
from PIL import Image
import pytesseract
import math

# from operator import itemgetter
# import hashlib
# import time


# imgdata = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAKAAAAAyCAIAAABUA0cyAAAFi0lEQVR4Xu2YYXLbOgyEc93+6yV8xZ4g92AjggTBXQCSZal1MvyGk6GAJQhhY6fvfXwsfjzl80+xxI+P3792sgf5/KNi2TxxNuaryFSn9wZ33Q6MyOVLs7fatF9Yy+B7gBG55Jqafb3bZfA95OYJuWYZ7LIMBpbB9xCZ94l/I/PVpv3CWgbfA4xIsfFII9Ts690ug+8hMm8Z/CLLYGAZfA+ReUcM/hx/Qdu0IfIMy+B7SMxz9xaJ15/cLUdylsH3kJvHe8syOMExOF6X3OjDIzq12rT3VvIiLxhM19y3khcAHIN7HDawv5h+Lz7aOGgUidef3CFHoqAwDJbRtAHtPW5HvaaTm9QtXa1U3+gjryTFSigrl2tjtsOs2xfp9+Kjjdd9m79FNPUnd8iRKCh0g4GoP/voNZ3cxEVg6MnZJAU0g/v+bQ1uc++ocGj+i8FN+RMN9udwGnpZ2HRnB6r9bwZP7XRADDdFMnm83uBnvsxBbN4pg4ska7T9iQYXmqfGm6b+5BfnSBQUqLpg+pDHqRcDiPWmXCaPNxk8le2Xwl28h4YjVL9DvXfo39zgqZEZEC+DC5XaQgcMbsqqkc7lXXhtReblBmXNpZXZDNuB7jVixcnIoGZrqyIbexZIUhNnDYZWE/SsC6o7493tEOh70aZEefDFExmVFkwf0IF9lMjPM1gFzwJ1LE3xbgbz9TbSgqcMhuwXSZeQsqds3DVYItESpS2INY9TXYFSlmabWaggjbwCRipNX4H5WHpdoJsxLu5oZMSNc/YmUDaxF1f0LHCk7IZn8NjPG0tY8CnqXVAKsLNy9SNVs9AtiAWWWYZogu7WjA22eGBw8cQQYexxJTHYDQqnDQZQHUFDc8n1IzUbDDKLlTFDNDF/e1gLbXxLVbFmjxtc+qfN5BsSjxaqUy4xWMAzTL+LD0JEgq7BI2UMRsX8a60yl+kARjV1kcGCZvPuLbYsqist5/5Vmyu4s8AzAXgMiA32G0v1ajBk3f7doNCO+VEzOIhPgtcMZpkKlNzgoavfCm72EoM/vN4GMofIy8Px5m6Q2vo3AlkQdMalzyNk44HBkC3e+PwjlUsMNqpmsKvZNRhDFagTyRrd4EIHowFuKTcoVlGqBP1D0BkXPs/BqD/IFrqpREcqkcEgK8eVZw1O4FIhucF9QUqyHHGCFbf/kwbv0s68bPAj+F5VIoNnlf8VLbLTBpfdS5XY4HEqyALvYrCix93rd8XsimpUIJtc5hosmX9scGSPfhggy3CFLRj0vwwODXaKzEC1TP+MwcWrbHE/64X6F243+EH/tWrXQTHItKVys8FWxphKmWwjNbidNQa7FiputlD/gqQUqxknJ2wfBnuZRQXR9a4ehu5qhsAdWf1bZddpg0Hvpj54UJbZ4EIVRtbqSaa4KZ6wpjRymcEtasR8veAefNFgK2hcYXCCPehw1uDCSvl9rd1CKkGrvbvBeko5bjBqem+RwYV6S4CDyJ7BW4XAYDFySnWDi1eHGWff1uCEWw0u1B6DB1zIYLFtqhMbPOIFDS57HcJxx+AH/ZPHXVPVw6f44FNnjy/XYEcWA8e3Cse502ABq3VAZh9R2rB9MPZNZrBRw25bCWIeRpljBv/LBf18PP+bDa/IEQ7ax5O3PurEObjFI8ihTDwj12GUof/Prvvjd53H+wSXPuJJQ3tsr36CebYnVjN4qi4XJMSf4AzSPw4PfVPScYfZ4Gh/F4HBB60yhZxZKaj0gvZxGXwds8GTef3RxhPjk9Szaxl8HTSWcakG7VskbxSn3BeBoH1cBl8HjcUa/KDP1rVLL53uXQZfCY3FudS+RfJGccqpSXxXg+F3ltcyWLCa72PwEb6DwfDrePdaBl8HjWXnUhrIIE7t1KxYTTN48YP5C1h1TXOwN3oUAAAAAElFTkSuQmCC")
# filename = 'input.jpg'  # I assume you have a way of picking unique filenames
# with open(filename, 'wb') as f:
#     f.write(imgdata)
im = Image.open("input.jpg")
im = im.convert("P")
his = im.histogram()

im2 = Image.new("P",im.size,255)
temp = {}

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        temp[pix] = pix
        if pix == 0:
            im2.putpixel((y,x),0)

im2.save("output.gif")

print(pytesseract.image_to_string('output.gif'))

