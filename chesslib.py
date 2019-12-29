#chess assignment

#An empty board position has a value of 0. A
#board position that is occupied will have a value
#given by: Offset+Value

#White: Offset=10
#Black: Offset=20

#Piece: Value
#Pawn:   +0
#Knight: +1
#Bishop: +2
#Rook:   +3
#Queen:  +4
#King:   +5

#_ is a BLACK square, # is a WHITE square

#starting chess board
def genBoard():
        T=[13,11,12,14,15,12,11,13,10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,20,20,20,20,20,20,23,21,22,24,25,22,21,23]
        return T

#to determine if the opponent are black or white pieces
def opponent(player):
        if player==10:
                opponent=20
        elif player==20:
                opponent=10
        return opponent

def printBoard(T):
        i=0
        list=[]
#check if it works
        if len(T)>64:
                return False
#replacing numerical values from original list into a list that contains easier to understand values that represent the pieces
        while i<64:
                if T[i]==0:
                        if i%2==0:
                                list=list+["__"]
                                i=i+1
                        elif i%2==1:
                                list=list+["##"]
                                i=i+1
                elif T[i]==10:
                        list=list+["WP"]
                        i=i+1
                elif T[i]==11:
                        list=list+["WN"]
                        i=i+1
                elif T[i]==12:
                        list=list+["WB"]
                        i=i+1
                elif T[i]==13:
                        list=list+["WR"]
                        i=i+1
                elif T[i]==14:
                        list=list+["WQ"]
                        i=i+1
                elif T[i]==15:
                        list=list+["WK"]
                        i=i+1
                elif T[i]==20:
                        list=list+["BP"]
                        i=i+1
                elif T[i]==21:
                        list=list+["BN"]
                        i=i+1
                elif T[i]==22:
                        list=list+["BB"]
                        i=i+1
                elif T[i]==23:
                        list=list+["BR"]
                        i=i+1
                elif T[i]==24:
                        list=list+["BQ"]
                        i=i+1
                elif T[i]==25:
                        list=list+["BK"]
                        i=i+1
                else:
                        return False
#how board looks
        print(str(list[56])+str(list[57])+str(list[58])+str(list[59])+str(list[60])+str(list[61])+str(list[62])+str(list[63]))
        print(str(list[48])+str(list[49])+str(list[50])+str(list[51])+str(list[52])+str(list[53])+str(list[54])+str(list[55]))
        print(str(list[40])+str(list[41])+str(list[42])+str(list[43])+str(list[44])+str(list[45])+str(list[46])+str(list[47]))
        print(str(list[32])+str(list[33])+str(list[34])+str(list[35])+str(list[36])+str(list[37])+str(list[38])+str(list[39]))
        print(str(list[24])+str(list[25])+str(list[26])+str(list[27])+str(list[28])+str(list[29])+str(list[30])+str(list[31]))
        print(str(list[16])+str(list[17])+str(list[18])+str(list[19])+str(list[20])+str(list[21])+str(list[22])+str(list[23]))
        print(str(list[8])+str(list[9])+str(list[10])+str(list[11])+str(list[12])+str(list[13])+str(list[14])+str(list[15]))
        print(str(list[0])+str(list[1])+str(list[2])+str(list[3])+str(list[4])+str(list[5])+str(list[6])+str(list[7]))
        return True

#function which gets all the positions of the pieces that are still in the game and returns it in a list
def GetPlayerPositions(board,player):
        pos=[]
        if player==10:
                for i in range (0,64,1):
                        if (board[i]<20) and (board[i]>=10):
                                pos=pos+[i]
        elif player==20:
                for i in range (0,64,1):
                        if (board[i]>=20):
                                pos=pos+[i]
        return pos

#function that determines how the pawn can move on the board
def pawn_legal_moves(board,position):
        moves=[]
        #white pawn
        if board[position]==10:
                if (board[position+8]==0) and ((position+8)<64):
                        moves=moves+[position+8]
                #diagonal possible moves
                if (board[position+7]>=20 and board[position+7]<=25):
                        if (position+7)%8!=7:
                                moves=moves+[position+7]
                if (board[position+9]>=20 and board[position+9]<=25):
                        if (position+9)%8!=0:
                                moves=moves+[position+9]
        #black pawn
        elif board[position]==20:
                if (board[position-8]==0) and ((position-8)<=64):
                        moves=moves+[position-8]
                #pawn is not at beginning position
                if (board[position-9]<16 and board[position-9]>=10):
                        if (position-9)%8!=1:
                                moves=moves+[position-9]
                if (board[position-7]<16 and board[position-7]>=10):
                        if (position-7)%8!=0:
                                moves=moves+[position-7]
        else:
                return False
        return moves

