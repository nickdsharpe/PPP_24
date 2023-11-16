import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def create_court(ax, color):
    
    ''' BASIC NBA COURT '''
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=3, color=color)
    ax.plot([220, 220], [0, 140], linewidth=3, color=color)
    
    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 439, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=3))
    
    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=3, color=color)
    ax.plot([80, 80], [0, 190], linewidth=3, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=3, color=color)
    ax.plot([60, 60], [0, 190], linewidth=3, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=3, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=3))
    
    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=3))

    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)
    
    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)
    
    ''' ZONES '''
    # RIM
    ax.add_artist(mpl.patches.Arc((0, 60), 159, 140, theta1=0, theta2=180, facecolor='none', edgecolor='#5c5c5c', lw=2, linestyle='dashed'))
    ax.plot([-80, -80], [0, 60], lw=1, linestyle='dashed', color='#5c5c5c')
    ax.plot([80, 80], [0, 60], lw=1, linestyle='dashed', color='#5c5c5c')
    
    # SHORT MID-RANGE
    ax.add_artist(mpl.patches.Arc((0, 80), 290, 270, theta1=0, theta2=180, facecolor='none', edgecolor='#5c5c5c', lw=2, linestyle='dashed'))
    ax.plot([-145.2, -145.2], [0, 80], lw=2, linestyle='dashed', color='#5c5c5c')
    ax.plot([144.5, 144.5], [0, 80], lw=2, linestyle='dashed', color='#5c5c5c')
    
    ax.plot([45, 90], [118, 187], lw=2, linestyle='dashed', color='#5c5c5c')
    ax.plot([-45, -90], [118, 187], lw=2, linestyle='dashed', color='#5c5c5c')
    
    '''
    # 3PT ARC 
    ax.add_artist(mpl.patches.Arc((0, 140), 439, 315, theta1=0, theta2=180, facecolor='none', edgecolor='#5c5c5c', lw=2, linestyle='dashed'))
    ax.plot([-220, -220], [0, 140], linewidth=1, color='#5c5c5c', linestyle='dashed')
    ax.plot([220, 220], [0, 140], linewidth=1, color='#5c5c5c', linestyle='dashed')
    '''
    
    # MID-RANGE MIDDLE
    ax.plot([60, 100], [200, 280], lw=2, linestyle='dashed', color='#5c5c5c')
    ax.plot([-60, -100], [200, 280], lw=2, linestyle='dashed', color='#5c5c5c')
    
    # MID-RANGE WINGS
    ax.plot([132, 213], [135, 185], lw=2, linestyle='dashed', color='#5c5c5c')
    ax.plot([-132, -213], [135, 185], lw=2, linestyle='dashed', color='#5c5c5c')
    
    # 3PT CORNERS
    ax.plot([220, 250], [140, 140], lw=2, linestyle='dashed', color='#5c5c5c')
    ax.plot([-220, -250], [140, 140], lw=2, linestyle='dashed', color='#5c5c5c')
    
    # 3PT WINGS/MIDDLE
    ax.plot([100, 190], [280, 470], lw=2, linestyle='dashed', color='#5c5c5c')
    ax.plot([-100, -190], [280, 470], lw=2, linestyle='dashed', color='#5c5c5c')

    return ax
    
