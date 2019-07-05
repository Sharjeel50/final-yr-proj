coord=[ ['0',' bR ',' bKn ',' bB ',' bQ ',' bK ',' bB ',' bKn ',' bR '],
        ['1',' bP ',' bP  ',' bP ',' bP ',' bP ',' bP ',' bP  ',' bP '],
        ['2',' _  ','  _  ',' _  ',' _  ',' wK ','  _ ','  _  ','  _ '],
        ['3',' _  ','  _  ',' _  ',' _  ',' _  ','  _ ','  _  ','  _ '],
        ['4',' _  ','  _  ',' _  ',' _  ',' _  ','  _ ','  _  ','  _ '],
        ['5',' _  ','  _  ',' _  ',' _  ',' _  ','  _ ','  _  ','  _ '],
        ['6',' wP ','  _  ',' _  ',' _  ',' _  ','  _ ','  _  ','  _ '],
        ['7',' wR ',' wKn ',' wB ',' wQ ',' _  ',' wB ',' wKn ',' wR '],
        [' ',' 1  ','  2  ','  3 ',' 4  ',' 5  ',' 6  ',' 7   ','  8 '] ]


for sublist in coord: print (" | " .join(sublist))

for i in range(1000):

    movepiece = input("enter coordinate to move piece (e.g. [0][1]): ")
    newpos = input("enter coordinate of new position")
        
    string_row = int( movepiece[1] )
    string_column = int ( movepiece[4] )

    piece = coord[string_row][string_column]

    current_pos = [0,0]

    allpieces = [' wK ', ' wP ']

    for ss in allpieces:
        if piece == ss:
            for i in range(len(coord)-1):
                found = False
                if(found):
                    break
                count = 0
            
                for j in coord[i]:
                    if j == ss:
                        found = True
                        current_pos = [i,count]
                        break
                    count = count + 1
                    
                
    print("Current position", current_pos)

    #King moves -------------------------------------

    topright = [current_pos[0] - 1, current_pos[1] + 1]

    topleft = [current_pos[0] - 1, current_pos[1] - 1]

    bottomright = [current_pos[0] + 1, current_pos[1] + 1]

    bottomleft = [current_pos[0] + 1, current_pos[1] - 1]

    left = [current_pos[0], current_pos[1] - 1]

    right = [current_pos[0], current_pos[1] + 1]

    down = [current_pos[0] + 1 , current_pos[1]]

    up = [current_pos[0] - 1, current_pos[1]]
    

    #Pawn moves --------------------------------------

    pawnup = [current_pos[0] - 1, current_pos[1]]

    pawnenpassant = [current_pos[0] - 2, current_pos[1]]

    takeleft = [current_pos[0] - 1, current_pos[1] - 1]

    takeright = [current_pos[0] - 1, current_pos[1] + 1]
    

      
    moves = [topright,topleft,bottomright,bottomleft,left,right,up,down,pawnup]
    
    pieces = ['bP']  
    
    for i in moves:
        if i == [ int(newpos[1]),int(newpos[4]) ] and i != ' _ ':
                coord[int(newpos[1])][int(newpos[4])] = piece
                coord[string_row][string_column] = ' _ '
            
                
    print("The current position ", current_pos)

    print("Piece ",piece,"has been moved!")
                        
    for sublist in coord: print (" | ".join(sublist))
