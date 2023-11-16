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

def get_stats(team, player, game, save=False):
    
    # Generate the file paths for the selected player
    offense_path = f'data/{game}/{team}/Offense/{player}.json'
    #defense_path = f'data/{game}/{team}/Defense/{player}.json'
    
    # Retreive the files and assign them a variable
    with open (offense_path, 'r') as o:
        offense_file = json.load(o)
    '''
    with open (defense_path, 'r') as d:
        defense_file = json.load(d)
        '''
    
    # Generate Overall and Rim PPP
    off_PPP = offense_file['ovr_data']['data']
    off_PPP = pd.DataFrame(off_PPP).transpose()
    off_PPP = PPP(off_PPP)
    try:
        off_rim_PPP = offense_file['Rim']['data']
        off_rim_PPP = pd.DataFrame(off_rim_PPP).transpose()
        off_rim_PPP = PPP(off_rim_PPP)
    except:
        offense_rim_PPP = 'N/A'
        off_rim_TS = 'N/A'
        off_rim_SQ = 'N/A'
    
    '''
    def_PPP = defense_file['ovr_data']['data']
    def_PPP = pd.DataFrame(def_PPP).transpose()
    def_PPP = defense_PPP(def_PPP)
    
    try:
        def_rim_PPP = defense_file['Rim']['data']
        def_rim_PPP = pd.DataFrame(def_rim_PPP).transpose()
        def_rim_PPP = defense_PPP(def_rim_PPP)
    except:
        pass
    '''
    
    
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
    mpl.rcParams['font.size'] = 20
    mpl.rcParams['axes.linewidth'] = 2
    # Draw basketball court
    nugg_off_fig = plt.figure(figsize=(7, 6.5))
    nugg_off_ax = nugg_off_fig.add_axes([0, 0, 1, 1])
    nugg_off_ax = create_court(nugg_off_ax, '#c4c4c4')
    nugg_off_ax.set_facecolor('#4a4a4a')

    for shot in shots:
        x = shot[0][0]
        y = shot[0][1] + 60
        res = shot[1]
        if res == 1:
            nugg_off_ax.plot(x,y, marker='o', color='#4aff50', markersize=12, alpha=0.7)
        if res == 0:
            nugg_off_ax.plot(x,y, marker='o', color='#f54767', markersize=14, alpha=0.7)
        if res == 11: # Free Throws
            nugg_off_ax.plot(x,y, marker='^', color='#40ccff', markersize=12, alpha=0.7)
            
        if res == 20: # Turnovers
            nugg_off_ax.plot(x,y, marker='D', color='#ffed2b', markersize=9, alpha=0.5)
            
        if res == 30: # And-1
            nugg_off_ax.plot(x,y, marker='^', color='#2393de', markersize=11, alpha=0.7)
    
    if player == 'Team':
        player = team
        
    nugg_off_ax.annotate(f'Total PPP:  {offense_PPP} \n Shooting TS%:  {off_shoot_TS} on {off_total_SQ} SQ \n 3pt FG %:  {off_3pt_fg_per} on {off_3pt_SQ} SQ \n \n Total FTR:  {off_FTR} \n \n Rim PPP:  {offense_rim_PPP} \n Rim TS%:  {off_rim_TS} on {off_rim_SQ} SQ', xy=(250, 250), xytext=(250, 250), fontsize=20)
    
    nugg_off_ax.set_title(f'{player} Shot Chart | {game}', y=1.03, fontsize=25)
    #nugg_off_ax.set_xlabel(f'Total PPP:  {offense_PPP} \n Shooting TS%:  {off_shoot_TS} on {off_total_SQ} SQ \n 3pt FG %:  {off_3pt_fg_per} on {off_3pt_SQ} SQ \n \n Total FTR:  {off_FTR} \n \n Rim PPP:  {offense_rim_PPP} \n Rim TS%:  {off_rim_TS} on {off_rim_SQ} SQ', fontsize=20)

    plt.show()
    #plt.subplots_adjust(top=0.88)
    
    # Save figure if save is True
    if save:
        nugg_off_fig.savefig(f'data/{game}/{team}/Offense/{player}.png', bbox_inches='tight', dpi=nugg_off_fig.dpi)

    return off_PPP, off_rim_PPP, nugg_off_fig