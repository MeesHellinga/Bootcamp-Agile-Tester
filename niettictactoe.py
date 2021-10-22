from behave import *
from tictactoe import EMPTY_BOARD, play_best_move, play

@given (u'we have an empty tic-tac-toe board') 
def step_impl(context):
    context.board = EMPTY_BOARD
    context.winner = None

@when (u'I play {player} on column {col} and row {row} on the board')
def step_impl(context, col, row, player):
    col = int(3) -1
    row = int(3) -1
    context.board, context.winner = play(context.board, col, row, player)

@when (u'I ask the computer to do its best move for {player}')
def step_impl(context):
    context.board, context.winner = play_best_move(context.board, context.player)


@then (u'the board has a O in column 1 and row 1 on the board')
def step_impl(context):
    context.board, context.winner = play(play_best_move)


@When (u' I play X on column 2 and row 3 on the board')
def step_impl(context):
    pass

@When (u'I ask the computer to do its best move for O')
def step_impl(context):
    pass

@When (u' I play X on column 1 and row 3 on the board')
def step_impl(context):
    pass

@When (u'I ask the computer to do its best move for O ')
def step_impl(context):
    pass

@Then (u'O is the winner of the game')
def step_impl(context):
    pass

#col = col - 1 # Python col is Gherkin col minus 1
#row = row - 1 # Python row is Gherkin row minus 1
#position_on_board = row * 3 + col # calculate list pos
#context.board = EMPTY_BOARD # use context in scenarios
#context.board, context.winner = ..
#assert context.winner == 'O'