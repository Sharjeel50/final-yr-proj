import tkinter as tk
import pygame
from socket import *
import socket
import threading
import sys
import json
import time



pygame.init()

AllPieces = ['WhiteKing','BlackKing','WhiteQeen','BlackQueen','WhiteKnight1','WhiteKnight2','WhiteBishop1',
             'WhiteBishop2','BlackKnight1','BlackKnight2','BlackBishop1','BlackBishop2','WhiteRook1','WhiteRook2',
             'BlackRook1','BlackRook2','WhitePawn1','WhitePawn2','WhitePawn3','WhitePawn4','WhitePawn5','WhitePawn6',
             'WhitePawn7','WhitePawn8','BlackPawn1','BlackPawn2','BlackPawn3','BlackPawn4','BlackPawn5','BlackPawn6',
             'BlackPawn7','BlackPawn8']

WHITE = "White"
BLACK = "Black"
moveover = 0


class Worker(threading.Thread):
    def run(self):
        time.sleep(10)

class ChessBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=70, white="White", lightgrey="lightgrey"):

        self.rows = rows
        self.columns = columns
        self.size = size
        self.white = white
        self.lightgrey = lightgrey
        self.pieces = {}
        #self.client = Client('127.0.0.1')


        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,width=canvas_width, height=canvas_height, background="white")
        self.canvas.grid(row=0, column=0, columnspan=5, padx=3, pady=3, sticky="nsew")

        self.UI_lbl = tk.Label(self, text="Choose Piece: ")
        self.UI_lbl.grid(row=1, column=0, sticky="e")
        self.UI_entry1 = tk.Entry(self)
        self.UI_entry1.grid(row=1, column=1, sticky="w")

        self.UI_lbl = tk.Label(self, text="Choose Row: ")
        self.UI_lbl.grid(row=2, column=0, sticky="e")
        self.UI_entry2 = tk.Entry(self)
        self.UI_entry2.grid(row=2, column=1, sticky="w")

        self.UI_lbl2 = tk.Label(self, text="Choose Column: ")
        self.UI_lbl2.grid(row=3, column=0, sticky="e")
        self.UI_entry3 = tk.Entry(self)
        self.UI_entry3.grid(row=3, column=1, sticky="w")

        self.UI_lbl = tk.Label(self, text="Move Row: ")
        self.UI_lbl.grid(row=4, column=0, sticky="e")
        self.UI_entry4 = tk.Entry(self)
        self.UI_entry4.grid(row=4, column=1, sticky="w")

        self.UI_lbl2 = tk.Label(self, text="Move Column: ")
        self.UI_lbl2.grid(row=5, column=0, sticky="e")
        self.UI_entry5 = tk.Entry(self)
        self.UI_entry5.grid(row=5, column=1, sticky="w")

        self.UI_entry1.bind("<Return>", self.AllPieceMoves)
        self.UI_entry2.bind("<Return>", self.AllPieceMoves)
        self.UI_entry3.bind("<Return>", self.AllPieceMoves)
        self.UI_entry4.bind("<Return>", self.AllPieceMoves)
        self.UI_entry5.bind("<Return>", self.AllPieceMoves)

        #self.game_lbl = tk.Label(self, text="Player moves: ")
        #self.game_lbl.grid(row=1, column=2, rowspan=2, columnspan=3, sticky="w")

        color = self.lightgrey
        for row in range(self.rows):
            color = self.white if color == self.lightgrey else self.lightgrey
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.white if color == self.lightgrey else self.lightgrey

# -------------------------------------------------------------------------------------------------------------- All Pieces added to board

