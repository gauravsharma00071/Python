def jpeg_res(IMG_20230214_210822.jpg):

    with open(filename , 'rb') as img_file:
        img_file.seek(163)  #height of image is at 164th position

        a = img_file.read(2)
        height = (a[0] << 8) + a[1]

        # next 2 bytes is width
        a = img_file.read(2)

        width = (a[0] << 8) + a[1]

    print("the resolution of the image is " , width, "x", height)
jpeg_res(("IMG_20230214_210822.jpg"))
