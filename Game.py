import Field_Functionality as ff

if __name__ == '__main__':

   game_field=ff.initializeGamefield()

   bad_moves=[[1,1,1],[1,1,2]]

   ff.removeBadChoices(game_field,bad_moves)
   print(game_field)
   print(ff.gameOver(game_field))




