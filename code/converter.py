import morse as m
str =input("Enter the string to be converted:")
print("String entered:",str)
print("Morse code:", end = " ")
for i in str:
    for j in m.morse:
        if i==j:
            print(m.morse[i],end = " ")