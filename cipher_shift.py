alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# UMYTMHUZSRGZ
def cipher_shift(text,n):
    text = text.upper()
    string = ""
    n = int(n)
    for i in text:
        if(i == " "):
            string += " "
        else:
            ind = alphabet.index(i)
            if(ind-n >= len(alphabet)):
                string += alphabet[ind-n - len(alphabet)]
            else:
                string += alphabet[ind-n]
    return string

text = input("Enter the text: ")
n = input("Enter shift-level (leave blank for brute-force): ")
if(n == ""):
    for i in range(0,26):
        print(cipher_shift(text, i) + " --- n: "+str(i))
else:
    print(cipher_shift(text,n))