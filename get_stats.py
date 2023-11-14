import pandas as pd
import numpy as np
import seaborn as sns
np.seterr(invalid='ignore')
from PPP import PPP
from defense_PPP import defense_PPP
from court import create_court
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
import plotly.graph_objects as go

def get_stats(team, player, game):
    
    # Generate the file paths for the selected player
    offense_path = f'data/{game}/{team}/Offense/{player}.json'
    defense_path = f'data/{game}/{team}/Defense/{player}.json'
    
    # Retreive the files and assign them a variable
    with open (offense_path, 'r') as o:
        offense_file = json.load(o)
    
    with open (defense_path, 'r') as d:
        defense_file = json.load(d)
    
    # Generate Overall and Rim PPP
    off_PPP = offense_file['ovr_data']['data']
    off_PPP = pd.DataFrame(off_PPP).transpose()
    off_PPP = PPP(off_PPP)

    off_rim_PPP = offense_file['Rim']['data']
    off_rim_PPP = pd.DataFrame(off_rim_PPP).transpose()
    off_rim_PPP = PPP(off_rim_PPP)
    
    def_PPP = defense_file['ovr_data']['data']
    def_PPP = pd.DataFrame(def_PPP).transpose()
    def_PPP = defense_PPP(def_PPP)

    def_rim_PPP = defense_file['Rim']['data']
    def_rim_PPP = pd.DataFrame(def_rim_PPP).transpose()
    def_rim_PPP = defense_PPP(def_rim_PPP)
    
    
    
    #### Generating shot chart and summary ####
    shots = offense_file['ovr_data']['shooting_locations']

    offense_PPP = off_PPP['Total PPP']['TOTAL']
    off_total_SQ = off_PPP['Total SQ']['TOTAL']
    off_shoot_TS = off_PPP['Shooting TS%']['TOTAL']
    off_3pt_fg_per = off_PPP['Shooting 3pt FG%']['TOTAL']
    off_3pt_SQ = off_PPP['Shooting 3pt SQ']['TOTAL']

    off_FTR = off_PPP['Total FTR']['TOTAL']

    offense_rim_PPP = off_rim_PPP['Shooting PPP']['TOTAL']
    off_rim_TS = off_rim_PPP['Shooting TS%']['TOTAL']
    off_rim_SQ = off_rim_PPP['Shooting SQ']['TOTAL']

    # General plot parameters
    mpl.rcParams['font.size'] = 12
    mpl.rcParams['axes.linewidth'] = 2
    # Draw basketball court
    nugg_off_fig = plt.figure(figsize=(5, 4.7))
    nugg_off_ax = nugg_off_fig.add_axes([0, 0, 1, 1])
    nugg_off_ax = create_court(nugg_off_ax, 'black')

    for shot in shots:
        x = shot[0][0]
        y = shot[0][1] + 60
        res = shot[1]
        if res == 1:
            nugg_off_ax.plot(x,y, marker='o', color='#29c42e', markersize=8)
        if res == 0:
            nugg_off_ax.plot(x,y, marker='x', color='red', markersize=9)
        if res == 11: # Free Throws
            nugg_off_ax.plot(x,y, marker='^', color='#2393de', markersize=9)
            
        if res == 20: # Turnovers
            nugg_off_ax.plot(x,y, marker='D', color='grey', markersize=6)
            
        if res == 30: # And-1
            nugg_off_ax.plot(x,y, marker='^', color='#2393de', markersize=9)
    
    nugg_off_ax.set_title(f'{player} Shot Chart | {game}', y=1.03)
    nugg_off_ax.set_xlabel(f'Total PPP: {offense_PPP} \n Shooting TS%: {off_shoot_TS} on {off_total_SQ} SQ \n 3pt FG %: {off_3pt_fg_per} on {off_3pt_SQ} SQ')
    print(f'{player} Shot Chart | {game}')
    print('-----------------------------------------')
    print(f'Total PPP: {offense_PPP}')
    print(f'Shooting TS%: {off_shoot_TS} on {off_total_SQ} SQ')
    print(f'3pt FG %: {off_3pt_fg_per} on {off_3pt_SQ} SQ\n')

    print(f'Total FTR: {off_FTR}\n')

    print(f'Rim PPP: {offense_rim_PPP}')
    print(f'Rim TS%: {off_rim_TS} on {off_rim_SQ} SQ')

    plt.show()

    return off_PPP, off_rim_PPP, nugg_off_fig