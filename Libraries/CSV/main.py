import csv

players = []
with open("india.csv", "r") as file: 
   
        read = csv.reader(file)
        for player,position in read:
                players.append({"name": player, "position": position})


print(players)



                
                


    

    
    

 