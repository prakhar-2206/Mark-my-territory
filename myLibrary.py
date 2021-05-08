#importing all the neccesary libraries

import cv2
import math

#creating a class 
class chessBoard:

    def __init__(self,path,size,cell_name):
        
        #initialising all the required variables       
        self.path = path
        self.size = size
        self.cell_name = cell_name

        #mapping the given cell name with cell matrix

        self.mapping_column_name = { 'a':0, 'b':1 , 'c':2 , 'd':3, 'e':4, 'f':5 , 'g':6, 'h':7 }
        self.mapping_row_number = { '1':7 , '2':6, '3':5 , '4':4, '5':3, '6':2 , '7':1, '8':0 }

        # checking validity of cell_name

        if(cell_name[0] in self.mapping_column_name and cell_name[1] in self.mapping_row_number):    

            self.read_image()
            self.resize_image()
            self.preprocessing()
            self.calc_circle_parameter()
            self.drawing()

        else:
            print("Invalid Cell Name")
            
    # reading the image

    def read_image( self):
        self.chess = cv2.imread( self.path , 0)

    # resizing the image according to the given size
     
    def resize_image(self):
        self.chess = cv2.resize(self.chess , (self.size , self.size))

    # creating a binary threshold of the image

    def preprocessing(self):
        self.ret,self.thresh = cv2.threshold(self.chess.copy(), 127 ,255, cv2.THRESH_BINARY)
    
    # calculating all the parameters required for drawing the circle

    def calc_circle_parameter(self ):

        # checking the height and width of the image 
        height , width = self.thresh.shape

        # finding length of each cell on the chess board
        len_col = width/8
        len_row = height/8

        # calculating the starting and ending column pixel values        
        starting_col_pixel = self.mapping_column_name[self.cell_name[0]]*len_col
        ending_col_pixel = (self.mapping_column_name[self.cell_name[0]]+1)*len_col


        # calculating the starting and ending column pixel values        
        starting_row_pixel = self.mapping_row_number[self.cell_name[1]]*len_row
        ending_row_pixel  =  (self.mapping_row_number[self.cell_name[1]]+1)*len_row

        # calculating the center coordinate
        self.center =(int(starting_col_pixel+ending_col_pixel)//2, int(starting_row_pixel + ending_row_pixel)//2 )
        
        # calculating the radius of the circle
        self.radius = math.ceil((ending_col_pixel -starting_col_pixel)/2)

        # calculating the pixel of center 
        self.center_pixel = self.thresh[ (int(starting_row_pixel) + int(ending_row_pixel))//2][ (int(starting_col_pixel)+ int(ending_col_pixel))//2]


    # drawing the circle on the chess board
    def drawing(self):
                
        # inverting the colour of circle by center pixel value        
        if(self.center_pixel == 0):
            self.chess = cv2.circle(self.chess , self.center , self.radius, 255,-1)
        else:
            self.chess = cv2.circle(self.chess , self.center , self.radius, 0,-1)


    # display the modified image on the screen
    def display(self):
        try:
            cv2.imshow("Chess Board" , self.chess)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass