import base64
import sys
rot13encode = str.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
rot13decode = str.maketrans(
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")
def encode(key, deger):
    encoded_chars = []
    for i in range(len(deger)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(deger[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_deger = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_deger)
def decode(key, deger):
    decoded_chars = []
    deger = base64.urlsafe_b64decode(deger)
    for i in range(len(deger)):
        key_c = key[i % len(key)]
        encoded_c = chr(abs(ord(deger[i]) - ord(key_c) % 256))
        decoded_chars.append(encoded_c)
    decoded_deger = "".join(decoded_chars)
    return decoded_deger


while True:
    print("İşlem Menüsü \n (1) Base64 \n (2) ROT13 \n (3) Vigenere \n (4) Çıkış")
    islem=input("Bir işlem numarası yazınız : ")
    if islem == "1":
        while True:
            menu=input("Ne yapmak istiyorsunuz ?? \n (1) Encode \n (2) Decode \n (3) Geri \n (4) Çıkış \n Bir işlem numarası yazınız : ")
            if menu=="1":
                girismetin = input("Bir metin girin : ")
                print(base64.b64encode(girismetin.encode()))
            elif menu=="2":
                girismetin = input("Bir metin girin : ")
                print(base64.b64decode(girismetin))
            elif menu=="3":
                break
            elif menu=="4":
                sys.exit()
            else:
                print("Lütfen geçerli bir işlem numarası giriniz.")
    elif islem == "2":
        while True:
            menu=input("Ne yapmak istiyorsunuz ?? \n (1) Encode \n (2) Decode \n (3) Geri \n (4) Çıkış \n Bir işlem numarası yazınız : ")
            if menu=="1":
                girismetin = input("Bir metin girin : ")
                print(str.translate(girismetin, rot13encode))
            elif menu=="2":
                girismetin = input("Bir metin girin : ")
                print(str.translate(girismetin, rot13decode))
            elif menu=="3":
                break
            elif menu=="4":
                sys.exit()
            else:
                print("Lütfen geçerli bir işlem numarası giriniz.")
    elif islem == "3":
        while True:
            menu=input("Ne yapmak istiyorsunuz ?? \n (1) Encode \n (2) Decode \n (3) Geri \n(4) Çıkış \n Bir işlem numarası yazınız : ")
            if menu=="1":
                deger = input("Thing to encode:")
                key = input("key:")
                encrypted = encode(key, deger)
                print(encrypted)
            elif menu=="2":
                deger = input("Thing to decode:")
                key = input("key:")
                decrypted = decode(key, deger)
                print(decrypted)
            elif menu=="3":
                break
            elif menu=="4":
                sys.exit()
            else:
                print("Lütfen geçerli bir işlem numarası giriniz.")
    elif islem=="4":
        sys.exit()
    else:
        print("Lütfen geçerli bir işlem numarası giriniz.")