# -------------------------------------------------------------------------------------------------------------- White Side

    def addpiece(self):

        self.canvas.WhiteKing = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhiteKing.png')
        self.canvas.create_image(0,0, image=self.canvas.WhiteKing, tags="WhiteKing", anchor="c")
        self.placepiece("WhiteKing", row = 7, column = 4)

        self.canvas.WhiteQueen = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhiteQueen.png')
        self.canvas.create_image(0,0, image=self.canvas.WhiteQueen, tags="WhiteQueen", anchor="c")
        self.placepiece("WhiteQueen", row = 7, column = 3)

        self.canvas.WhiteBishop1 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhiteBishop.png')
        self.canvas.create_image(0,0, image=self.canvas.WhiteBishop1, tags="WhiteBishop1", anchor="c")
        self.placepiece("WhiteBishop1", row = 7, column = 2)

        self.canvas.WhiteBishop2 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhiteBishop.png')
        self.canvas.create_image(0,0, image = self.canvas.WhiteBishop2,tags = "WhiteBishop2", anchor = 'c')
        self.placepiece("WhiteBishop2" , row = 7, column = 5)

        self.canvas.WhiteKnight1 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhiteKnight.png')
        self.canvas.create_image(0,0, image = self.canvas.WhiteKnight1,tags = "WhiteKnight1", anchor = 'c')
        self.placepiece("WhiteKnight1", row = 7, column = 1) # KNIGHTS TESTED

        self.canvas.WhiteKnight2 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhiteKnight.png')
        self.canvas.create_image(0,0, image = self.canvas.WhiteKnight2,tags = "WhiteKnight2", anchor = 'c')
        self.placepiece("WhiteKnight2", row = 7, column = 6)###

        self.canvas.WhiteRook1 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhiteRook.png')
        self.canvas.create_image(0,0, image = self.canvas.WhiteRook1,tags = "WhiteRook1", anchor = 'c')
        self.placepiece("WhiteRook1", row = 7, column = 0)

        self.canvas.WhiteRook2 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhiteRook.png')
        self.canvas.create_image(1,1, image = self.canvas.WhiteRook2,tags = "WhiteRook2", anchor = 'c')
        self.placepiece("WhiteRook2", row = 7, column = 7)

        self.canvas.WhitePawn1 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhitePawn.png')
        self.canvas.create_image(0,0, image = self.canvas.WhitePawn1, tags="WhitePawn1" ,anchor = 'c')
        self.placepiece("WhitePawn1", row = 6, column = 0)###

        self.canvas.WhitePawn2 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhitePawn.png')
        self.canvas.create_image(0,0, image = self.canvas.WhitePawn2, tags="WhitePawn2" ,anchor = 'c')
        self.placepiece("WhitePawn2", row = 6, column = 1)

        self.canvas.WhitePawn3 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhitePawn.png')
        self.canvas.create_image(0,0, image = self.canvas.WhitePawn3, tags="WhitePawn3" ,anchor = 'c')
        self.placepiece("WhitePawn3", row = 6, column = 2)

        self.canvas.WhitePawn4 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhitePawn.png')
        self.canvas.create_image(0,0, image = self.canvas.WhitePawn4, tags="WhitePawn4" ,anchor = 'c')
        self.placepiece("WhitePawn4", row = 6, column = 3)

        self.canvas.WhitePawn5 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhitePawn.png')
        self.canvas.create_image(0,0, image = self.canvas.WhitePawn5, tags="WhitePawn5" ,anchor = 'c')
        self.placepiece("WhitePawn5", row = 6, column = 4)

        self.canvas.WhitePawn6 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhitePawn.png')
        self.canvas.create_image(0,0, image = self.canvas.WhitePawn6, tags="WhitePawn6" ,anchor = 'c')
        self.placepiece("WhitePawn6", row = 6, column = 5)

        self.canvas.WhitePawn7 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhitePawn.png')
        self.canvas.create_image(0,0, image = self.canvas.WhitePawn7, tags="WhitePawn7" ,anchor = 'c')
        self.placepiece("WhitePawn7", row = 6, column = 6)

        self.canvas.WhitePawn8 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\WhitePawn.png')
        self.canvas.create_image(0,0, image = self.canvas.WhitePawn8, tags="WhitePawn8" ,anchor = 'c')
        self.placepiece("WhitePawn8", row = 6, column = 7)

 #---------------------------------------------------------------------------------------------------------------------- Black Side

        self.canvas.BlackKing = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackKing.png')
        self.canvas.create_image(0,0, image=self.canvas.BlackKing, tags="BlackKing", anchor="c")
        self.placepiece("BlackKing", row = 0, column = 4)

        self.canvas.BlackQueen = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackQueen.png')
        self.canvas.create_image(0,0, image=self.canvas.BlackQueen, tags="BlackQueen", anchor="c")
        self.placepiece("BlackQueen", row = 0, column = 3)

        self.canvas.BlackBishop1 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackBishop.png')
        self.canvas.create_image(0,0, image=self.canvas.BlackBishop1, tags="BlackBishop1", anchor="c")
        self.placepiece("BlackBishop1", row = 0, column = 2)

        self.canvas.BlackBishop2 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackBishop.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackBishop2,tags = "BlackBishop2", anchor = 'c')
        self.placepiece("BlackBishop2" , row = 0, column = 5)

        self.canvas.BlackKnight1 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackKnight.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackKnight1,tags = "BlackKnight1", anchor = 'c')
        self.placepiece("BlackKnight1", row = 0, column = 1)

        self.canvas.BlackKnight2 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackKnight.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackKnight2,tags = "BlackKnight2", anchor = 'c')
        self.placepiece("BlackKnight2", row = 0, column = 6)

        self.canvas.BlackRook1 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackRook.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackRook1,tags = "BlackRook1", anchor = 'c')
        self.placepiece("BlackRook1", row = 0, column = 0)

        self.canvas.BlackRook2 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackRook.png')
        self.canvas.create_image(1,1, image = self.canvas.BlackRook2,tags = "BlackRook2", anchor = 'c')
        self.placepiece("BlackRook2", row = 0, column = 7)

        self.canvas.BlackPawn1 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackPawn.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackPawn1, tags="BlackPawn1" ,anchor = 'c')
        self.placepiece("BlackPawn1", row = 1, column = 0)

        self.canvas.BlackPawn2 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackPawn.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackPawn2, tags="BlackPawn2" ,anchor = 'c')
        self.placepiece("BlackPawn2", row = 1, column = 1)

        self.canvas.BlackPawn3 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackPawn.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackPawn3, tags="BlackPawn3" ,anchor = 'c')
        self.placepiece("BlackPawn3", row = 1, column = 2)

        self.canvas.BlackPawn4 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackPawn.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackPawn4, tags="BlackPawn4" ,anchor = 'c')
        self.placepiece("BlackPawn4", row = 1, column = 3)

        self.canvas.BlackPawn5 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackPawn.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackPawn5, tags="BlackPawn5" ,anchor = 'c')
        self.placepiece("BlackPawn5", row = 1, column = 4)

        self.canvas.BlackPawn6 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackPawn.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackPawn6, tags="BlackPawn6" ,anchor = 'c')
        self.placepiece("BlackPawn6", row = 1, column = 5)

        self.canvas.BlackPawn7 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackPawn.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackPawn7, tags="BlackPawn7" ,anchor = 'c')
        self.placepiece("BlackPawn7", row = 1, column = 6)

        self.canvas.BlackPawn8 = tk.PhotoImage(file = 'E:\\Final Project + Report\\Pieces\\BlackPawn.png')
        self.canvas.create_image(0,0, image = self.canvas.BlackPawn8, tags="BlackPawn8" ,anchor = 'c')
        self.placepiece("BlackPawn8", row = 1, column = 7)


