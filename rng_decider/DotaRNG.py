import csv
import numpy as np

if __name__ == "__main__":
    # load csv
    fields = []
    entries = []
    totalentries = 0
    total_players = 0
    with open('DotaRNG.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.__next__()
        total_players = len(fields) - 2
        for row in csvreader:
            entries.append(row)
        totalentries = csvreader.line_num - 1
    
    # process fields
    player_name = []
    hero_num = [0] * totalentries
    hero_name = [''] * totalentries
    player_dist = [[0.0 for x in range(totalentries)] for y in range(total_players)]
    player_dist_tot = [0.0] * total_players
    
    # read player names
    for entry in fields[2:]:
        player_name.append(entry)
    
    # read entries
    for i in range(len(entries)):
        hero_num[i] = float(entries[i][0])
        hero_name[i] = entries[i][1]
        
        # read player-defined distributions
        for j in range(total_players):
            player_dist[j][i] = float(entries[i][j+2])
            player_dist_tot[j] += player_dist[j][i]
    
    # normalize probabilities
    player_prob = [[0.0 for x in range(totalentries)] for y in range(total_players)]
    for i in range(len(entries)):
        for j in range(total_players):
            player_prob[j][i] = player_dist[j][i]/player_dist_tot[j]
    
    # select the hero
    for i in range(total_players):
        hero = np.random.choice(hero_name, p=player_prob[i])
        print('Randomly selected ' + hero + ' for ' + player_name[i] + '')
    

