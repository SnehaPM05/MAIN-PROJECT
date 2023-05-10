from stegano import lsb



qp = lsb.hide(r"C:\Users\USER\PycharmProjects\steganograpy web\src\static\work\20230421112822.jpg","hello")
qp.save("sample1.png")
clear_message = lsb.reveal("sample1.png")
print(clear_message)