# -------------------------------------------------------------------------------------------------------------------------------

    def placepiece(self, name, row, column):
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

        # -- Make a whole nother function for a button that makes the pieces move


    # def PlayerTurn(self):
    #     a = 1
    #
    #     WhitePlayer = True
    #     BlackPlayer = False
    #
    #     #while not TurnNotFinshed == False
    #
    #     # while True:
    #     #     if WhitePlayer == True:
    #     #         BlackPlayer == False
    #     #         return 1
    #     #     elif BlackPlayer == True:
    #     #         WhitePlayer == False
    #     #         return 2




    def TheRooksOnly(self):

        piecestaken = []

        Rook = ["WhiteRook", "whiterook", "BlackRook", "blackrook"]

        RookTuple = []
        RookTuple2 = []

        ChoosePiece = str(self.UI_entry1.get())

        for Rooks in Rook:
            if ChoosePiece == Rooks:
                global moveover
                moveover = moveover + 1
                RookRow = int(self.UI_entry2.get()) #mighht not be needed
                RookColumn = int(self.UI_entry3.get())
                RookMoves = self.RookMoves(RookRow,RookColumn)
                RookTuple.append(RookRow) # Add to list to tuple
                RookTuple.append(RookColumn) # Add to list to tuple
                RookRowColumn = tuple(RookTuple) # Tuple the numbers
                for piece,position in list(self.pieces.items()): # Get the Key from the values
                    if position == RookRowColumn: # if the tupled numbers equals the key
                        print("Piece:",piece,"|","Old Position:",position)   # Print the key and position
                        MoveRow = int(self.UI_entry4.get()) #then get the row and column they can move to
                        MoveColumn = int(self.UI_entry5.get())
                        RookTuple2.append(MoveRow)
                        RookTuple2.append(MoveColumn)
                        TheComparisonRook = tuple(RookTuple2)
                        stop = 0
                        for TheRookMoves in RookMoves: #loop through all the kings moves
                            for a,b in list(self.pieces.items()):
                                # Position occupied!
                                if ChoosePiece[0] == "W" and TheComparisonRook == b and a[0] == "W" and TheComparisonRook[0] >= 0 and TheComparisonRook[1] <= 7 and TheComparisonRook[1] >= 0 and TheComparisonRook[0] <= 7:
                                    print("Cannot move there", TheComparisonRook,"already occupied.")
                                    stop = 1

                                elif ChoosePiece[0] == "B" and TheComparisonRook == b and a[0] == "B" and TheComparisonRook[0] >= 0 and TheComparisonRook[1] <= 7 and TheComparisonRook[1] >= 0 and TheComparisonRook[0] <= 7:
                                    print("Cannot move there", TheComparisonRook,"already occupied.")
                                    stop = 1
                                # Take Piece!
                                elif ChoosePiece[0] == "W" and TheComparisonRook == b and a[0] == "B" and a[7] != "n" and TheComparisonRook[0] >= 0 and TheComparisonRook[1] <= 7 and \
                                     TheComparisonRook[1] >= 0 and TheComparisonRook [0] <= 7 and TheComparisonRook:# == RookMoves:
                                    self.placepiece(a, row = 14, column = 14)
                                    piecestaken.append(a)
                                    print("Piece taken and removed!:", piecestaken)
                                    print("Possible Moves in current position:",RookMoves)
                                    del self.pieces[a]

                                elif ChoosePiece[0] == "B" and TheComparisonRook == b and a[0] == "W" and a[7] != "n" and TheComparisonRook[0] >= 0 and TheComparisonRook[1] <= 7 and \
                                     TheComparisonRook[1] >= 0 and TheComparisonRook [0] <= 7 and TheComparisonRook:# == RookMoves:
                                    self.placepiece(a, row = 14, column = 14)
                                    piecestaken.append(a)
                                    print("Piece taken and removed!:", piecestaken)
                                    print("Possible Moves in current position:",RookMoves)
                                    del self.pieces[a]
                                    #return True

                                # Move Piece!
                                elif TheComparisonRook == TheRookMoves and TheComparisonRook[0] >= 0 and TheComparisonRook[1] <= 7 and TheComparisonRook[1] >= 0 and TheComparisonRook[0] <= 7:
                                    self.placepiece(piece, row = MoveRow, column = MoveColumn)
                                    print("Piece:",piece,"|","Current Position:",TheComparisonRook)
                                    print("Possible Moves in current position:",RookMoves)
                                    break
                                    del RookTuple[:]
                                    del RookTuple2[:]
                                    return True
                            if stop == 1:
                                break


    def TheKnightsOnly(self):

        piecestaken = []

        KnightTuple = []
        KnightTuple2 = []

        Knight = ["WhiteKnight","BlackKnight","whiteknight","blackknight"]

        ChoosePiece = str(self.UI_entry1.get())

        for Knights in Knight:
            if ChoosePiece == Knights:
                  global moveover
                  moveover = moveover + 1
                  KnightRow = int(self.UI_entry2.get())#mighht not be needed
                  KnightColumn = int(self.UI_entry3.get())
                  AllKnightMoves = self.KnightMoves(KnightRow,KnightColumn)
                  KnightTuple.append(KnightRow) # Add to list to tuple
                  KnightTuple.append(KnightColumn) # Add to list to tuple
                  RowColumn = tuple(KnightTuple) # Tuple the numbers
                  for piece,position in list(self.pieces.items()): # Get the Key from the values
                      if position == RowColumn: # if the tupled numbers equals the key
                        print("Piece:",piece,"|","Old Position:",position)   # Print the key and position
                        MoveRow = int(self.UI_entry4.get())#then get the row and column they can move to
                        MoveColumn = int(self.UI_entry5.get())
                        KnightTuple2.append(MoveRow)
                        KnightTuple2.append(MoveColumn)
                        TheComparison = tuple(KnightTuple2)
                        stop = 0
                        for KnightMoves in AllKnightMoves: #loop through all the kings moves
                            for a,b in list(self.pieces.items()):
                                # Position occupied!
                                if ChoosePiece[0] == "W" and TheComparison == b and a[0] == "W" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                    print("Cannot move there", TheComparison,"already occupied.")
                                    stop = 1

                                elif ChoosePiece[0] == "B" and TheComparison == b and a[0] == "B" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                    print("Cannot move there", TheComparison,"already occupied.")
                                    stop = 1
                                # Take Piece!
                                elif ChoosePiece[0] == "W" and TheComparison == b and a[0] == "B" and a[7] != "n" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and \
                                     TheComparison[1] >= 0 and TheComparison[0] <= 7:# and TheComparison == KnightMoves:
                                    self.placepiece(a, row = 14, column = 14)
                                    piecestaken.append(a)
                                    print("Piece taken and removed!:", piecestaken)
                                    del self.pieces[a]

                                elif ChoosePiece[0] == "B" and TheComparison == b and a[0] == "W" and a[7] != "n" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and \
                                     TheComparison[1] >= 0 and TheComparison[0] <= 7:# and TheComparison == KnightMoves:
                                    self.placepiece(a, row = 14, column = 14)
                                    piecestaken.append(a)
                                    print("Piece taken and removed!:", piecestaken)
                                    del self.pieces[a]

                                # Move Piece!
                                elif TheComparison == KnightMoves and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                    self.placepiece(piece, row = MoveRow, column = MoveColumn)
                                    print("Piece:",piece,"|","Current Position:",TheComparison)
                                    print("Possible Moves in current position:",AllKnightMoves)
                                    return True
                                    #break
                                    del KnightTuple[:]
                                    del KnightTuple2[:]
                            if stop == 1:
                                break
            else:
                print(ChoosePiece, "Not on board!")
                print('')


    def TheBishopsOnly(self):

        piecestaken = []

        BishopTuple = []
        BishopTuple2 = []

        Bishop = ["WhiteBishop","BlackBishop","whitebishop","blackbishop"]

        ChoosePiece = str(self.UI_entry1.get())

        for Bishops in Bishop:
            if ChoosePiece == Bishops:
                  global moveover
                  moveover = moveover + 1
                  BishopRow = int(self.UI_entry2.get()) #mighht not be needed
                  BishopColumn = int(self.UI_entry3.get())
                  BishopMoves = self.BishopMoves(BishopRow,BishopColumn)
                  BishopTuple.append(BishopRow) # Add to list to tuple
                  BishopTuple.append(BishopColumn) # Add to list to tuple
                  BishopRowColumn = tuple(BishopTuple) # Tuple the numbers
                  for piece,position in list(self.pieces.items()): # Get the Key from the values
                      if position == BishopRowColumn: # if the tupled numbers equals the key
                        print("Piece:",piece,"|","Old Position:",position)   # Print the key and position
                        MoveRow = int(self.UI_entry4.get()) #then get the row and column they can move to
                        MoveColumn = int(self.UI_entry5.get())
                        BishopTuple2.append(MoveRow)
                        BishopTuple2.append(MoveColumn)
                        TheComparison = tuple(BishopTuple2)
                        stop = 0
                        for TheBishopMoves in BishopMoves: #loop through all the kings moves
                            for a,b in list(self.pieces.items()):
                                # Position occupied!
                                if ChoosePiece[0] == "W" and TheComparison == b and a[0] == "W" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                    print("Cannot move there", TheComparison,"already occupied.")
                                    stop =1

                                elif ChoosePiece[0] == "B" and TheComparison == b and a[0] == "B" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                    print("Cannot move there", TheComparison,"already occupied.")
                                    stop =1
                                # Take Piece!
                                elif ChoosePiece[0] == "W" and TheComparison == b and a[0] == "B" and a[7] != "n" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and \
                                         TheComparison[1] >= 0 and TheComparison[0] <= 7:# and TheComparison == TheQueenMoves:
                                        self.placepiece(a, row = 15, column = 14)
                                        piecestaken.append(a)
                                        print("Piece taken and removed!:", piecestaken)
                                        #print("Possible Moves in current position:",QueenMoves)
                                        del self.pieces[a]

                                elif ChoosePiece[0] == "B" and TheComparison == b and a[0] == "W" and a[7] != "n" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and \
                                         TheComparison[1] >= 0 and TheComparison[0] <= 7:# and TheComparison == TheQueenMoves:
                                        self.placepiece(a, row = 15, column = 14)
                                        piecestaken.append(a)
                                        print("Piece taken and removed!:", piecestaken)
                                        #print("Possible Moves in current position:",QueenMoves)
                                        del self.pieces[a]

                                # Move Piece!
                                elif TheComparison == TheBishopMoves and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                    self.placepiece(piece, row = MoveRow, column = MoveColumn)
                                    print("Piece:",piece,"|","Current Position:",TheComparison)
                                    print("Possible Moves in current position:",BishopMoves)
                                    return True
                                    break
                                    del BishopTuple[:]
                                    del BishopTuple2[:]
                            if stop == 1:
                                break



    def TheQueensOnly(self):

        piecestaken = []

        QueenTuple = []
        QueenTuple2 = []

        Queen = ["WhiteQueen", "BlackQueen", "whitequeen", "blackqueen"]

        ChoosePiece = str(self.UI_entry1.get())

        for Queens in Queen:
            if ChoosePiece == Queens:
                  global moveover
                  moveover = moveover + 1
                  QueenRow = int(self.UI_entry2.get())
                  QueenColumn = int(self.UI_entry3.get())
                  QueenMoves = self.QueenMoves(QueenRow,QueenColumn)
                  QueenTuple.append(QueenRow) # Add to list to tuple
                  QueenTuple.append(QueenColumn) # Add to list to tuple
                  QueenRowColumn = tuple(QueenTuple) # Tuple the numbers
                  for piece,position in list(self.pieces.items()): # Get the Key from the values
                      if position == QueenRowColumn: # if the tupled numbers equals the key
                        print("Piece:",piece,"|","Old Position:",position)   # Print the key and position
                        MoveRow = int(self.UI_entry4.get()) #then get the row and column they can move to
                        MoveColumn = int(self.UI_entry5.get())
                        QueenTuple2.append(MoveRow)
                        QueenTuple2.append(MoveColumn)
                        TheComparisonQueen = tuple(QueenTuple2)
                        CheckPath = list(self.CheckQueenPathDown(QueenRowColumn,TheComparisonQueen))
                        stop = 0
                        for TheQueenMoves in QueenMoves:
                            for a,b in list(self.pieces.items()):
                                for CheckThePath in CheckPath:
                                    #print(CheckThePath)
                                    # Position occupied!
                                    if ChoosePiece[0] == "W" and TheComparisonQueen == b and a[0] == "W" and TheComparisonQueen[0] >= 0 and TheComparisonQueen[1] <= 7 and \
                                       TheComparisonQueen[1] >= 0 and TheComparisonQueen[0] <= 7:
                                       #print(CheckThePath)
                                       print("Cannot move there", TheComparisonQueen,"already occupied by ", a)
                                       stop = 1

                                    elif ChoosePiece[0] == "B" and TheComparisonQueen == b and a[0] == "B" and TheComparisonQueen[0] >= 0 and TheComparisonQueen[1] <= 7 and \
                                       TheComparisonQueen[1] >= 0 and TheComparisonQueen[0] <= 7:
                                       #print(CheckThePath)
                                        #print("Cannot move there", TheComparisonQueen,"already occupied by ", a)
                                        stop = 1

                                    # Take Piece!
                                    elif ChoosePiece[0] == "B" and TheComparisonQueen == b and a[0] == "W" and a[7] != "n" and TheComparisonQueen[0] >= 0 and TheComparisonQueen[1] <= 7 and \
                                         TheComparisonQueen[1] >= 0 and TheComparisonQueen[0] <= 7:# and TheComparison == QueenMoves:
                                        self.placepiece(a, row = 14, column = 14)
                                        #piecestaken.append(a)
                                        #print("Piece taken and removed!:", piecestaken)
                                        #print("Possible Moves in current position:",QueenMoves)
                                        #del self.pieces[a]
                                        #print(CheckThePath)
                                        #return True
                                        print(CheckThePath)

                                    elif ChoosePiece[0] == "W" and TheComparisonQueen == b and a[0] == "B" and a[7] != "n" and TheComparisonQueen[0] >= 0 and TheComparisonQueen[1] <= 7 and \
                                         TheComparisonQueen[1] >= 0 and TheComparisonQueen[0] <= 7:# and TheComparison == QueenMoves:
                                        self.placepiece(a, row = 14, column = 14)

                                    # Move Piece
                                    elif TheComparisonQueen == TheQueenMoves and TheComparisonQueen[0] >= 0 and TheComparisonQueen[1] <= 7 and \
                                         TheComparisonQueen[1] >= 0 and TheComparisonQueen[0] <= 7 and CheckThePath != b: # condition is still met after being incorrect.
                                        self.placepiece(piece, row = MoveRow, column = MoveColumn)
                                        print(b)
                                        print(CheckThePath)
                                        #return True

                                        #print(CheckThePath[4])
                                        #print("Piece:",piece,"|","Current Position:",TheComparisonQueen)
                                        #print("Possible Moves in current position:",QueenMoves)
                                        #break
                                        #return True

                                        del QueenTuple[:]
                                        del QueenTuple2[:]

                            if stop == 1:
                                break



    def TheKingsOnly(self):

        CheckMate = False

        piecestaken = []

        KingTuple = []
        KingTuple2 = []

        King = ["WhiteKing", "BlackKing", "whiteking", "blackking"]

        #PlayerTurn = self.PlayerTurn()

        ChoosePiece = str(self.UI_entry1.get())

        for Kings in King:
            if ChoosePiece == Kings:
              global moveover
              moveover = moveover + 1
              print(moveover , "TheKingsOnly")
              KingRow = int(self.UI_entry2.get())
              KingColumn = int(self.UI_entry3.get())
              AllKingMoves = self.KingMoves(KingRow,KingColumn)
              KingTuple.append(KingRow) # Add to list to tuple
              KingTuple.append(KingColumn) # Add to list to tuple
              RowColumn = tuple(KingTuple) # Tuple the numbers
              for piece,position in list(self.pieces.items()): # Get the Key from the values
                  if position == RowColumn: # if the tupled numbers equals the key
                    print("Piece:",piece,"|","Old Position:",position)   # Print the key and position
                    MoveRow = int(self.UI_entry4.get())#then get the row and column they can move to
                    MoveColumn = int(self.UI_entry5.get())
                    KingTuple2.append(MoveRow)
                    KingTuple2.append(MoveColumn)
                    TheComparison = tuple(KingTuple2)
                    #QueenMoves = self.QueenMoves(QueenRow,QueenColumn)
                    stop = 0
                    for KingMoves in AllKingMoves: #loop through all the kings moves
                        #for i in CheckPath:
                        for a,b in list(self.pieces.items()):

                            # Position occupied!
                                    # if PlayerTurn == 1 and ChoosePiece[0] == "W":
                            if ChoosePiece[0] == "W" and TheComparison == b and a[0] == "W" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                print("Cannot move there", TheComparison,"already occupied.")
                                stop = 1

                            if ChoosePiece[0] == "B" and TheComparison == b and a[0] == "B" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                print("Cannot move there", TheComparison,"already occupied.")
                                stop = 1

                                        #elif TheQueenMoves == "WhiteKing" and i != b:
                                        #    print("The king is in Check!"")
                                        # Take Piece!
                            elif ChoosePiece[0] == "W" and TheComparison == b and a[0] == "B" and a[8] != "g" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and \
                                 TheComparison[1] >= 0 and TheComparison[0] <= 7:# and TheComparison == KingMoves:
                                self.placepiece(a, row = 11, column = 11)
                                piecestaken.append(a)
                                print("Piece taken and removed!:", piecestaken)
                                del self.pieces[a]

                            elif ChoosePiece[0] == "B" and TheComparison == b and a[0] == "W" and a[8] != "g" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and \
                                 TheComparison[1] >= 0 and TheComparison[0] <= 7:# and TheComparison == KingMoves:
                                self.placepiece(a, row = 11, column = 11)
                                piecestaken.append(a)
                                print("Piece taken and removed!:", piecestaken)
                                del self.pieces[a]

                                        # Move Piece!
                            elif TheComparison == KingMoves and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                self.placepiece(piece, row = MoveRow, column = MoveColumn)
                                print("Piece:",piece,"|","Current Position:",TheComparison)
                                print("Possible Moves in current position:",AllKingMoves)
                                break
                                del KingTuple[:]
                                del KingTuple2[:]

                        if stop == 1:
                            break



    def WhitePawnsOnly(self):

        piecestaken = []

        WhitePawnTuple = []
        WhitePawnTuple2 = []

        ChoosePiece = str(self.UI_entry1.get())

        if ChoosePiece == "WhitePawn":
              global moveover
              moveover = moveover + 1
              WhitePawnRow = int(self.UI_entry2.get()) #mighht not be needed
              WhitePawnColumn = int(self.UI_entry3.get())
              WhitePawnMoves = self.WhitePawnMoves(WhitePawnRow,WhitePawnColumn)
              WhitePawnTuple.append(WhitePawnRow) # Add to list to tuple
              WhitePawnTuple.append(WhitePawnColumn) # Add to list to tuple
              WhitePawnRowColumn = tuple(WhitePawnTuple) # Tuple the numbers
              for piece,position in list(self.pieces.items()): # Get the Key from the values
                  if position == WhitePawnRowColumn: # if the tupled numbers equals the key
                    print("Piece:",piece,"|","Old Position:",position)   # Print the key and position
                    MoveRow = int(self.UI_entry4.get()) #then get the row and column they can move to
                    MoveColumn = int(self.UI_entry5.get())
                    WhitePawnTuple2.append(MoveRow)
                    WhitePawnTuple2.append(MoveColumn)
                    TheComparison = tuple(WhitePawnTuple2)
                    stop = 0
                    for WPawnMoves in WhitePawnMoves: #loop through all the kings moves
                        for a,b in list(self.pieces.items()):
                            # Position occupied!
                            if TheComparison == b and a[0] == "W" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                print("Cannot move there", TheComparison,"already occupied.")
                                stop = 1
                            # Take Piece!
                            elif TheComparison == b and a[0] == "B" and a[8] != "g" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and \
                                 TheComparison[1] >= 0 and TheComparison[0] <= 7:# and TheComparison == WPawnMoves:
                                self.placepiece(a, row = 14, column = 14)
                                piecestaken.append(a)
                                print("Piece taken and removed!:", piecestaken)
                                del self.pieces[a]
                                break
                            # Move Piece!
                            elif TheComparison == WPawnMoves and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                self.placepiece(piece, row = MoveRow, column = MoveColumn)
                                print("Piece:",piece,"|","Current Position:",TheComparison)
                                print("Possible Moves in current position:",WhitePawnMoves)
                                return True
                                break
                                del WhitePawnTuple[:]
                                del WhitePawnTuple2[:]
                        if stop == 1:
                            break


    def BlackPawnsOnly(self):

        piecestaken = []

        BlackPawnTuple = []
        BlackPawnTuple2 = []

        ChoosePiece = str(self.UI_entry1.get())

        if ChoosePiece == "BlackPawn":
              global moveover
              moveover = moveover + 1
              print(moveover , "for ")
              BlackPawnRow = int(self.UI_entry2.get()) #mighht not be needed
              BlackPawnColumn = int(self.UI_entry3.get())
              BlackPawnMoves = self.BlackPawnMoves(BlackPawnRow,BlackPawnColumn)
              BlackPawnTuple.append(BlackPawnRow) # Add to list to tuple
              BlackPawnTuple.append(BlackPawnColumn) # Add to list to tuple
              BlackPawnRowColumn = tuple(BlackPawnTuple) # Tuple the numbers
              for piece,position in list(self.pieces.items()): # Get the Key from the values
                  if position == BlackPawnRowColumn: # if the tupled numbers equals the key
                    print("Piece:",piece,"|","Old Position:",position)   # Print the key and position
                    MoveRow = int(self.UI_entry4.get()) #then get the row and column they can move to
                    MoveColumn = int(self.UI_entry5.get())
                    BlackPawnTuple2.append(MoveRow)
                    BlackPawnTuple2.append(MoveColumn)
                    TheComparison = tuple(BlackPawnTuple2)
                    stop = 0
                    for BPawnMoves in BlackPawnMoves: #loop through all the kings moves
                        for a,b in list(self.pieces.items()):
                            # Position occupied!
                            if TheComparison == b and a[0] == "B" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                print("Cannot move there", TheComparison,"already occupied.")
                                stop = 1
                            # Take Piece!
                            elif TheComparison == b and a[0] == "W" and a[7] != "n" and TheComparison[0] >= 0 and TheComparison[1] <= 7 and \
                                 TheComparison[1] >= 0 and TheComparison[0] <= 7:# and TheComparison == BPawnMoves:
                                self.placepiece(a, row = 14, column = 14)
                                piecestaken.append(a)
                                print("Piece taken and removed!:", piecestaken)
                                del self.pieces[a]
                                break
                            # Move Piece!
                            elif TheComparison == BPawnMoves and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
                                self.placepiece(piece, row = MoveRow, column = MoveColumn)
                                print("Piece:",piece,"|","Current Position:",TheComparison)
                                print("Possible Moves in current position:2",BlackPawnMoves)
                                return True
                                break
                                del BlackPawnTuple[:]
                                del BlackPawnTuple2[:]
                        if stop == 1:
                            break




    ########################################################

    # def recvData(self):
    #     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     while True:
    #          data = sock.recv(1024)
    #          if data:
    #              self.pieces = data
    #              break

    ########################################################



    # -------------------------------------------------------------------------- Call one function that calls the rest.

    def AllPieceMoves(self, Event):



        a = self.BlackPawnsOnly()
        b = self.WhitePawnsOnly()
        c = self.TheKingsOnly()
        d = self.TheQueensOnly()
        e = self.TheBishopsOnly()
        f = self.TheRooksOnly()
        g = self.TheKnightsOnly()

        #h = str(self.UI_entry6.get())


        #if(a==True and b==True and c==True and d==True and e==True and f==True and g==True):
        # if (d == True):
        #     #getClient = Client('127.0.0.1')
        #
        #     print("A moved has been made!")
        #
        #     #getClient.sendDict(board=self.pieces)
        #     self.client.sendDict(board=self.pieces)
        #     self.pieces = self.client.recieve()

        # elif (a == True):
        #     getClient = Client('127.0.0.1')
        #
        #     print("A moved has been made!")
        #
        #     getClient.sendDict(board=self.pieces)
        #     self.pieces = getClient.recieve()
        #
        # elif (b == True):
        #     getClient = Client('127.0.0.1')
        #
        #     print("A moved has been made!")
        #
        #     getClient.sendDict(board=self.pieces)
        #     self.pieces = getClient.recieve()
        #
        # elif (c == True):
        #     getClient = Client('127.0.0.1')
        #
        #     print("A moved has been made!")
        #
        #     getClient.sendDict(board=self.pieces)
        #     self.pieces = getClient.recieve()
        #
        # elif (e == True):
        #     getClient = Client('127.0.0.1')
        #
        #     print("A moved has been made!")
        #
        #     getClient.sendDict(board=self.pieces)
        #     self.pieces = getClient.recieve()
        #
        # elif (f == True):
        #     getClient = Client('127.0.0.1')
        #
        #     print("A moved has been made!")
        #
        #     getClient.sendDict(board=self.pieces)
        #     self.pieces = getClient.recieve()
        #
        # elif (g == True):
        #     #getClient = Client('127.0.0.1')
        #
        #     print("A moved has been made!")
        #
        #     self.client.sendDict(board=self.pieces)
        #     self.pieces = self.client.recieve()
        #
        #





    # -------------------------------------------------------------------------- Bishop Path Check

    def CheckBishopPathUpRight(self, BishopRowColumn, TheComparison):

        row = []
        column = []

        CurrentLocation = QueenRowColumn

        a = BishopRowColumn[0]
        b = BishopRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] + i)
            column.append(CurrentLocation[1] + i)

        UpRight = zip(row,column)

        UpRight = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparison]

        return UpRight

    ##########

    def CheckBishopPathUpLeft(self, BishopRowColumn, TheComparison):

        row = []
        column = []

        CurrentLocation = BishopRowColumn

        a = BishopRowColumn[0]
        b = BishopRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] + i)
            column.append(CurrentLocation[1] - i)

        UpLeft = zip(row,column)

        UpLeft = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparison]

        return UpLeft

    ##########

    def CheckBishopPathDownRight(self, BishopRowColumn, TheComparison):

        row = []
        column = []

        CurrentLocation = BishopRowColumn

        a = BishopRowColumn[0]
        b = BishopRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] - i)
            column.append(CurrentLocation[1] + i)

        DownRight = zip(row,column)

        DownRight = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparison] #Remove the current posotion from the path.

        return DownRight

    ##########

    def CheckBishopPathDownLeft(self, BishopRowColumn, TheComparison):

        row = []
        column = []

        CurrentLocation = BishopRowColumn

        a = BishopRowColumn[0]
        b = BishopRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] - i)
            column.append(CurrentLocation[1] - i)

        DownLeft = zip(row,column)

        DownLeft = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparison]

        return DownLeft

    # -------------------------------------------------------------------------- Rook Path Check

    def CheckRookPathUp(self, RookRowColumn, TheComparisonRook):

        row = []
        column = []

        CurrentLocation = RookRowColumn

        a = RookRowColumn[0]
        b = RookRowColumn[1]

        for i in range (-7,7):

            row.append(CurrentLocation[1] + i)
            column.append(a)

        Up = zip(row,column)

        Up = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonRook]

        return Up

    ##########

    def CheckRookPathDown(self, RookRowColumn, TheComparisonRook):


        row = []
        column = []

        CurrentLocation = RookRowColumn

        a = RookRowColumn[0]
        b = RookRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[1] - i)
            column.append(a)

        Down = zip(row,column)

        Down = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonRook]

        return Down

    ##########

    def CheckQRookPathRight(self, RookRowColumn, TheComparisonRook):

         row = []
         column = []

         CurrentLocation = RookRowColumn

         a = RookRowColumn[0]
         b = RookRowColumn[1]

         for i in range (-7,0):

            row.append(CurrentLocation[0] + i)
            column.append(b)

         Right = zip(row,column)

         Right = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonRook]

         return Right

    ##########

    def CheckRookPathLeft(self, RookRowColumn, TheComparisonRook):

        row = []
        column = []

        CurrentLocation = RookRowColumn

        a = RookRowColumn[0]
        b = RookRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] - i)
            column.append(b)

        Left = zip(row,column)

        Left = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonRook]

        return Left

    # -------------------------------------------------------------------------- Queen Path Check

    def CheckQueenPathDown(self, QueenRowColumn, TheComparisonQueen):


        row = []
        column = []

        CurrentLocation = QueenRowColumn

        a = QueenRowColumn[0]
        b = QueenRowColumn[1]

        for i in range (-10,0):

            row.append(CurrentLocation[1] - i)
            column.append(a)

        Down = zip(row,column)

        Down = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonQueen]

        return Down

    ##########

    def CheckQueenPathUp(self, QueenRowColumn, TheComparisonQueen):

        row = []
        column = []

        CurrentLocation = QueenRowColumn

        a = QueenRowColumn[0]
        b = QueenRowColumn[1]

        for i in range (-10,7):

            row.append(CurrentLocation[1] + i)
            column.append(a)

        Up = zip(row,column)

        Up = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonQueen]

        return Up

    ##########

    def CheckQueenPathRight(self, QueenRowColumn, TheComparisonQueen):

         row = []
         column = []

         CurrentLocation = QueenRowColumn
         #MoveLocation = TheComparisonQueen
         a = QueenRowColumn[0]
         b = QueenRowColumn[1]

         for i in range (-7,0):

            row.append(CurrentLocation[0] + i)
            column.append(b)

         Right = zip(row,column)

         Right = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonQueen]

         return Right

    ##########

    def CheckQueenPathLeft(self, QueenRowColumn, TheComparisonQueen):

        row = []
        column = []

        CurrentLocation = QueenRowColumn
        #MoveLocation = TheComparisonQueen
        a = QueenRowColumn[0]
        b = QueenRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] - i)
            column.append(b)

        Left = zip(row,column)

        Left = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonQueen]

        return Left

    ##########

    def CheckQueenPathUpRight(self, QueenRowColumn, TheComparisonQueen):

        row = []
        column = []

        CurrentLocation = QueenRowColumn
        #MoveLocation = TheComparisonQueen
        a = QueenRowColumn[0]
        b = QueenRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] + i)
            column.append(CurrentLocation[1] + i)

        UpRight = zip(row,column)

        UpRight = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonQueen]

        return UpRight

    ##########

    def CheckQueenPathUpLeft(self, QueenRowColumn, TheComparisonQueen):

        row = []
        column = []

        CurrentLocation = QueenRowColumn
        #MoveLocation = TheComparisonQueen
        a = QueenRowColumn[0]
        b = QueenRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] + i)
            column.append(CurrentLocation[1] - i)

        UpLeft = zip(row,column)

        UpLeft = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonQueen]

        return UpLeft

    ##########

    def CheckQueenPathDownRight(self, QueenRowColumn, TheComparisonQueen):

        row = []
        column = []

        CurrentLocation = QueenRowColumn

        a = QueenRowColumn[0]
        b = QueenRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] - i)
            column.append(CurrentLocation[1] + i)

        DownRight = zip(row,column)

        DownRight = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonQueen]

        return DownRight

    ##########

    def CheckQueenPathDownLeft(self, QueenRowColumn, TheComparisonQueen):

        row = []
        column = []

        CurrentLocation = QueenRowColumn

        a = QueenRowColumn[0]
        b = QueenRowColumn[1]

        for i in range (-7,0):

            row.append(CurrentLocation[0] - i)
            column.append(CurrentLocation[1] - i)

        DownLeft = zip(row,column)

        DownLeft = [(i,j) for i,j in zip(row,column) if (i,j) != TheComparisonQueen]

        return DownLeft

    # -------------------------------------------------------------------------- All Possible Piece Moves

    def BlackPawnMoves(self, BlackPawnRow, BlackPawnColumn):

        FinalMove = []

        FinalMove.append(((BlackPawnRow + 2),(BlackPawnColumn))) # (2 up) -- En Passant Move
        FinalMove.append(((BlackPawnRow + 1),(BlackPawnColumn))) # (1 up) -
        FinalMove.append(((BlackPawnRow + 1),(BlackPawnColumn - 1))) # -- Diagnals, Need to do.
        FinalMove.append(((BlackPawnRow + 1),(BlackPawnColumn - 1))) #

        return FinalMove;



    def WhitePawnMoves(self, WhitePawnRow, WhitePawnColumn):

        FinalMove = []

        FinalMove.append(((WhitePawnRow - 2),(WhitePawnColumn))) # (2 up) -- En Passant Move
        FinalMove.append(((WhitePawnRow - 1),(WhitePawnColumn))) # (1 up) -
        FinalMove.append(((WhitePawnRow - 1),(WhitePawnColumn + 1))) # -- Diagnals, Need to do.
        FinalMove.append(((WhitePawnRow - 1),(WhitePawnColumn + 1))) #

        return FinalMove;



    def QueenMoves(self, QueenRow, QueenColumn):

        FinalMove = []

        for i in range(-7,7):

            FinalMove.append(((QueenRow + i),(QueenColumn)))
            FinalMove.append(((QueenRow - i),(QueenColumn)))
            FinalMove.append(((QueenRow),(QueenColumn + i)))
            FinalMove.append(((QueenRow),(QueenColumn - i)))
            FinalMove.append(((QueenRow + i),(QueenColumn - i)))
            FinalMove.append(((QueenRow - i),(QueenColumn - i)))
            FinalMove.append(((QueenRow + i),(QueenColumn + i)))
            FinalMove.append(((QueenRow - i),(QueenColumn + i)))

        return FinalMove



    def BishopMoves(self, BishopRow, BishopColumn):

        FinalMove = []

        for i in range(-7,7):

            FinalMove.append(((BishopRow + i),(BishopColumn - i)))
            FinalMove.append(((BishopRow - i),(BishopColumn - i)))
            FinalMove.append(((BishopRow + i),(BishopColumn + i)))
            FinalMove.append(((BishopRow - i),(BishopColumn + i)))

        return FinalMove;



    def RookMoves(self, RookRow, RookColumn):

        FinalMove = []

        for i in range(-7,7):

            FinalMove.append(((RookRow + i),(RookColumn)))
            FinalMove.append(((RookRow - i),(RookColumn)))
            FinalMove.append(((RookRow),(RookColumn + i)))
            FinalMove.append(((RookRow),(RookColumn - i)))

        return FinalMove

    def KingMoves(self, KingRow, KingColumn):


        FinalMove = []

        FinalMove.append(((KingRow - 1),(KingColumn))) # (left 1)
        FinalMove.append(((KingRow + 1),(KingColumn))) # (right 1)
        FinalMove.append(((KingRow),(KingColumn - 1)))
        FinalMove.append(((KingRow),(KingColumn + 1))) # (up 1)
        FinalMove.append(((KingRow + 1),(KingColumn + 1))) # (right 1) (up 1) -- Diagonals for king only
        FinalMove.append(((KingRow - 1),(KingColumn + 1))) # (left 1)(up 1)
        FinalMove.append(((KingRow + 1),(KingColumn - 1))) # (right 1)(down 1)
        FinalMove.append(((KingRow - 1),(KingColumn - 1))) # (left 1)(down 1)

        return FinalMove


    def KnightMoves(self, KnightRow, KnightColumn):

        FinalMove = []

        FinalMove.append(((KnightRow + 2),(KnightColumn - 1))) # (Up 2) (1 left)
        FinalMove.append(((KnightRow - 1),(KnightColumn + 2))) # (Down 1)  (2 Right)
        FinalMove.append(((KnightRow - 2),(KnightColumn - 1))) # (Down 2)  (1 Left)
        FinalMove.append(((KnightRow + 2),(KnightColumn + 1))) # (Up 2) (1 Right)
        FinalMove.append(((KnightRow + 1),(KnightColumn + 2))) # (Up 1) (2 Right)
        FinalMove.append(((KnightRow - 1),(KnightColumn - 2))) # (Down 1)  (2 Left)
        FinalMove.append(((KnightRow + 1),(KnightColumn - 2))) # (Up 1) (2 Left)
        FinalMove.append(((KnightRow - 2),(KnightColumn + 1))) # (Down 2)  (1 Right)

        return FinalMove;


