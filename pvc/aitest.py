import ai,chess,pieces
def get_user_move():
    print "Format: xfrom,yfrom xto,yto"
    return ai.Move(3, 1, 3, 2, False)
def get_valid_user_move(board):
    move = get_user_move()
    return move
board = chess.Board.new()
move = ai.Move(3, 1, 3, 2, False)
print "User move: " + move.to_string()
ai_move = ai.AI.get_ai_move(board, [])
board.perform_move(ai_move)
print "AI move: " + ai_move.to_string()


###
def get_user_move():
    print "Format: xfrom,yfrom xto,yto"
    return ai.Move(x_start,y_start,x_end,y_end, False)

def get_valid_user_move(board):
    move = get_user_move()
    return move
while True:
    if (x_start!=0 and y_start!=0 and x_end!=0 and y_end!=0):
        print 'test'
        move = get_valid_user_move(board)
        print "User move: " + move.to_string()
        ai_move = ai.AI.get_ai_move(board, [])
        board.perform_move(ai_move)
        print "AI move: " + ai_move.to_string()
        print "message is:"+message
        break
