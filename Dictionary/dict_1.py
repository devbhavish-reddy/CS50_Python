"""
Dictionary (dict): 

The fundametnal is keys and value, every dict is 
assigned with a key and a value which is corresponding. 



Dictionary in python refers to a data-structures consisting of a key and
a value. It is essentaily mapping something to someth9ing else.   
"""

players = {"Lebron": "76ers", 
          "Kobe": "Lakers", 
          "Kyrie" : "Mavs",
          "D-Rose": "Bulls"

}

print(players["Kyrie"])
print(players)

# Using a for loop to print the dic

for player in players: 
    print(player, players[player], sep = " ")




    math_dictionary_set = [
    {"name": "Euler", "idendity": "Eulers_Identity", "Subject": "Mathematics"},
    {"name": "Pythagoras", "idendity": "Pythagorean_Theorem", "Subject": "Geometry"},
    {"name": "Newton", "idendity": "Second_Law_of_Motion", "Subject": "Physics"},
    {"name": "Einstein", "idendity": "Mass_Energy_Equivalence", "Subject": "Physics"},
    {"name": "Gauss", "idendity": "Normal_Distribution", "Subject": "Statistics"},
    {"name": "Fibonacci", "idendity": "Golden_Ratio", "Subject": "Mathematics"},
    {"name": "Leibniz", "idendity": "Fundamental_Theorem_of_Calculus", "Subject": "Mathematics"},
    {"name": "Shannon", "idendity": "Information_Entropy", "Subject": "Computer_Science"},
    {"name": "Bayes", "idendity": "Bayes_Theorem", "Subject": "Probability"},
    {"name": "Archimedes", "idendity": "Pi_Constant", "Subject": "Geometry"}
]


for entry in math_dictionary_set: 
    print(entry["name"], entry["idendity"], entry["Subject"])

    








