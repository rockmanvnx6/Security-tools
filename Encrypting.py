import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def keyIn(console):
    console = input("Type command here. Type /help to see available commands: ")
    return console

def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
store = []
def primeFactorize(n):
    print("Calculating...")
    for i in range(2,9999):
        if(is_prime(i)):
            store.append(i)
    for i in store:
        for a in store:
            if(a != i):
                if (a*i == n):
                    return a,i;


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def L(u,n):
    return (u-1)/n
console = None
console = keyIn(console)
while(True):
    if(console == "/help"):
        print("")
        print("Available mode: ")
        print("[+] /rsa to start rsa mode")
        print("[+] /b-rsa to start cracking mode")
        print("[+] /elgamal to start elgamal mode")
        print("[+] /paillier to start paillier mode")
        print("")

        console = keyIn(console)

    elif(console == "/rsa"):
        print("----- RSA -----");
        p = input("Enter p: ")
        q = input("Enter q: ")
        e = input("Enter e (leave blank to choose the smallest) : ")
        M = input("Enter message (leave blank if none): ")
        p = int(p)
        q = int(q)
        n = p*q
        fin = (p-1)*(q-1)
        if(e == ""):
            for i in range(1,999):
                if(i > 1 and math.gcd(i,fin) == 1):
                    e = i;
                    break;
        else:
            e = int(e)
        if(M != ""):
            M = int(M)
            C = (M**e)%n
            d = modinv(e,fin)
        else:
            C = None
            d = "No Message, not Available"
        print("")
        print("Result:")
        print("[+] n = " + str(n))
        print("[+] e = " + str(e))
        print("[+] fin = " + str(fin))
        print("public-key: (" + str(n) + "," + str(e) + ")")
        print("private-key: d = " + str(d))
        print("Encrypted Message: " + str(C));
        print()
        print("---- TEST CORRECTNESS ----")
        print()
        test = (C**d)%n
        print("Taking private key (" + str(d) + ") decrypting (" + str(C) + ")")
        print("Decrypted Message: " + str(test));
        if(test == M):
            print("Test positive, calculation is correct !")
        else:
            print("Test negative, please use tool online")
        print("")
        console = keyIn(console)

    elif(console == "/b-rsa"):
        print("----- BREAKING RSA -----");
        n = input("Enter n: ")
        n = int(n)
        e = input("Enter e: ")
        e = int(e)
        C = input("Enter C: ")
        C = int(C)
        p,q = primeFactorize(n);
        fin = (p-1) * (q-1)
        d = modinv(e,fin)
        M = (C**d) % n
        print()
        print("Result:")
        print("[+] p = " + str(p))
        print("[+] q = " + str(q))
        print("[+] fin = " + str(fin))
        print("Private key d = " + str(d))
        print("Decrypted Message: " + str(M))
        console = keyIn(console)
    elif(console == "/elgamal"):
        print("----- ELGAMAL ENCRYPTION -----")
        p = input("enter p: ")
        p = int(p)
        g = input("enter g: ")
        g = int(g)
        x = input("enter x: ")
        x = int(x)
        r = input("enter r: ")
        r = int(r)
        m = input("enter m: ")
        m = int(m)

        y = (g**x)%p
        k = (y**r)%p
        C1 = (g**r)%p
        C2 = m*k%p
        mod_inv_k = modinv(k,p)

        print("--- Calculation ---")
        print("")
        print("Initial: ")
        print(" - p:" + str(p))
        print(" - g:" + str(g))
        print(" - x:" + str(x))
        print(" - r:" + str(r))
        print(" - m:" + str(m))
        print("")
        print("Key generation: ")
        print("[+] y: " + str(y))
        print("")
        print("Sender side Encryption")
        print("[+] k: " + str(k))
        print("[+] C1: " + str(C1))
        print("[+] C2: " + str(C2))
        print("")
        print("Receiver side decryption")
        print("[+] k: " + str((C1**x)%p))
        print("[+] mod_inv k: " + str(mod_inv_k))
        test = mod_inv_k * C2 % p
        print("[+] message: " + str(test))
        if(int(test) == m):
            print("---SUCCESSFULLY---")
        else:
            print("Failed !")
        console = keyIn(console)


    elif (console == "/paillier"):
        print("----- PAILLIER ENCRYPTION -----")
        p = input("enter p: ")
        p = int(p)
        q = input("enter q: ")
        q = int(q)
        g = input("enter g: ")
        g = int(g)
        r = input("enter r: ")
        r = int(r)
        m = input("enter m: ")
        m = int(m)

        n = p*q;
        halflife = int(lcm(p-1,q-1))
        target = (g**halflife)%(n**2)
        k = int(L(target,n))
        u = int(modinv(k,n))

        print("--- Calculation ---")
        print("")
        print("Initial: ")
        print(" - p:" + str(p))
        print(" - q:" + str(q))
        print(" - g:" + str(g))
        print(" - r:" + str(r))
        print(" - m:" + str(m))
        print("")
        print("Public key generation by receiver: ")
        print("[+] n: " + str(n))
        print("[+] Public key (n,g): ("+str(n) + "," + str(g)+")")

        print("")
        print("Private key generation by Receiver")

        print("[+] lambda: " + str(halflife))
        print("[+] k: " + str(k))
        print("[+] u: " + str(u))
        print("[+] Receiver saves private key: (" + str(halflife) + "," + str(u) +")")


        print("")
        print("Sender side encryption")
        c = (g**m)*(r**n)%(n**2)
        print("[+] with r = " + str(r) + "; we have c = " +str(c))

        print("")
        print("Receiver decryption")
        test_c = (c**halflife)%(n**2)
        test = int(L(test_c,n) * u % n)
        print("[+] message: " + str(test))
        if (int(test) == m):
            print("---SUCCESSFULLY---")
        else:
            print("Failed !")
        console = keyIn(console)



    else:
        print("Invalid argument!")
        console = keyIn(console)