#function that determines how the rook can move on the board
def rook_legal_moves(board,position,player):
        moves=[]
        #counter for leftward and rightward moving of piece
        cnt_l=1
        cnt_r=1
        #counter for upwards and downwards moving of piece
        cnt_u=8
        cnt_d=8
        opp=opponent(player)
        if (board[position]==(player+3)) or (board[position]==(player+4)):
                #vertical boundary
                #downwards bound
                while (position-cnt_d)>=0:
                        #open spot
                        if (board[position-cnt_d]==0):
                                moves=moves+[position-cnt_d]
                                cnt_d=cnt_d+8
                        #taken spot by opponent
                        elif ((board[position-cnt_d]!=0) and ((board[position-cnt_d]>=opp) and (board[position-cnt_d]<opp+6))):
                                moves=moves+[position-cnt_d]
                                break
                        #taken spot by player
                        elif ((board[position-cnt_d]!=0) and ((board[position-cnt_d]>=player) and (board[position-cnt_d]<player+6))):
                                break
                        else:
                                break
                #upwards bound
                while (position+cnt_u)<64:
                        #open spot
                        if (board[position+cnt_u]==0):
                                moves=moves+[position+cnt_u]
                                cnt_u=cnt_u+8
                        #taken spot by opponent
                        elif ((board[position+cnt_u]!=0) and ((board[position+cnt_u]>=opp) and (board[position+cnt_u]<opp+6))):
                                moves=moves+[position+cnt_u]
                                break
                        #taken spot by player
                        elif ((board[position+cnt_u]!=0) and ((board[position+cnt_u]>=player) and (board[position+cnt_u]<player+6))):
                                break
                        else:
                                break
                #horizontal boundary
                #left boundary
                while (((position-cnt_l)%8)!=7) and (cnt_l<9):
                        #open spot
                        if (board[position-cnt_l]==0):
                                moves=moves+[position-cnt_l]
                                cnt_l=cnt_l+1
                        #taken spot by opponent
                        elif ((board[position-cnt_l]!=0) and ((board[position-cnt_l]>=opp) and (board[position-cnt_l]<opp+6))):
                                moves=moves+[position-cnt_l]
                                break
                        #taken spot by player
                        elif ((board[position-cnt_l]!=0) and ((board[position-cnt_l]>=player) and (board[position-cnt_l]<player+6))):
                                break
                        else:
                                break
                #right boundary
                while ((position+cnt_r)%8!=0) and (cnt_r<9):
                        #open spot
                        if (board[position+cnt_r]==0):
                                moves=moves+[position+cnt_r]
                                cnt_r=cnt_r+1
                        #taken spot by opponent
                        elif ((board[position+cnt_r]!=0) and ((board[position+cnt_r]>=opp) and (board[position+cnt_r]<opp+6))):
                                moves=moves+[position+cnt_r]
                                break
                        #taken spot by player
                        elif ((board[position+cnt_r]!=0) and ((board[position+cnt_r]>=player) and (board[position+cnt_r]<player+6))):
                                break
                        else:
                                break
        else:
                return False
        return moves