# class Client:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     def sendDict(self, board):
#
#         open = True
#         serverName = '127.0.0.1'
#         serverPort = 8000
#         serializedDict = json.dumps(board)
#         #serializedDict = json.dumps(data.pieces)
#         print(serializedDict)
#         print("Data is sent")
#         result = self.sock.send(serializedDict.encode('utf-8'))
#         #print(result)
#         #self.sock.send(serializedDict.encode('utf-8'),(serverName, serverPort))
#         #print(serializedDict)
#         #print(board)
#     #def sendMsg(self):
#     #        self.sock.send(bytes(input(""), 'utf-8'))
#
#     def recieve(self):
#         send_data = None
#         print("Trying to recieve data")
#         while True:
#             print("data")
#             data = self.sock.recv(1024)
#             print(data)
#             data = json.loads(data)
#             print("Printing data")
#             print("Data should be here:", data)
#             send_data = data
#             break
#         return send_data
#
#         # def close(self):
#         #     if open == True:
#         #         open = False
#         #         self.sock.close()
#         #         return True
#         #
#         #     return False
#         #
#         # def open(self):
#         #     if open == False:
#         #         open = True
#         #         self.sock.open()
#         #         return True
#         #     return False
#
#         #     if not data:
#         #         print("Data is recieved")
#         #         send_data = data
#         #         print(send_data)
#         #         break
#         # return send_data
#
#     # you missed the "address" parameter that is used when you call Client(), sys.argv[1] is what you type when connecting (127.0.0.1)
#     def __init__(self, address):
#         self.sock.connect((address, 8000))
        # you had a typo here "aThead"
        #aThread = threading.Thread(target=self.sendDict(board))
        #aThread.daemon = True
        #aThread.start()
        #print(data)

