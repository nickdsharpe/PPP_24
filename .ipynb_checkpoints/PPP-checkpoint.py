import pandas as pd
import numpy as np

def PPP(data):

    #Grab the column headers
    headers = data.columns

    # Assign shooting data to new variables
    shoot2FGA = data.loc['shoot2FGA'].sum().sum()
    shoot2FGM = data.loc['shoot2FGM'].sum().sum()
    shoot2FTA = data.loc['shoot2FTA'].sum().sum()
    shoot2FTM = data.loc['shoot2FTM'].sum().sum()
    shoot2TO = data.loc['shoot2TO'].sum().sum()
    shoot2SQ = data.loc['shootSQ2'].sum().sum()
    shoot3FGA = data.loc['shoot3FGA'].sum().sum()
    shoot3FGM = data.loc['shoot3FGM'].sum().sum()
    shoot3FTA = data.loc['shoot3FTA'].sum().sum()
    shoot3FTM = data.loc['shoot3FTM'].sum().sum()
    shoot3TO = data.loc['shoot3TO'].sum().sum()
    shoot3SQ = data.loc['shootSQ3'].sum().sum()
   
    # Assign passing data to new variables
    pass2FGA = data.loc['pass2FGA'].sum().sum()
    pass2FGM = data.loc['pass2FGM'].sum().sum()
    pass2FTA = data.loc['pass2FTA'].sum().sum()
    pass2FTM = data.loc['pass2FTM'].sum().sum()
    pass2TO = data.loc['pass2TO'].sum().sum()
    pass2SQ = data.loc['passSQ2'].sum().sum()
    pass3FGA = data.loc['pass3FGA'].sum().sum()
    pass3FGM = data.loc['pass3FGM'].sum().sum()
    pass3FTA = data.loc['pass3FTA'].sum().sum()
    pass3FTM = data.loc['pass3FTM'].sum().sum()
    pass3TO = data.loc['pass3TO'].sum().sum()
    pass3SQ = data.loc['passSQ3'].sum().sum()
    
    # Average out passing Shot Quality, mark as N/A if no FGA's
    if pass2FGA > 0:
        passing2SQ = round((pass2SQ / pass2FGA),2)
    else:
        passing2SQ = 'N/A'
        
    if pass3FGA > 0:
        passing3SQ = round((pass3SQ / pass3FGA),2)
    else:
        passing3SQ = 'N/A'
    
    # Create Overall data variables
    FGA2 = pass2FGA + shoot2FGA
    FGM2 = pass2FGM + shoot2FGM
    FTA2 = pass2FTA + shoot2FTA
    FTM2 = pass2FTM + shoot2FTM
    TO2 = pass2TO + shoot2TO
    FGA3 = pass3FGA + shoot3FGA
    FGM3 = pass3FGM + shoot3FGM
    FTA3 = pass3FTA + shoot3FTA
    FTM3 = pass3FTM + shoot3FTM
    TO3 = pass3TO + shoot3TO
    
    # FGA
    tot3FGA = shoot3FGA + pass3FGA
    tot2FGA = shoot2FGA + pass2FGA
    passFGA = pass2FGA + pass3FGA
    shootFGA = shoot2FGA + shoot3FGA
    totFGA = shoot2FGA + pass2FGA + shoot3FGA + pass3FGA
    
    # FTA Totals
    totFTA = FTA2 + FTA3
    shootFTA = shoot2FTA + shoot3FTA
    passFTA = pass2FTA + pass3FTA
    
    # Points
    total_points = ((shoot3FGM + pass3FGM) * 3) + ((shoot2FGM + pass2FGM) * 2) + (shoot2FTM + shoot3FTM + pass3FTM + pass2FTM)
    shooting_points = (shoot3FGM * 3) + (shoot2FGM *2) + (shoot3FTM + shoot2FTM)
    passing_points = (pass3FGM * 3) + (pass2FGM *2) + (pass3FTM + pass2FTM)
    
    # True Shooting Percentage
    tot_trueshooting_per = str(round(((0.5 * total_points) / ((FGA2 + FGA3) + (0.44 * (FTM2 + FTM3))))* 100, 2))
    shooting_trueshooting_per = str(round(((0.5 * shooting_points) / ((shootFGA) + (0.44 * (shoot2FTM + shoot3FTM))))* 100, 2))
    passing_trueshooting_per = str(round(((0.5 * passing_points) / ((passFGA) + (0.44 * (pass2FTM + pass3FTM))))* 100, 2))
    
    # Shooting Possessions
    shootPoss_totOVR = int((shoot2FGA + (0.44*(shoot2FTA + shoot3FTA)) + shoot2TO + shoot3FGA + shoot3TO))
    shootPoss_2pt = int((shoot2FGA + (0.44 * shoot2FTA) + shoot2TO))
    shootPoss_3pt = int((shoot3FGA + (0.44 * shoot3FTA) + shoot3TO))
    
    # Passing Possessions
    passingPoss_totOVR = int((pass2FGA + (0.44*(pass2FTA + pass3FTA)) + pass2TO + pass3FGA + pass3TO))
    passingPoss_2pt = int((pass2FGA + (.044 * pass2FTA) + pass2TO))
    passingPoss_3pt = int((pass3FGA + (0.44 * pass3FTA) + pass3TO))
    
    # Total Possessions
    totPossOVR = (shootPoss_totOVR + passingPoss_totOVR)
    totPoss_2ptOVR = (shootPoss_2pt + passingPoss_2pt)
    totPoss_3ptOVR = (shootPoss_3pt + passingPoss_3pt)  
    
    # Total turnovers and turnover percentage
    total_to = TO2 + TO3
    total_to_per = round((((total_to * 100) / totPossOVR)),1)
    
    # Shooting Turnovers and Turnover Percentage
    shooting_total_to = shoot2TO + shoot3TO
    shooting_to_per = round(((shooting_total_to * 100) / shootPoss_totOVR),2)
    
    # Passing Turnovers and Turnover Percentage
    passing_total_to = pass2TO + pass3TO
    passing_to_per = round(((passing_total_to * 100) / passingPoss_totOVR),2)
    
    # Passing Shot Quality
    passingSQ = pass2SQ + pass3SQ
    passingSQ = round((passingSQ / passFGA),2)
    
    # Shooting Shot Quality
    shootingSQ = shoot2SQ + shoot3SQ
    shootingSQ = round((shootingSQ / shootFGA),2)
    
    # Total Shot Quality
    SQ2 = pass2SQ + shoot2SQ
    SQ3 = pass3SQ + shoot3SQ
    totalSQ = SQ2 + SQ3
    totalSQ = round((totalSQ / totFGA),2)
    
    # Calculate shooting, passing, and total Points per Possesion
    shootingPPP_tot = round(((shoot2FGM * 2) + (shoot3FGM * 3) + (shoot2FTM + shoot3FTM)) / ((shoot2FGA + shoot3FGA) + ((shoot2FTA + shoot3FTA) * 0.44) + (shoot2TO + shoot3TO)),2)
    shootingPPP_2pt = round(((shoot2FGM * 2) + shoot2FTM) / (shoot2FGA + (shoot2FTA * 0.44) + shoot2TO),2)
    shootingPPP_3pt = round(((shoot3FGM * 3) + shoot3FTM) / (shoot3FGA + (shoot3FTA * 0.44) + shoot3TO),2)
    passingPPP_tot = round(((pass2FGM * 2) + (pass3FGM * 3) + (pass2FTM + pass3FTM)) / ((pass2FGA + pass3FGA) + ((pass2FTA + pass3FTA) * 0.44) + (pass2TO + pass3TO)),2)
    passingPPP_2pt = round(((pass2FGM * 2) + pass2FTM) / (pass2FGA + (pass2FTA * 0.44) + pass2TO),2)
    passingPPP_3pt = round(((pass3FGM * 3) + pass3FTM) / (pass3FGA + (pass3FTA * 0.44) + pass3TO),2)
    ppp_2pt = round((((shoot2FGM + pass2FGM)* 2) + (shoot2FTM + pass2FTM)) / ((shoot2FGA + pass2FGA) + (0.44 *  (shoot2FTA + pass2FTA)) + (shoot2TO + pass2TO)),2)
    ppp_3pt = round((((shoot3FGM + pass3FGM) * 3) + (shoot3FTM + pass3FTM)) / ((shoot3FGA + pass3FGA) + (0.44 * (shoot3FTA + pass3FTA)) + (shoot3TO + pass3TO)),2)
    ppp_tot = round(((FGM2 * 2) + (FGM3 * 3) + (FTM2 + FTM3)) / ((FGA2 + FGA3) + ((FTA2 + FTA3) * 0.44) + (TO2 + TO3)),2)
    
    # Total Free Throw Rate
    if totFGA > 0:
        tot_FTR = round((totFTA / totFGA),2)
    elif totFTA > 0 and totFGA == 0:
        tot_FTR = 1.0
    else:
        tot_FTR = 0.0
    
    # Shooting Free Throw Rate
    if shootFGA > 0:
        shoot_FTR = round((shootFTA / shootFGA),2)
    elif shootFTA > 0 and shootFGA == 0:
        shoot_FTR = 1.0
    else:
        shoot_FTR = 0.0
    
    # Creation Free Throw Rate
    if passFGA > 0:
        pass_FTR = round((passFTA / passFGA),2)
    elif passFTA > 0 and passFGA == 0:
        pass_FTR = 1.0
    else:
        pass_FTR = 0.0
    
    # TOTAL 2pt and 3pt Shot Quality
    if FGA2 > 0:
        SQ_2pt = round((SQ2 / FGA2),2)
    else:
        SQ_2pt = 'N/A'
    if FGA3 > 0:
        SQ_3pt = round((SQ3 / FGA3),2)
    else:
        SQ_3pt = 'N/A'
        
    # SHOOTING 2pt and 3pt Shot Quality
    if shoot2FGA > 0:
        shooting_SQ_2pt = round((shoot2SQ / shoot2FGA),2)
    else:
        shooting_SQ_2pt = 'N/A'
    if shoot3FGA > 0:
        shooting_SQ_3pt = round((shoot3SQ / shoot3FGA),2)
    else:
        shooting_SQ_3pt = 'N/A'
    
    # PASSING 2pt and 3pt Shot Quality
    if pass2FGA > 0:
        passing_SQ_2pt = round((pass2SQ / pass2FGA),2)
    else:
        passing_SQ_2pt = 'N/A'
    if pass3FGA > 0:
        passing_SQ_3pt = round((pass3SQ / pass3FGA),2)
    else:
        passing_SQ_3pt = 'N/A'
    
    # Creation Percentage  
    try:
        passingPoss_perOVR = round(((passingPoss_totOVR / totPossOVR)*100),1)
    except(ZeroDivisionError):
        passingPoss_perOVR = 0
        
    # Percentage of Shooting Poss.
    try:
        shootingPoss_perOVR = round(((shootPoss_totOVR / totPossOVR)*100),1)
    except(ZeroDivisionError):
        shootingPoss_perOVR = 0
        
    # OVR FG percentage    
    try:
        totFG_per = round(((shoot2FGM + shoot3FGM + pass2FGM + pass3FGM) / (shoot2FGA + pass2FGA + shoot3FGA + pass3FGA)* 100),1)
    except(ZeroDivisionError):
        totFG_per = 'N/A'
        
    try:
        shootFG_per = round((((shoot2FGM + shoot3FGM) / (shoot2FGA + shoot3FGA))*100),1)
    except(ZeroDivisionError):
        shootFG_per = 'N/A'
        
    try:
        passFG_per = round((((pass2FGM + pass3FGM) / (pass2FGA + pass3FGA))*100),1)
    except(ZeroDivisionError):
        passFG_per = 'N/A'
    
    # 2pt FG percentage
    try:
        tot2FG_per = round((((pass2FGM + shoot2FGM) / (pass2FGA + shoot2FGA))*100),1)
    except(ZeroDivisionError):
        tot2FG_per = 'N/A'
        
    try:
        shoot2FG_per = round((((shoot2FGM) / (shoot2FGA))* 100), 1)
    except(ZeroDivisionError):
        shoot2FG_per = 'N/A'
        
    try:
        pass2FG_per = round((((pass2FGM) / (pass2FGA))* 100), 1)
    except(ZeroDivisionError):
        pass2FG_per = 'N/A'
    
    # 3pt FG percentage    
    try:
        tot3FG_per = round((((pass3FGM + shoot3FGM) / (pass3FGA + shoot3FGA))*100),1)
    except(ZeroDivisionError):
        tot3FG_per = 'N/A'
        
    try:
        if shoot3FGA == 0:  
            shoot3FG_per = 'N/A'
        else:
            shoot3FG_per = round((((shoot3FGM) / (shoot3FGA))* 100), 1)
    except:
        shoot3FG_per = 'N/A'
        
    try:
        pass3FG_per = round((((pass3FGM) / (pass3FGA))* 100), 1)
    except(ZeroDivisionError):
        pass3FG_per = 'N/A'
    
    # Create the index
    index = ['Total PPP', '% of Poss.', 'Total TO', 'Total Creation %', 'Total FTR', 'Total TS%', 'Total SQ' ,'Total 2pt FGA','Total 2pt FG%', 'Total 2pt SQ', 'Total 3pt FGA','Total 3pt FG%', 'Total 3pt SQ', 'Shooting PPP', '% of Shooting Poss.', 'Shooting TO', 'Shooting Freq.', 'Shooting FTR', 'Shooting TS%', 'Shooting SQ', 'Shooting 2pt Poss.', 'Shooting 2pt FG%', 'Shooting 2pt SQ', 'Shooting 3pt Poss.', 'Shooting 3pt FG%', 'Shooting 3pt SQ', 'Creation PPP', '% of Creation Poss.', 'Creation TO', 'Creation %', 'Creation FTR', 'Creation TS%', 'Creation SQ', 'Creation 2pt Poss.', 'Creation 2pt FG%', 'Creation 2pt SQ', 'Creation 3pt Poss.', 'Creation 3pt FG%', 'Creation 3pt SQ']   
    
    # Create the PPP DataFrame
    data_df = pd.DataFrame(columns=headers, index=index)
    
    #Create the 'TOTAL' column at the end of the dataframe
    data_df['TOTAL'] = [str(ppp_tot), (str(totPossOVR)), str(total_to_per), str(passingPoss_perOVR), str(tot_FTR), str(tot_trueshooting_per), str(totalSQ), str(tot2FGA), str(tot2FG_per), str(SQ_2pt), str(tot3FGA), str(tot3FG_per), str(SQ_3pt), str(shootingPPP_tot), str(shootPoss_totOVR), str(shooting_to_per), str(shootingPoss_perOVR), str(shoot_FTR), str(shooting_trueshooting_per), str(shootingSQ), str(shootPoss_2pt), str(shoot2FG_per), str(shooting_SQ_2pt), str(shootPoss_3pt), str(shoot3FG_per), str(shooting_SQ_3pt), str(passingPPP_tot), str(passingPoss_totOVR), str(passing_to_per), str(passingPoss_perOVR), str(pass_FTR), str(passing_trueshooting_per), str(passingSQ), str(passingPoss_2pt), str(pass2FG_per), str(passing_SQ_2pt), str(passingPoss_3pt), str(pass3FG_per), str(shooting_SQ_3pt)]
    
    # Create dictionary for each column
    col_dicts = {col_name: data[col_name].to_dict() for col_name in data.columns}
    
    # Loop over each column dictionary to create new calculated column
    for i, col_dict in col_dicts.items():
        
        shoot2FGA = col_dict['shoot2FGA']
        shoot2FGM = col_dict['shoot2FGM']
        shoot2FTA = col_dict['shoot2FTA']
        shoot2FTM = col_dict['shoot2FTM']
        shoot2TO = col_dict['shoot2TO']
        shoot2SQ = col_dict['shootSQ2']
        shoot3FGA = col_dict['shoot3FGA']
        shoot3FGM = col_dict['shoot3FGM']
        shoot3FTA = col_dict['shoot3FTA']
        shoot3FTM = col_dict['shoot3FTM']
        shoot3TO = col_dict['shoot3TO']
        shoot3SQ = col_dict['shootSQ3']

        pass2FGA = col_dict['pass2FGA']
        pass2FGM = col_dict['pass2FGM']
        pass2FTA = col_dict['pass2FTA']
        pass2FTM = col_dict['pass2FTM']
        pass2TO = col_dict['pass2TO']
        pass2SQ = col_dict['passSQ2']
        pass3FGA = col_dict['pass3FGA']
        pass3FGM = col_dict['pass3FGM']
        pass3FTA = col_dict['pass3FTA']
        pass3FTM = col_dict['pass3FTM']
        pass3TO = col_dict['pass3TO']
        pass3SQ = col_dict['passSQ3']

        FGA2 = pass2FGA + shoot2FGA
        FGM2 = pass2FGM + shoot2FGM
        FTA2 = pass2FTA + shoot2FTA
        FTM2 = pass2FTM + shoot2FTM
        TO2 = pass2TO + shoot2TO
        SQ2 = shoot2SQ + pass2SQ
        FGA3 = pass3FGA + shoot3FGA
        FGM3 = pass3FGM + shoot3FGM
        FTA3 = pass3FTA + shoot3FTA
        FTM3 = pass3FTM + shoot3FTM
        TO3 = pass3TO + shoot3TO
        SQ3 = shoot3SQ + pass3SQ
        
        # FGA Totals
        totFGA = (shoot2FGA + pass2FGA + shoot3FGA + pass3FGA)
        shootFGA = shoot2FGA + shoot3FGA
        passFGA = (pass2FGA + pass3FGA)
        
        # FGA for 2's, and 3's
        tot2FGA = shoot2FGA + pass2FGA
        tot3FGA = shoot3FGA + pass3FGA
        
        # FTA Totals
        totFTA = FTA2 + FTA3
        shootFTA = shoot2FTA + shoot3FTA
        passFTA = pass2FTA + pass3FTA
        
        # Points
        total_points = ((shoot3FGM + pass3FGM) * 3) + ((shoot2FGM + pass2FGM) * 2) + (shoot2FTM + shoot3FTM + pass3FTM + pass2FTM)
        shooting_points = (shoot3FGM * 3) + (shoot2FGM *2) + (shoot3FTM + shoot2FTM)
        passing_points = (pass3FGM * 3) + (pass2FGM *2) + (pass3FTM + pass2FTM)
        
        # Turnovers
        total_to = TO2 + TO3
        shoot_to = shoot2TO + shoot3TO
        pass_to = pass2TO + pass3TO
        
        # Shooting Possessions
        shootPoss_tot = shoot2FGA + (0.44*(shoot2FTA + shoot3FTA)) + shoot2TO + shoot3FGA + shoot3TO
        shootPoss_2pt = int((shoot2FGA + (0.44 * shoot2FTA) + shoot2TO))
        shootPoss_3pt = int((shoot3FGA + (0.44 * shoot3FTA) + shoot3TO))
        
        # Passing Possessions
        passingPoss_tot =  pass2FGA + (0.44*(pass2FTA + pass3FTA)) + pass2TO + pass3FGA + pass3TO
        passingPoss_2pt = int((pass2FGA + (0.44 * pass2FTA) + pass2TO))
        passingPoss_3pt = int((pass3FGA + (0.44 * pass3FTA) + pass3TO))
        
        # Total Possessions
        totPoss = (shootPoss_tot + passingPoss_tot)
        totPoss_2pt = (shootPoss_2pt + passingPoss_2pt)
        totPoss_3pt = (shootPoss_3pt + passingPoss_3pt)
        
        # Total Shot Quality
        SQ2 = pass2SQ + shoot2SQ
        SQ3 = pass3SQ + shoot3SQ
        totalSQ = SQ2 + SQ3
        
        # Shot Quality for 2' and 3's
        if FGA2 > 0:
            SQ_2pt = round((SQ2 / FGA2),2)
        else:
            SQ_2pt = 'N/A'
        if FGA3 > 0:
            SQ_3pt = round((SQ3 / FGA3),2)
        else:
            SQ_3pt = 'N/A'
            
        if totFGA > 0:
            try:
                totalSQ = round((totalSQ / totFGA),2)
            except:
                totalSQ = 'N/A'
            
        # Average out shooting Shot Quality, mark as N/A if no FGA's
        if shoot2FGA > 0:
            shooting2SQ = round((shoot2SQ / shoot2FGA),2)
        else:
            shooting2SQ = 'N/A'

        if shoot3FGA > 0:
            shooting3SQ = round((shoot3SQ / shoot3FGA),2)
        else:
            shooting3SQ = 'N/A'

        shootingSQ = shoot2SQ + shoot3SQ
        try:
            shootingSQ = round((shootingSQ / shootFGA),2)
        except(ZeroDivisionError):
            shootingSQ = 'N/A'
            
        # Average out Passing Shot Quality, mark as N/A if no FGA's
        if pass2FGA > 0:
            passing2SQ = round((pass2SQ / pass2FGA),2)
        else:
            passing2SQ = 'N/A'

        if pass3FGA > 0:
            try:
                passing3SQ = round((pass3SQ / pass3FGA),2)
            except:
                passing3SQ = 'N/A'

        passingSQ = pass2SQ + pass3SQ
        try:
            passingSQ = round((passingSQ / passFGA),2)
        except(ZeroDivisionError):
            passingSQ = 'N/A'
            
        # Total Free Throw Rate
        if totFGA > 0:
            tot_FTR = round((totFTA / totFGA),2)
        elif totFTA > 0 and totFGA == 0:
            totFTR = 1.0
        else:
            tot_FTR = 0.0
            
        # Shooting Free Throw Rate
        if shootFGA > 0:
            shoot_FTR = round((shootFTA / shootFGA),2)
        elif shootFTA > 0 and shootFGA == 0:
            shoot_FTR = 1.0
        else:
            shoot_FTR = 0.0
        
        # Creation Free Throw Rate
        if passFGA > 0:
            pass_FTR = round((passFTA / passFGA),2)
        elif passFTA > 0 and passFGA == 0:
            pass_FTR = 1.0
        else:
            pass_FTR = 0.0
        
        # Total True Shooting Percentage
        try:
            tot_trueshooting_per = str(round(((0.5 * total_points) / ((totFGA) + (0.44 * (FTM2 + FTM3))))* 100, 2))
        except(ZeroDivisionError):
            tot_trueshooting_per = 'N/A'
                                    
        # Shooting True Shooting Percentage
        try:
            shooting_trueshooting_per = str(round(((0.5 * shooting_points) / ((shootFGA) + (0.44 * (shoot2FTM + shoot3FTM))))* 100, 2))
        except(ZeroDivisionError):
            shooting_trueshooting_per = 'N/A'
            
        # Passing True Shooting Percentage
        try:
            passing_trueshooting_per = str(round(((0.5 * passing_points) / ((passFGA) + (0.44 * (pass2FTM + pass3FTM))))* 100, 2))
        except(ZeroDivisionError):
            passing_trueshooting_per = 'N/A'
            
        # Shooting PPP
        try:
            shootingPPP_tot = round(((shoot2FGM * 2) + (shoot3FGM * 3) + (shoot2FTM + shoot3FTM)) / ((shoot2FGA + shoot3FGA) + ((shoot2FTA + shoot3FTA) * 0.44) + (shoot2TO + shoot3TO)),2)
        except(ZeroDivisionError):
            shootingPPP_tot = 'N/A'
            
        try:
            shootingPPP_2pt = round(((shoot2FGM * 2) + shoot2FTM) / (shoot2FGA + (shoot2FTA * 0.44) + shoot2TO),2)
        except(ZeroDivisionError):
            shootingPPP_2pt = 'N/A'
            
        try:
            shootingPPP_3pt = round(((shoot3FGM * 3) + shoot3FTM) / (shoot3FGA + (shoot3FTA * 0.44) + shoot3TO),2)
        except(ZeroDivisionError):
            shootingPPP_3pt = 'N/A'
        
        # Shooting Possession Percentage
        try:
            shootPoss_per = round(((shootPoss_tot / shootPoss_totOVR)*100),1)
        except(ZeroDivisionError):
            shootPoss_per = 'N/A'
            
        # Passing Possession Percentage
        try:
            passPoss_per = round(((passingPoss_tot / passingPoss_totOVR)*100),1)
        except(ZeroDivisionError):
            passPoss_per = 'N/A'
            
        # Shooting FG Percentage
        try:
            shootFG_per = round((((shoot2FGM + shoot3FGM) / (shoot2FGA + shoot3FGA))*100),1)
        except(ZeroDivisionError):
            shootFG_per = 'N/A'
            
        try:
            shoot2FG_per = round((((shoot2FGM) / (shoot2FGA))* 100), 1)
        except(ZeroDivisionError):
            shoot2FG_per = 'N/A'
            
        try:
            shoot3FG_per = round((((shoot3FGM) / (shoot3FGA))* 100), 1)
        except(ZeroDivisionError):
            shoot3FG_per = 'N/A'
            
        # Passing FG Percentage    
        try:
            passFG_per = round((((pass2FGM + pass3FGM) / (pass2FGA + pass3FGA))*100),1)
        except(ZeroDivisionError):
            passFG_per = 'N/A'
            
        try:
            pass2FG_per = round((((pass2FGM) / (pass2FGA))* 100), 1)
        except(ZeroDivisionError):
            pass2FG_per = 'N/A'
            
        try:
            pass3FG_per = round((((pass3FGM) / (pass3FGA))* 100), 1)
        except(ZeroDivisionError):
            pass3FG_per = 'N/A'

        # Passing PPP
        try:
            passingPPP_tot = round(((pass2FGM * 2) + (pass3FGM * 3) + (pass2FTM + pass3FTM)) / ((pass2FGA + pass3FGA) + ((pass2FTA + pass3FTA) * 0.44) + (pass2TO + pass3TO)),2)
        except(ZeroDivisionError):
            passingPPP_tot = 'N/A'
            
        try:
            passingPPP_2pt = round(((pass2FGM * 2) + pass2FTM) / (pass2FGA + (pass2FTA * 0.44) + pass2TO),2)
        except(ZeroDivisionError):
            passingPPP_2pt = 'N/A'
            
        try:
            passingPPP_3pt = round(((pass3FGM * 3) + pass3FTM) / (pass3FGA + (pass3FTA * 0.44) + pass3TO),2)
        except(ZeroDivisionError):
            passingPPP_3pt = 'N/A'
        
        # Creation Percantage
        try:
            passingPoss_per = round(((passingPoss_tot / totPoss)*100),1)
        except(ZeroDivisionError):
            passingPoss_per = 0
        
        # Shooting Frequency
        try:
            shootingFreq_per = round(((shootPoss_tot / totPoss)*100),1)
        except(ZeroDivisionError):
            shootingFreq_per = 0
        
        # PPP for 2's, 3's, and TOTAL
        try:
            ppp_2pt = round((((shoot2FGM + pass2FGM)* 2) + (shoot2FTM + pass2FTM)) / ((shoot2FGA + pass2FGA) + (0.44 *  (shoot2FTA + pass2FTA)) + (shoot2TO + pass2TO)),2)
        except(ZeroDivisionError):
            ppp_2pt = 'N/A'
        
        try:
            ppp_3pt = round((((shoot3FGM + pass3FGM) * 3) + (shoot3FTM + pass3FTM)) / ((shoot3FGA + pass3FGA) + (0.44 * (shoot3FTA + pass3FTA)) + (shoot3TO + pass3TO)),2)
        except(ZeroDivisionError):
            ppp_3pt = 'N/A'
            
        try:
            ppp_tot = round(((FGM2 * 2) + (FGM3 * 3) + (FTM2 + FTM3)) / ((FGA2 + FGA3) + ((FTA2 + FTA3) * 0.44) + (TO2 + TO3)),2)
        except(ZeroDivisionError):
            ppp_tot = 'N/A'
        
        # Percentage of Possession
        try:
            totPoss_per = round(((totPoss / totPossOVR)*100),1)
        except(ZeroDivisionError):
            totPoss_per = 'N/A'
            
        # FG Percentage
        try: 
            totFG_per = round((((shoot2FGM + shoot3FGM + pass2FGM + pass3FGM) / (shoot2FGA + pass2FGA + shoot3FGA + pass3FGA))* 100),1)
        except(ZeroDivisionError):
            totFG_per = 'N/A'
            
        try:
            tot2FG_per = round((((pass2FGM + shoot2FGM) / (pass2FGA + shoot2FGA))*100),1)
        except(ZeroDivisionError):
            tot2FG_per = 'N/A'
            
        try:
            tot3FG_per = round((((pass3FGM + shoot3FGM) / (pass3FGA + shoot3FGA))*100),1)
        except(ZeroDivisionError):
            tot3FG_per = 'N/A'
       
        data_df[i] = [str(ppp_tot), str((totPoss_per)), str(total_to), str(passingPoss_per), str(tot_FTR), str(tot_trueshooting_per), str(totalSQ), str(FGA2), str(tot2FG_per), str(SQ_2pt), str(FGA3), str(tot3FG_per), str(SQ_3pt), str(shootingPPP_tot), str(shootPoss_per), str(shoot_to), str(shootingFreq_per), str(shoot_FTR), str(shooting_trueshooting_per), str(shootingSQ), str(shootPoss_2pt), str(shoot2FG_per), str(shooting2SQ), str(shootPoss_3pt), str(shoot3FG_per), str(shooting3SQ), str(passingPPP_tot), str(passPoss_per), str(pass_to), str(passingPoss_per), str(pass_FTR), str(passing_trueshooting_per), str(passingSQ), str(passingPoss_2pt), str(pass2FG_per), str(passing2SQ), str(passingPoss_3pt), str(pass3FG_per), str(shooting3SQ)]
           
    # Rename column headers
    data_df = data_df.rename(columns={'PNR BH' : 'PNR Ball Handler', 'PNR SC' : 'PNR Screener', "DHO BH" : "DHO Ball Handler", "DHO SC" : "DHO Screener",
"ISO" : "ISOLATION", "TRAN" : "TRANSITION", "ACO" : "Attacking Closeouts", "C/S" : "Catch & Shoot", "OBS" : "Off Ball Screens", "CUT" : "Cutting", "OREB" : "Off. Rebounds"})
    
    data_df = data_df.transpose()
    
    return(data_df)