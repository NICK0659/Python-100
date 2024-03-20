def disply_caesarcipher():
    print("     ")
    
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("type ENCODE for Encoding and DECODE for Decoding")
text=input("Enter your message")
shift=int(input("enter the shift number"))

def encode(plain_text,shift_number):
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_number
        new_letter=