#function that determines how the bishop can move on the board
def bishop_legal_moves(board,position,player):
        moves=[]
        #counter for diagonal moving of piece
        cnt_lr=7
        cnt_ll=9
        cnt_ur=9
        cnt_ul=7
        opp=opponent(player)
        if (board[position]==player+2) or (board[position]==player+4):
                #lower right diagonal
                while ((position-cnt_lr)>=0) and (((position-cnt_lr)%8)!=0):
                        #open spot
                        if (board[position-cnt_lr]==0):
                                moves=moves+[position-cnt_lr]
                                cnt_lr=cnt_lr+7
                        #taken spot by opponent
                        elif ((board[position-cnt_lr]!=0) and ((board[position-cnt_lr]>=opp) and (board[position-cnt_lr]<opp+6))):
                                moves=moves+[position-cnt_lr]
                                break
                        #taken spot by player
                        elif ((board[position-cnt_lr]!=0) and ((board[position-cnt_lr]>=player) and (board[position-cnt_lr]<player+6))):
                                break
                        else:
                                break
                #lower left diagonal
                while ((position-cnt_ll)>=0) and (((position-cnt_ll)%8)!=7):
                        #open spot
                        if (board[position-cnt_ll]==0):
                                moves=moves+[position-cnt_ll]
                                cnt_ll=cnt_ll+9
                        #taken spot by opponent
                        elif ((board[position-cnt_ll]!=0) and ((board[position-cnt_ll]>=opp) and (board[position-cnt_ll]<opp+6))):
                                moves=moves+[position-cnt_ll]
                                break
                        #taken spot by player
                        elif ((board[position-cnt_ll]!=0) and ((board[position-cnt_ll]>=player) and (board[position-cnt_ll]<player+6))):
                                break
                        else:
                                break
                #upper right diagonal (+9)
                while ((position+cnt_ur)<64) and (((position+cnt_ur)%8)!=0):
                        #open spot
                        if (board[position+cnt_ur]==0):
                                moves=moves+[position+cnt_ur]
                                cnt_ur=cnt_ur+9
                        #taken spot by opponent
                        elif ((board[position+cnt_ur]!=0) and ((board[position+cnt_ur]>=opp) and (board[position+cnt_ur]<opp+6))):
                                moves=moves+[position+cnt_ur]
                                break
                        #taken spot by player
                        elif ((board[position+cnt_ur]!=0) and ((board[position+cnt_ur]>=player) and (board[position+cnt_ur]<player+6))):
                                break
                        else:
                                break
                #upper left diagonal (+7)
                while ((position+cnt_ul)<64) and (((position+cnt_ul)%8)!=7):
                        #open spot
                        if (board[position+cnt_ul]==0):
                                moves=moves+[position+cnt_ul]
                                cnt_ul=cnt_ul+7
                        #taken spot by opponent
                        elif ((board[position+cnt_ul]!=0) and ((board[position+cnt_ul]>=opp) and (board[position+cnt_ul]<opp+6))):
                                moves=moves+[position+cnt_ul]
                                break
                        #taken spot by player
                        elif ((board[position+cnt_ul]!=0) and ((board[position+cnt_ul]>=player) and (board[position+cnt_ul]<player+6))):
                                break
                        else:
                                break
        else:
                return False
        return moves

#function that determines how the king can move on the board
def king_legal_moves(board,position,player):
        moves=[]
        opp=opponent(player)
        if (board[position]==player+5):
                #forward
                if (position+8)<64:
                        if (board[position+8]!=0) and ((board[position+8]>=opp) and (board[position+8]<opp+6)):
                                moves=moves+[position+8]
                        elif (board[position+8]==0):
                                moves=moves+[position+8]
                #backwards      
                if (position-8)>=0:
                        if (board[position-8]!=0) and ((board[position-8]>=opp) and (board[position-8]<opp+6)):
                                moves=moves+[position-8]
                        elif (board[position-8]==0):
                                moves=moves+[position-8]
                #right
                if position%8!=7:
                        if (board[position+1]!=0) and ((board[position+1]>=opp) and (board[position+1]<opp+6)):
                                moves=moves+[position+1]
                        elif (board[position+1]==0):
                                moves=moves+[position+1]

                #left
                if position%8!=0:
                        if (board[position-1]!=0) and ((board[position-1]>=opp) and (board[position-1]<opp+6)):
                                moves=moves+[position-1]
                        elif (board[position-1]==0):
                                moves=moves+[position-1]
                #upper right diagnoal
                if (position+9)<64 and position%8!=7:
                        if (board[position+9]!=0) and ((board[position+9]>=opp) and (board[position+9]<opp+6)):
                                moves=moves+[position+9]
                        elif (board[position+9]==0):
                                moves=moves+[position+9]
                #upper left diagoonal
                if (position+7)<64 and position%8!=0:
                        if (board[position+7]!=0) and ((board[position+7]>=opp) and (board[position+7]<opp+6)):
                                moves=moves+[position+7]
                        elif (board[position+7]==0):
                                moves=moves+[position+7]
                #lower right diagonal
                if (position-7)>=0 and position%8!=7:
                        if (board[position-7]!=0) and ((board[position-7]>=opp) and (board[position-7]<opp+6)):
                                moves=moves+[position-7]
                        elif (board[position-7]==0):
                                moves=moves+[position-7]
                 #lower left diagonal
                if (position-9)>=64 and position%8!=0:
                        if (board[position-9]!=0) and ((board[position-9]>=opp) and (board[position-9]<opp+6)):
                                moves=moves+[position-9]
                        elif (board[position-9]==0):
                                moves=moves+[position-9]
        else:
                return False
        return moves

