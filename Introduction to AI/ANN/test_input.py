#Simple method
# '''f = open("C:\\Users\\DELL\\Downloads\\308333058_2348290398679519_648870950978099272_n.png",'rb')

# newfile = open('newfile.jpg','wb')

# for line in f:
#     newfile.write(line)'''

# # #Using tkinter
# '''from tkinter import *
# # from PIL import Image, ImageTk (Use for JPG or JPEG file)

# root = Tk()
# top = Toplevel()
# cL = Canvas(top, width = 900, height = 400)
# cL.pack()

# # im = Image.open("C:\\Users\\DELL\\Downloads\\f6c71b2ad38aa6d5b17f7ab07b4e6576.jpg") (Use for JPG or JPEG file)
# # pic = ImageTk.PhotoImage(im) (Use for JPG or JPEG file)
# pic = PhotoImage(file = "C:\\Users\\DELL\\Downloads\\298569798_444649757708625_3631162112473503760_n.png")
# cL.create_image(0,0, image = pic, anchor = 'nw')
# root.mainloop()'''

# # ----------------------------------------------------

# #Using OpenCV to read image
# '''from IPython.display import Image
# import os
# import cv2 as cv
# dirPath = r"C:\\python code\\newfile.jpg"
# files = os.listdir(dirPath)
# for file in files:
#     filename = os.path.join(dirPath, file)
#     print(filename)
#     image = cv.imread(filename, cv.IMREAD_GRAYSCALE)
#     cv.imshow("image", image)
#     cv.waitKey(0)
# cv.destroyAllWindows()''' 

# # ---------------------------------------------------------

# #Convert image to pixel
# """from PIL import Image
# import numpy as np
# img = Image.open('C:/Users/Lenovo/Desktop/Data/by_class/4a/hsf_0/hsf_0_00000.png')
# a = np.array(img)"""

# # -------------------------------------------------------------

# # Using OpenCV (easier to understand =))) )
# '''import cv2
# path = r"C:\Users\DELL\Downloads\hsf_0_00000.png"
# img = cv2.imread(path)      # read image into a 2D matrix
# print(img)
# cv2.imshow('image', img)    # show image
# cv2.waitKey(0)              # if key = 0, the image won't close until a key is stroke
# cv2.destroyAllWindows() 
# # gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # turn the pixel matrix to 2D matrix
# # # cv2.imwrite('gray_new_file.jpg', gray_image)        # save new image
# # print(gray_image)
# # cv2.imshow('gray_image', gray_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()'''

# ----------------------------------------------------------

