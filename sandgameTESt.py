import dudraw
import random

            
w = 400
h = 400

cells = []

#populate 2d list with a shit ton of 0s 
for r in range (w):
    cells.append([])
    for c in range(h):
        cells[r].append(0)


#make sure mouse click is in bounds of the canvas 
def mouse_in_bounds() -> bool:
    return dudraw.mouse_x() < 97 and dudraw.mouse_x() > 5 and dudraw.mouse_y() < 97 and dudraw.mouse_y() > 5




def sand_Animate() -> None:
    for j in range(len(cells)-1):
        for i in range(len(cells[0])):
            if cells[j][i]==0 and cells[j+1][i]==1:
                cells[j][i],cells[j+1][i]=cells[j+1][i], cells[j][i]
                
                




#def balance (i,j):
#    x = random.randint(1,2)#left/right
    
#    if mouse_in_bounds() == True and cells[i-1][j] != 0 and cells[i][j] == 1 and x == 1 :
#        cells[i-1][j] == 1 
#        sand_Animate()

#    elif cells[i-1][j] != 0 and cells[i][j] == 1 and x == 2 :
#        cells[i-1][j] == 1 
#        sand_Animate()






    #check diagonal left/right -- move left first then check if rigth empty 



    





    
    #check below -- if theres floor? 
#def check_bounds() -> bool:
#    x = random.randint(1,2)
#    for r in range (len(cells)):
#        for c in range(len(cells[r])):
#           if r>0 and c>=1 and c<149 and cells[r][c]==1 and cells[r-1][c]==1:
#                if x==1 and cells[r-1][c-1]!=1 and floorCells[r-1][c-1]!=1: #anself.water_cells[r-1][c-1]!=1:
#                    cells[r-1][c-1]=1
#                    cells[r][c]=0
#                elif x==2 and cells[r-1][c+1]!=1 and floorCells[r-1][c+1]!=1:#and self.water_cells[r-1][c+1]!=1
#                        cells[r-1][c+1]=1
#                        cells[r][c]=0



                #literally i fucking hate it here this sucks :////////////////////////
                #augh fuck 




        #h


def header(key) ->None: 
    if key == 's' :
        dudraw.text("Sand")
    
    if key == 'f':
        dudraw.text("Floor ")
    
    if key == 'w':
        dudraw.text("Water ")
    



dudraw.set_canvas_size(w,h )

dudraw.set_x_scale(0,100)
dudraw.set_y_scale(0,100)
dudraw.clear(dudraw.LIGHT_GRAY)

key = 's'
frameCount=0
while key != 'q':
    frameCount+=1
    dudraw.clear(dudraw.BOOK_LIGHT_BLUE)
    
    
    if dudraw.has_next_key_typed():
        #Runs once per keypress
        key = dudraw.next_key_typed()
        
    if key == 's':
        if dudraw.mouse_is_pressed() and mouse_in_bounds():
            r1 = random.randrange(-5,5) 
            r2 = random.randrange(-5,5)
            cells [int (dudraw.mouse_y()) + r2] [int(dudraw.mouse_x()) + r1]= 1 
        


     
    #ohhhhh i am sad no focus
    if key == 'f':
        if dudraw.mouse_is_pressed() and mouse_in_bounds():
            cells[int (dudraw.mouse_y())][int(dudraw.mouse_x())]  = 2

  

    sand_Animate()
    
    if frameCount%10==0:
        for j in range(len(cells)-1):
            for i in reversed(range(1,len(cells[0])-1)):
                if cells[j+1][i]==1 and cells[j][i+1]==0:
                    cells[j+1][i],cells[j][i+1]=cells[j][i+1],cells[j+1][i]
    if frameCount%10==5:
        for j in range(len(cells)-1):
            for i in range(1,len(cells[0])-1):
                if cells[j+1][i]==1 and cells[j][i-1]==0:
                    cells[j+1][i],cells[j][i-1]=cells[j][i-1],cells[j+1][i]

    for i in range(h):
        for j in range(w):
            if cells [i][j] == 2:
                dudraw.set_pen_color(dudraw.BLACK)
                dudraw.filled_rectangle(j+.5,i+.5,.5,.5)
            if cells[i][j] == 1:
                dudraw.set_pen_color(dudraw.YELLOW)
                dudraw.filled_rectangle(j+0.5,i+0.5,0.5,0.5)


    


    #check_bounds()
    #if cells [j][i] == 2 :# and #sand is touching ig? 
    #    cells[int(dudraw.mouse_y())] [int (dudraw.mouse_x())] = 5
    #if cells [j][i] == 5
        

    
    #    

    #Nooooooooo  i      guess i will just ae ea  e e e ae ae ae ae a e

    
    #if key == 'w ':
    #     if dudraw.mouse_is_pressed() and mouse_in_bounds(): i dont have m i
    #what do i wanna do i wanna EAT JESUS CHRIST MPEOPLe 
    #im so hunru ygy 
             
    #         OH MAC AND CHEESE ###
                

               
   #i litearlly hate it here 

    dudraw.show()