#function that determines how the knight can move on the board
def knight_legal_moves(board,position,player):
        moves=[]
        opp=opponent(player)
        if (board[position]==player+1):
                #position+6
                if ((position+6)<64):
                        if (((position+6)%8!=7) and ((position+6)%8!=6)):
                                #taken by opponent
                                if (board[position+6]!=0) and ((board[position+6]>=opp) and (board[position+6]<opp+6)):
                                        moves=moves+[position+6]
                                elif ((board[position+6])==0):
                                        moves=moves+[position+6]
                #position+10
                if ((position+10)<64):
                        if (((position+10)%8!=0) and ((position+10)%8!=1)):
                                #taken by opponent
                                if (board[position+10]!=0) and ((board[position+10]>=opp) and (board[position+10]<opp+6)):
                                        moves=moves+[position+10]
                                elif ((board[position+10])==0):
                                        moves=moves+[position+10]
                #position+15
                if ((position+15)<64):
                        if ((position+15)%8!=7):
                                #taken by opponent
                                if (board[position+15]!=0) and ((board[position+15]>=opp) and (board[position+15]<opp+6)):
                                        moves=moves+[position+15]
                                elif ((board[position+15])==0):
                                        moves=moves+[position+15]
                #position+17
                if ((position+17)<64):
                        if ((position+17)%8!=0):
                                #taken by opponent
                                if (board[position+17]!=0) and ((board[position+17]>=opp) and (board[position+17]<opp+6)):
                                        moves=moves+[position+17]
                                elif ((board[position+17])==0):
                                        moves=moves+[position+17]
                #position-10
                if ((position-10)>=0):
                        if (((position-10)%8!=7) and ((position-10)%8!=6)):
                                #taken by opponent
                                if (board[position-10]!=0) and ((board[position-10]>=opp) and (board[position-10]<opp+6)):
                                        moves=moves+[position-10]
                                elif ((board[position-10])==0):
                                        moves=moves+[position-10]
                 #position-6
                if ((position-6)>=0):
                        if (((position-6)%8!=0) and ((position-6)%8!=1)):
                                #taken by opponent
                                if (board[position-6]!=0) and ((board[position-6]>=opp) and (board[position-6]<opp+6)):
                                        moves=moves+[position-6]
                                elif ((board[position-6])==0):
                                        moves=moves+[position-6]
                #position-17
                if ((position-17)>=0):
                        if (((position-17)%8)!=7):
                                #taken by opponent
                                if ((board[position-17])!=0) and (((board[position-17])>=opp) and ((board[position-17])<opp+6)):
                                        moves=moves+[position-17]
                                elif ((board[position-17])==0):
                                        moves=moves+[position-17]
                #position-15
                if ((position-15)>=0):
                        if ((position-15)%8!=0):
                                #taken by opponent
                                if ((board[position-15]!=0) and ((board[position-15]>=opp) and (board[position-15]<opp+6))):
                                        moves=moves+[position-15]
                                elif ((board[position-15])==0):
                                        moves=moves+[position-15]
        else:
                return False
        return moves

#function that determines how the piece at a certain position on the board can move
def GetPieceLegalMoves(board,position):
        moves=[]
        #pawn
        if board[position]==10 or board[position]==20:
                moves=pawn_legal_moves(board,position)
        #knight, needs player
        elif board[position]==11:
                moves=knight_legal_moves(board,position,10)
        elif board[position]==21:
                moves=knight_legal_moves(board,position,20)
        #bishop, needs player
        elif (board[position]==12):
                moves=bishop_legal_moves(board,position,10)
        elif (board[position]==22):
                moves=bishop_legal_moves(board,position,20)
        #rook, needs player
        elif board[position]==13:
                moves=rook_legal_moves(board,position,10)
        elif board[position]==23:
                moves=rook_legal_moves(board,position,20)
        #queen legal moves: a combination of rook and bishop moves
        elif board[position]==14:
                moves=(rook_legal_moves(board,position,10))+(bishop_legal_moves(board,position,10))
        elif board[position]==24:
                moves=rook_legal_moves(board,position,20)+bishop_legal_moves(board,position,20)
        #king,needs player
        elif board[position]==15:
                moves=king_legal_moves(board,position,10)
        elif board[position]==25:
                moves=king_legal_moves(board,position,20)
        return moves

#function that determines if a piece at a certain position on the board is under threat (can be killed)
def IsPositionUnderThreat(board, position, player):
        opp=opponent(player)
        #list that contains positions that are under threat
        threat=[]
        #loop through each legal moves of opponent
        for i in range (0,64,1):
                if ((board[i]>=opp) and (board[i]<opp+6)):
                        threat=GetPieceLegalMoves(board,i)
                        #determining if the plays of the opponent would be a threat
                        for plays in threat:
                                if plays==position:
                                        return True
        return False


#board=[13,11,12,14,15,12,11,13,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,20,20,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,20,20,20,0,23,21,22,24,25,22,21,23]
board=[13,11,12,14,0,12,11,13,10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0,0,23,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,20,20,20,20,20,20,20,23,21,22,24,25,22,21,23]
printBoard(board)
print(GetPieceLegalMoves(board,26))
print(IsPositionUnderThreat(board,26,10))




