import hashlib
def instruction():
    print("-----COMMAND LIST-----")
    print("/md5 value")
    print("/sha256 value")
    print("/sha512 value")
    print("/md5-b value ----- brute force from 0 to value")
    print("/sha512-b value ---- brute force from 0 to value")
    print("/sha256-b value ---- brute force from 0 to value")

def takeInput(x):
    x = input("Type in command (/help): ");
    return x;

def printDict(dict,n):
    for i in range(0,n):
        print(i,dict[i])

store = {}

x = None
x = takeInput(x);
while(not False):
    if(x == "/help"):
       instruction()
       x = takeInput(x)

    elif (x.startswith("/md5-b")):
        target = x[7:]
        n = int(target) + 1
        for i in range(0,n):
            targetx = str(i).encode('utf-8')
            ans = hashlib.md5(targetx).hexdigest()
            store[i] = ans
        printDict(store,n)
        x = takeInput(x)

    elif (x.startswith("/sha256-b")):
        target = x[10:]
        n = int(target) + 1
        for i in range(0, n):
            targetx = str(i).encode('utf-8')
            ans = hashlib.sha256(targetx).hexdigest()
            store[i] = ans
        printDict(store, n)
        x = takeInput(x)

    elif (x.startswith("/sha512-b")):
        target = x[10:]
        n = int(target) + 1
        for i in range(0, n):
            targetx = str(i).encode('utf-8')
            ans = hashlib.sha512(targetx).hexdigest()
            store[i] = ans
        printDict(store, n)
        x = takeInput(x)

    elif(x.startswith("/md5")):
        target = x[5:].encode('utf-8')
        ans = hashlib.md5(target).hexdigest()
        print("md5: " + ans)
        x = takeInput(x)


    elif (x.startswith("/sha256")):
        target = x[8:].encode('utf-8')
        ans = hashlib.sha256(target).hexdigest()
        print("sha256: " + ans)
        x = takeInput(x)

    elif (x.startswith("/sha512")):
        target = x[8:].encode('utf-8')
        ans = hashlib.sha512(target).hexdigest()
        print("sha512: " +ans)
        x = takeInput(x)

    else:
        print("Command is not found")
        instruction()
        x = takeInput(x)

