from myLibrary import chessBoard

# taking inputs 

size = int(input("Input the required size of the image "))
cell_name = input("Input the name of the cell ")

print("Press 0 to exit")

# defining the path of the image
path = "input_image.png"

# constructing object of the class 

obj = chessBoard(path,size,cell_name)

# calling the dispaly function 
obj.display()

