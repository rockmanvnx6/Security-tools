from PIL import Image

im = Image.open('mona_lisa.jpg')
pix = im.load()
img = Image.new(im.mode,im.size)
student_number = 3619352
b_student_number = "{0:b}".format(student_number)
arr_list = [
    [10,50], [20,100], [30,150], [40,200], [50,250],
    [60,300], [70,350], [80,400], [90,450], [100,500],
    [110,550], [120,600], [130,650], [140,700], [150,750],
    [160,800], [170,850], [180,900], [190,950], [200,1000],
    [210,1050], [220,1100]
]
def bind_binary(value,digit):
    # Modify the most right binary digit of value and then return decimal value.
    binary_value = "{0:b}".format(value)
    binary_value_modify = list(binary_value)
    binary_value_modify[len(binary_value_modify) - 1] = str(digit)
    raw = "".join(binary_value_modify)
    print("-------MODIFYING RED VALUE--------")
    print("Origin: " + binary_value)
    print("Modified: " + raw)
    print("----------------------------------")

    return int(raw,2)

target = pix[10,50]
print("Student binary number: " + b_student_number)
print("-------BEFORE--------")
for i in range(0,len(b_student_number)):
    print(pix[arr_list[i][0],arr_list[i][1]])
print("")
print("")
for i in range(0,len(b_student_number)):
    # pix[i] = (bind_binary(pix[i][0],student_number[i]),target[1],target[2])
    print("before: " + str(pix[arr_list[i][0],arr_list[i][1]]))
    pix[arr_list[i][0],arr_list[i][1]] = (bind_binary(pix[arr_list[i][0],arr_list[i][1]][0],
                                                      b_student_number[i]),pix[arr_list[i][0],arr_list[i][1]][1],
                                          pix[arr_list[i][0],arr_list[i][1]][2])
    print("after: " + str(pix[arr_list[i][0],arr_list[i][1]]))
    print("")
    print("")

im.save('stego_mona_lisa.jpg', format='PNG')
im.close()
test = Image.open("stego_mona_lisa.jpg")
pix_t = test.load()
print("-------AFTER--------")
for i in range(0,len(b_student_number)):
    print(pix_t[arr_list[i][0],arr_list[i][1]])

