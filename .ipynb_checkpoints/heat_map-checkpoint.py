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
import plotly.figure_factory as ff
import plotly.express as px

def get_heat_map(team, player, game, off_def, play_type='TOTAL', save=False):
    
    # Load the offensive stats if Offense is selected
    if off_def == 'Offense':
        try:
            # Generate the file paths for the selected player
            path = f'data/{game}/{team}/Offense/{player}.json'
            # Retreive the files and assign them a variable
            with open (path, 'r') as o:
                file = json.load(o)

            # Generate Overall PPP
            PPP_raw_data = file['ovr_data']['data']
            PPP_raw_data = pd.DataFrame(PPP_raw_data).transpose()
            PPP_data = PPP(PPP_raw_data)
            
            if play_type == 'TOTAL':
                # Get most frequent play type
                most_freq_df = PPP_data.copy()
                most_freq_df['% of Poss.'] = most_freq_df['% of Poss.'].astype('float')
                most_freq = most_freq_df.sort_values('% of Poss.', ascending=False).drop('TOTAL').reset_index()

                most_freq_play_type = most_freq['index'][0]
                most_freq_play_type_per = most_freq['% of Poss.'][0]
                most_freq_play_type_PPP = most_freq['Total PPP'][0]
                most_freq_play_type_creation_per = most_freq['Total Creation %'][0]
                most_freq_play_type_SQ = most_freq['Total SQ'][0]
                most_freq_play_type_TS = most_freq['Total TS%'][0]

                # Get Most Efficient Play Type
                best = PPP_data.copy()
                best = best[best['Total PPP'] != 'N/A']
                best['Total PPP'] = best['Total PPP'].astype('float')
                best['% of Poss.'] = best['% of Poss.'].astype('float')
                best = best.drop('TOTAL')
                best = best[best['% of Poss.'] > 5.0]

                if best['Total PPP'].sum() != 0:
                    best = best.sort_values('Total PPP', ascending=False).reset_index()
                    best_play_type = best['index'][0]
                    best_play_type_per = best['% of Poss.'][0]
                    best_play_type_PPP = best['Total PPP'][0]
                    best_play_type_SQ = best['Total SQ'][0]
                    best_play_type_creation = best['Total Creation %'][0]
                    best_play_type_TS = best['Total TS%'][0]
                else:
                    best_play_type = 'N/A'
                    best_play_type_per = 'N/A'
                    best_play_type_PPP = 'N/A'
                    best_play_type_SQ = 'N/A'
                    best_play_type_creation = 'N/A'
                    best_play_type_TS = 'N/A'
            else:
                best_play_type = 'N/A'
                best_play_type_per = 'N/A'
                best_play_type_PPP = 'N/A'
                best_play_type_SQ = 'N/A'
                best_play_type_creation = 'N/A'
                best_play_type_TS = 'N/A'
                    
                most_freq_play_type = 'N/A'
                most_freq_play_type_per = 'N/A'
                most_freq_play_type_PPP = 'N/A'
                most_freq_play_type_creation_per = 'N/A'
                most_freq_play_type_SQ = 'N/A'
                most_freq_play_type_TS = 'N/A'

            # Load shot data from selected play_type
            if play_type != 'TOTAL':
                shots = []
                for shot in file['ovr_data']['shooting_locations']:
                    if len(shot) > 2:
                        if shot[2] == play_type:
                            shots.append(shot)
                    else:
                        pass
            else:
                shots = file['ovr_data']['shooting_locations']

            # Generate summary stats
            total_PPP = PPP_data['Total PPP'][play_type]
            total_SQ = PPP_data['Total SQ'][play_type]
            shoot_TS = PPP_data['Shooting TS%'][play_type]
            total_3pt_fg_per = PPP_data['Shooting 3pt FG%'][play_type]
            total_3pt_SQ = PPP_data['Shooting 3pt SQ'][play_type]
            total_creation = PPP_data['Total Creation %'][play_type]

            FTR = PPP_data['Total FTR'][play_type]
            TO_per = PPP_data['Total TO'][play_type]

            try:
                rim_PPP = file['Rim']['data']
                rim_PPP = pd.DataFrame(rim_PPP).transpose()
                rim_PPP = PPP(rim_PPP)

                total_rim_PPP = rim_PPP['Shooting PPP'][play_type]
                rim_TS = rim_PPP['Shooting TS%'][play_type]
                rim_SQ = rim_PPP['Shooting SQ'][play_type]
            except:
                rim_PPP = 'N/A'
                total_rim_PPP = 'N/A'
                rim_TS = 'N/A'
                rim_SQ = 'N/A'
            summary = f'Total PPP:  {total_PPP} \n Shooting TS%:  {shoot_TS} on {total_SQ} SQ \n 3pt FG%:  {total_3pt_fg_per} on {total_3pt_SQ} SQ \n Total Creation %: {total_creation} \n \n Total FTR:  {FTR} \n Total TO%:  {TO_per} \n \n Rim PPP:  {total_rim_PPP} \n Rim TS%:  {rim_TS} on {rim_SQ} SQ \n \n Most Frequent:  {most_freq_play_type} ({most_freq_play_type_per}%)\n PPP:  {most_freq_play_type_PPP} on {most_freq_play_type_SQ} SQ\n Creation %:  {most_freq_play_type_creation_per}\n Total TS%:  {most_freq_play_type_TS} \n \n Best Play Type:  {best_play_type} ({best_play_type_per}%)\n Total PPP:  {best_play_type_PPP} on {best_play_type_SQ} SQ \n Creation %:  {best_play_type_creation} \n Total TS%:  {best_play_type_TS}'
        except:
            print(f'No data for {player}')
            
            
    if off_def == 'Defense':
        try:
            # Generate the file paths for the selected player
            path = f'data/{game}/{team}/Defense/{player}.json'

            # Retreive the files and assign them a variable
            with open (path, 'r') as o:
                file = json.load(o)
           
            # Generate Overall PPP
            PPP_raw_data = file['ovr_data']['data']
            PPP_raw_data = pd.DataFrame(PPP_raw_data).transpose()
            PPP_data = defense_PPP(PPP_raw_data)
            
            # Load shot data from selected zone
            shots = file['ovr_data']['shooting_locations']
            
            # Generate summary stats
            total_PPP = PPP_data['Total PPP']['TOTAL']
            total_SQ = PPP_data['Total SQ']['TOTAL']
            shoot_TS = PPP_data['Shooting TS%']['TOTAL']
            total_3pt_fg_per = PPP_data['Shooting 3pt FG%']['TOTAL']
            total_3pt_SQ = PPP_data['Shooting 3pt SQ']['TOTAL']
            
            FTR = PPP_data['Total FTR']['TOTAL']
            TO_per = PPP_data['Total TO']['TOTAL']

            # Get most frequent play type
            most_freq_df = PPP_data.copy()
            most_freq_df['% of Poss.'] = most_freq_df['% of Poss.'].astype('float')
            most_freq = most_freq_df.sort_values('% of Poss.', ascending=False).drop('TOTAL').reset_index()
    
            most_freq_play_type = most_freq['index'][0]
            most_freq_play_type_per = most_freq['% of Poss.'][0]
            most_freq_play_type_PPP = most_freq['Total PPP'][0]
            most_freq_play_type_SQ = most_freq['Total SQ'][0]
            most_freq_play_type_TS = most_freq['Total TS%'][0]
        
            # Get Most Efficient Play Type
            best = PPP_data.copy()
            best = best[best['Total PPP'] != 'N/A']
            best['% of Poss.'] = best['% of Poss.'].astype('float')
            best = best.drop('TOTAL')
            best = best[best['% of Poss.'] > 5.0]
            
            if best['Total PPP'].sum() != 0:
                best = best.sort_values('Total PPP', ascending=True).reset_index()
                best_play_type = best['index'][0]
                best_play_type_per = best['% of Poss.'][0]
                best_play_type_PPP = best['Total PPP'][0]
                best_play_type_SQ = best['Total SQ'][0]
                best_play_type_creation = best['Total Creation %'][0]
                best_play_type_TS = best['Total TS%'][0]
            else:
                best_play_type = 'N/A'
                best_play_type_per = 'N/A'
                best_play_type_PPP = 'N/A'
                best_play_type_SQ = 'N/A'
                best_play_type_creation = 'N/A'
                best_play_type_TS = 'N/A'
            
            try:
                rim_PPP = file['Rim']['data']
                rim_PPP = pd.DataFrame(rim_PPP).transpose()
                rim_PPP = defense_PPP(rim_PPP)

                total_rim_PPP = rim_PPP['Shooting PPP']['TOTAL']
                rim_TS = rim_PPP['Shooting TS%']['TOTAL']
                rim_SQ = rim_PPP['Shooting SQ']['TOTAL']
            except:
                rim_PPP = 'N/A'
                total_rim_PPP = 'N/A'
                rim_TS = 'N/A'
                rim_SQ = 'N/A'
                
            summary = f'Total PPP:  {total_PPP} \n Shooting TS%:  {shoot_TS} on {total_SQ} SQ \n 3pt FG%:  {total_3pt_fg_per} on {total_3pt_SQ} SQ\n \n Total FTR:  {FTR} \n Total TO%:  {TO_per} \n \n Rim PPP:  {total_rim_PPP} \n Rim TS%:  {rim_TS} on {rim_SQ} SQ \n \n Most Frequent:  {most_freq_play_type} ({most_freq_play_type_per}%)\n PPP:  {most_freq_play_type_PPP} on {most_freq_play_type_SQ} SQ\n Total TS%:  {most_freq_play_type_TS}\n \n Best Play Type:  {best_play_type} ({best_play_type_per}%)\n Total PPP:  {best_play_type_PPP} on {best_play_type_SQ} SQ \n Total TS%:  {best_play_type_TS}'
            
        except:
            print(f'No data for {player}')
    
    
    #### Generating shot chart and summary ####
    #-----------------------------------------#
     # General plot parameters
    mpl.rcParams['font.size'] = 20
    mpl.rcParams['axes.linewidth'] = 2
    
    # Draw basketball court
    nugg_off_fig = plt.figure(figsize=(7, 6.5))
    plt.gca().set_aspect('equal', adjustable='box')
    nugg_off_ax = nugg_off_fig.add_axes([0, 0, 1, 1])
    nugg_off_ax = create_court(nugg_off_ax, 'black')
    nugg_off_ax.set_facecolor('white')
    
    extent = [-250, 250, 0, 470]
    
    x = [shot[0][0] for shot in shots]
    y = [shot[0][1] + 60 for shot in shots]
    res = [shot[1] for shot in shots]
    
    
    
    nugg_off_ax.annotate(summary, xy=(250,250), xytext=(470, 250), fontsize=20, ha='center', va='center')
    
    nugg_off_ax.set_title(f'{player} Shot Chart | {game}', y=1.03, fontsize=25)
    
    if player == 'Team':
        player = team
        
    if game == '!season_totals':
        game = 'Season Total'
        
    plt.hexbin(x, y, gridsize=15, cmap='gist_heat_r', alpha=0.7, mincnt=0, extent=extent)
    plt.show()

    return PPP_data, rim_PPP, nugg_off_fig