#if (len(sys.argv) > 1):
#    client = Client(sys.argv[1])

if __name__ == "__main__":
    root = tk.Tk()
    root.title("                                                                       Welcome, Chess 2.0") #-- Dont change or remove spaces!
    #button = tk.Button(root)
    board = ChessBoard(root)
    board.grid(row=0, column=0,sticky="nsew")
    board.addpiece()
    root.mainloop()






    # ---------------------------------------------- Tests -----------------------------------------------------------
    ##  def MouseClickOnEachPiece(self, rows, columns, event): # -- Do later
##
##       global AllPieces
##
##       while True:S
##         for ThePieces in AllPieces:
##             if board[rows][columns] == ThePieces:
##                 self.canvas.bind('<Button-1>', MakeMove)
##             elif board[rows][columns] != ThePieces:
##                 break


    # -- If the square you're trying to move into is empty or if the square has a opponents piece in it then it is a valid move. # do opponent piece code later!

##    def MakeMove(self, rows, columns):
##
##        global AllPieces
##
##        mouseposition = pygame.mouse.get_pos()
##
##        validmove = ValidMove()
##
##        print("You have clicked at: ", event.x , event.y)
##
##        while True:
##            for i in AllPieces:
##                if i.collidepoint(mouseposition):
##                    self.canvas.move(i, rows , columns + 1) # For example purposes! -- Fix -- show all possible moves
##                    self.canvas.update()

