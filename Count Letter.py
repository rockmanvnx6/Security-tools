def showArr(dict):
    for key in dict:
        print(key);

a = input("Type in the string: ")
store = {};
for i in a:
    if(i not in store):
        store[i] = 1
    else:
        store[i] += 1
store = sorted(store.items(), key=lambda kv: kv[1])
showArr(store)
