from Coach import Coach
from tictactoe.TicTacToeGame import TicTacToeGame
from tictactoe.keras.NNet import NNetWrapper as nn
from utils import *

args = dotdict({
    'numIters': 5,
    'numEps': 25,
    'tempThreshold': 10,
    'updateThreshold': 0.55,
    'maxlenOfQueue': 200000,
    'numMCTSSims': 25,
    'numItersForTrainExamplesHistory': 20,
    'arenaCompare': 50,
    'cpuct': 1,

    'checkpoint': './temp/tictactoe/',
    'load_model': False,
    'load_folder_file': ('./models/tictactoe/10x25x25','best.pth.tar'),
})

if __name__=="__main__":
    g = TicTacToeGame()
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    c.learn()