##    def new(self):
##
##        FinalMove = []
##
##        RookRow = 2
##
##        RookColumn = 2
##
##        for i in range (0,7):
##
##            FinalMove.append(((RookRow + i),(RookColumn))) #right # up -- rows stay the same as we are going up
##            FinalMove.append(((RookRow - i),(RookColumn))) #left
##            FinalMove.append(((RookRow),(RookColumn + i)))
##            FinalMove.append(((RookRow),(RookColumn - i))) # need to do them till
##
##        print(FinalMove)

##    def new(self):
##
##        for key, value in self.pieces.items():
##             print("{}: {}".format(key, value))
##
##        a = input("dsa")
##
##        self.placepiece(a,row = 6, column = 4)
##
##        for key, value in self.pieces.items():
##             print("{}: {}".format(key, value))

##    def new(self):
##
##        w = []
##
##        b = int(input("first:" ))
##        c = int(input("second: "))
##        d = int(input("third: "))
##        e = int(input("4th: "))
##
##        w.append(b)
##        w.append(c)
##        w.append(d)
##        w.append(e)
##
##        r = tuple(w)
##
##        print(r)
##
##        for piece,position in self.pieces.items():
##            if position == r:
##                print(piece)

##    def new(self):
##
##        a = input("a")
##        b = int(input("r"))
##        c = int(input("c"))
##
##        self.placepiece(a, row = b, column = c)

####
##    #def Player1(self, Event):
####
####          KingTuple = []
####          KingTuple2 = []
##        KnightTuple = []
##        KnightTuple2 = []
####
##        ChoosePiece = self.UI_entry1 = tk.Entry(self)
####
####          #if ChoosePiece == "a":
####          KingRow = int(self.UI_entry2.get())
####          KingColumn = int(self.UI_entry3.get())
####          AllKingMoves = self.KingMoves(KingRow,KingColumn)
####          KingTuple.append(KingRow) # Add to list to tuple
####          KingTuple.append(KingColumn) # Add to list to tuple
####          RowColumn = tuple(KingTuple) # Tuple the numbers
####          for piece,position in list(self.pieces.items()): # Get the Key from the values
####              if position == RowColumn: # if the tupled numbers equals the key
####                print("Piece:",piece,"|","Old Position:",position)   # Print the key and position
####                MoveRow = int(self.UI_entry4.get())
####                MoveColumn = int(self.UI_entry5.get())
####                KingTuple2.append(MoveRow)
####                KingTuple2.append(MoveColumn)
####                TheComparison = tuple(KingTuple2)
####                for KingMoves in AllKingMoves:
####                    for a,b in list(self.pieces.items()):
####                        if b == TheComparison:
####                            print("Cannot move there", TheComparison,"already occupied.")
####                            #self.placepiece(a,row = 5, column = 5)
####                            del self.pieces[a]
####                            break
####                        elif TheComparison == KingMoves and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
####                            self.placepiece(piece, row = MoveRow, column = MoveColumn)
####                            print("Piece:",piece,"|","Current Position:",TheComparison)
####                            print("Possible moves in current position:",AllKingMoves)
####                            break
####                            del KingTuple[:]
####                            del KingTuple2[:]
##
##        if ChoosePiece == "W":
##              KnightRow = int(self.UI_entry2.get())#mighht not be needed
##              KnightColumn = int(self.UI_entry3.get())
##              AllKnightMoves = self.KnightMoves(KnightRow,KnightColumn)
##              KnightTuple.append(KnightRow) # Add to list to tuple
##              KnightTuple.append(KnightColumn) # Add to list to tuple
##              RowColumn = tuple(KnightTuple) # Tuple the numbers
##              for piece,position in self.pieces.items(): # Get the Key from the values
##                  if position == RowColumn: # if the tupled numbers equals the key
##                    print("Piece:",piece,"|","Old Position:",position)   # Print the key and position
##                    MoveRow = int(self.UI_entry4.get())#then get the row and column they can move to
##                    MoveColumn = int(self.UI_entry5.get())
##                    KnightTuple2.append(MoveRow)
##                    KnightTuple2.append(MoveColumn)
##                    TheComparison = tuple(KnightTuple)
##                    stop = 0
##                    for KnightMoves in AllKnightMoves: #loop through all the kings moves
##                        for a,b in self.pieces.items():
##                            if b == TheComparison and a[0] == "W":
##                                print("Cannot move there", TheComparison,"already occupied.")
##                                stop = 1
##                            elif b == TheComparison and a[0] == "B" and a[7] != "n":
##                                self.placepiece(a, row = 14, column = 14)
##                                piecestaken.append(a)
##                                print("Piece taken and removed!:", piecestaken)
##                                del self.pieces[a]
##                            elif TheComparison == KnightMoves and TheComparison[0] >= 0 and TheComparison[1] <= 7 and TheComparison[1] >= 0 and TheComparison[0] <= 7:
##                                self.placepiece(piece, row = MoveRow, column = MoveColumn)
##                                print("Piece:",piece,"|","Current Position:",TheComparison)
##                                print("Possible Moves in current position:",KnightMoves)
##                                break
##                                del KnightTuple[:]
##                                del KnightTuple2[:]
##                        if stop == 1:
##                            break
