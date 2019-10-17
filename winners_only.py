
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import math

def dummies(df, col_name):
   return pd.concat([df.drop(col_name, axis=1), pd.get_dummies(df[col_name])], axis=1)

def winners_only_cleaning(df):
    #Removes Unwatned Columns
    #Removes Unwanted Weight Classes
    #Calculate KNN missing Reach Vals
    #Reduce Outlier Data (Weights)
    #Fills Null Values (AGE)
    #Converts Categorical to Dummies
    #Converts Binary to Boolean
    

    #Split data into winners only
    red_winner = df[df["Winner"]=="Red"]
    blue_winner = df[df["Winner"]=="Blue"]


    #Define cols to drop per each
    red_cols = ['R_current_lose_streak',
    'R_current_win_streak',
    'R_draw',
    'R_avg_BODY_att',
    'R_avg_BODY_landed',
    'R_avg_CLINCH_att',
    'R_avg_CLINCH_landed',
    'R_avg_DISTANCE_att',
    'R_avg_DISTANCE_landed',
    'R_avg_GROUND_att',
    'R_avg_GROUND_landed',
    'R_avg_HEAD_att',
    'R_avg_HEAD_landed',
    'R_avg_KD',
    'R_avg_LEG_att',
    'R_avg_LEG_landed',
    'R_avg_PASS',
    'R_avg_REV',
    'R_avg_SIG_STR_att',
    'R_avg_SIG_STR_landed',
    'R_avg_SIG_STR_pct',
    'R_avg_SUB_ATT',
    'R_avg_TD_att',
    'R_avg_TD_landed',
    'R_avg_TD_pct',
    'R_avg_TOTAL_STR_att',
    'R_avg_TOTAL_STR_landed',
    'R_longest_win_streak',
    'R_losses',
    'R_avg_opp_BODY_att',
    'R_avg_opp_BODY_landed',
    'R_avg_opp_CLINCH_att',
    'R_avg_opp_CLINCH_landed',
    'R_avg_opp_DISTANCE_att',
    'R_avg_opp_DISTANCE_landed',
    'R_avg_opp_GROUND_att',
    'R_avg_opp_GROUND_landed',
    'R_avg_opp_HEAD_att',
    'R_avg_opp_HEAD_landed',
    'R_avg_opp_KD',
    'R_avg_opp_LEG_att',
    'R_avg_opp_LEG_landed',
    'R_avg_opp_PASS',
    'R_avg_opp_REV',
    'R_avg_opp_SIG_STR_att',
    'R_avg_opp_SIG_STR_landed',
    'R_avg_opp_SIG_STR_pct',
    'R_avg_opp_SUB_ATT',
    'R_avg_opp_TD_att',
    'R_avg_opp_TD_landed',
    'R_avg_opp_TD_pct',
    'R_avg_opp_TOTAL_STR_att',
    'R_avg_opp_TOTAL_STR_landed',
    'R_total_rounds_fought',
    'R_total_time_fought(seconds)',
    'R_total_title_bouts',
    'R_win_by_Decision_Majority',
    'R_win_by_Decision_Split',
    'R_win_by_Decision_Unanimous',
    'R_win_by_KO/TKO',
    'R_win_by_Submission',
    'R_win_by_TKO_Doctor_Stoppage',
    'R_wins',
    'R_Stance',
    'R_Height_cms',
    'R_Reach_cms',
    'R_Weight_lbs',
    'R_age',
    'R_fighter',
    'B_fighter',
    'Referee',
    'date',
    'location',
    'Winner',
    'title_bout']

    blue_cols = ['B_current_lose_streak',
    'B_current_win_streak',
    'B_draw',
    'B_avg_BODY_att',
    'B_avg_BODY_landed',
    'B_avg_CLINCH_att',
    'B_avg_CLINCH_landed',
    'B_avg_DISTANCE_att',
    'B_avg_DISTANCE_landed',
    'B_avg_GROUND_att',
    'B_avg_GROUND_landed',
    'B_avg_HEAD_att',
    'B_avg_HEAD_landed',
    'B_avg_KD',
    'B_avg_LEG_att',
    'B_avg_LEG_landed',
    'B_avg_PASS',
    'B_avg_REV',
    'B_avg_SIG_STR_att',
    'B_avg_SIG_STR_landed',
    'B_avg_SIG_STR_pct',
    'B_avg_SUB_ATT',
    'B_avg_TD_att',
    'B_avg_TD_landed',
    'B_avg_TD_pct',
    'B_avg_TOTAL_STR_att',
    'B_avg_TOTAL_STR_landed',
    'B_longest_win_streak',
    'B_losses',
    'B_avg_opp_BODY_att',
    'B_avg_opp_BODY_landed',
    'B_avg_opp_CLINCH_att',
    'B_avg_opp_CLINCH_landed',
    'B_avg_opp_DISTANCE_att',
    'B_avg_opp_DISTANCE_landed',
    'B_avg_opp_GROUND_att',
    'B_avg_opp_GROUND_landed',
    'B_avg_opp_HEAD_att',
    'B_avg_opp_HEAD_landed',
    'B_avg_opp_KD',
    'B_avg_opp_LEG_att',
    'B_avg_opp_LEG_landed',
    'B_avg_opp_PASS',
    'B_avg_opp_REV',
    'B_avg_opp_SIG_STR_att',
    'B_avg_opp_SIG_STR_landed',
    'B_avg_opp_SIG_STR_pct',
    'B_avg_opp_SUB_ATT',
    'B_avg_opp_TD_att',
    'B_avg_opp_TD_landed',
    'B_avg_opp_TD_pct',
    'B_avg_opp_TOTAL_STR_att',
    'B_avg_opp_TOTAL_STR_landed',
    'B_total_rounds_fought',
    'B_total_time_fought(seconds)',
    'B_total_title_bouts',
    'B_win_by_Decision_Majority',
    'B_win_by_Decision_Split',
    'B_win_by_Decision_Unanimous',
    'B_win_by_KO/TKO',
    'B_win_by_Submission',
    'B_win_by_TKO_Doctor_Stoppage',
    'B_wins',
    'B_Stance',
    'B_Height_cms',
    'B_Reach_cms',
    'B_Weight_lbs',
    'B_age',
    'B_fighter',
    'R_fighter',
    'Referee',
    'date',
    'location',
    'Winner',
    'title_bout']

    red_winner = red_winner.drop(columns = blue_cols,axis =1)
    blue_winner = blue_winner.drop(columns = red_cols,axis =1)
    
    rename = ['weight_class',
    'no_of_rounds',
    'current_lose_streak',
    'current_win_streak',
    'draw',
    'avg_BODY_att',
    'avg_BODY_landed',
    'avg_CLINCH_att',
    'avg_CLINCH_landed',
    'avg_DISTANCE_att',
    'avg_DISTANCE_landed',
    'avg_GROUND_att',
    'avg_GROUND_landed',
    'avg_HEAD_att',
    'avg_HEAD_landed',
    'avg_KD',
    'avg_LEG_att',
    'avg_LEG_landed',
    'avg_PASS',
    'avg_REV',
    'avg_SIG_STR_att',
    'avg_SIG_STR_landed',
    'avg_SIG_STR_pct',
    'avg_SUB_ATT',
    'avg_TD_att',
    'avg_TD_landed',
    'avg_TD_pct',
    'avg_TOTAL_STR_att',
    'avg_TOTAL_STR_landed',
    'longest_win_streak',
    'losses',
    'avg_opp_BODY_att',
    'avg_opp_BODY_landed',
    'avg_opp_CLINCH_att',
    'avg_opp_CLINCH_landed',
    'avg_opp_DISTANCE_att',
    'avg_opp_DISTANCE_landed',
    'avg_opp_GROUND_att',
    'avg_opp_GROUND_landed',
    'avg_opp_HEAD_att',
    'avg_opp_HEAD_landed',
    'avg_opp_KD',
    'avg_opp_LEG_att',
    'avg_opp_LEG_landed',
    'avg_opp_PASS',
    'avg_opp_REV',
    'avg_opp_SIG_STR_att',
    'avg_opp_SIG_STR_landed',
    'avg_opp_SIG_STR_pct',
    'avg_opp_SUB_ATT',
    'avg_opp_TD_att',
    'avg_opp_TD_landed',
    'avg_opp_TD_pct',
    'avg_opp_TOTAL_STR_att',
    'avg_opp_TOTAL_STR_landed',
    'total_rounds_fought',
    'total_time_fought(seconds)',
    'total_title_bouts',
    'win_by_Decision_Majority',
    'win_by_Decision_Split',
    'win_by_Decision_Unanimous',
    'win_by_KO/TKO',
    'win_by_Submission',
    'win_by_TKO_Doctor_Stoppage',
    'wins',
    'Stance',
    'Height_cms',
    'Reach_cms',
    'Weight_lbs',
    'age']

    red_winner.columns = rename
    blue_winner.columns = rename


    #Combine winners into single DF
    big_winner = red_winner.append(blue_winner,ignore_index=True)
    big_winner = big_winner[~big_winner["avg_BODY_att"].isnull()]


    #Change missing stats to Orthodox ~75% already there
    big_winner["Stance"] = big_winner["Stance"].fillna("Orthodox")


    #Replace Missing Values using KNN
    #Combine all B and R values together for single master list
    r_cols = ["R_Height_cms","R_Reach_cms"]
    b_cols = ["B_Height_cms","B_Reach_cms"]
    header = ["Height","Reach"]

    R_heights_to_reach = df[r_cols]
    R_heights_to_reach.columns = header
    B_heights_to_reach = df[b_cols]
    B_heights_to_reach.columns = header
    MasterHR = R_heights_to_reach.append(B_heights_to_reach,ignore_index=True)

    #Train the KNN Model
    num_neighbors = 3 
    trainer = MasterHR.dropna()
    X = np.array(list(trainer["Height"])).reshape(len(trainer),1)
    y = np.array(list(trainer["Reach"])).reshape(len(trainer),1)
    nay = KNeighborsRegressor(n_neighbors=num_neighbors).fit(X,y)

    #Replace vals with KNN predictions
    big_winner["Reach_cms"] = big_winner.apply(lambda x: nay.predict(np.array(x["Height_cms"]).reshape(1,1))[0][0] if math.isnan(x["Reach_cms"]) else x["Reach_cms"],axis=1)
    
    #Add dummy values (should drop low val stances / weight classes?)
    #big_winner = dummies(big_winner,"weight_class")
    #big_winner = dummies(big_winner,"Stance")
    
    win_pct = (big_winner["wins"]+1) / (big_winner["wins"] + 1 + big_winner["losses"])

    big_winner["age"] = big_winner["age"].fillna(big_winner["age"].mean())





    drop_cols = [
        'draw',
        'wins',
        'losses',
        'longest_win_streak',
        'current_lose_streak',
        'current_win_streak',
        'total_title_bouts',
        'win_by_Decision_Majority',
        'win_by_Decision_Split',
        'win_by_Decision_Unanimous',
        'win_by_KO/TKO',
        'win_by_Submission',
        'win_by_TKO_Doctor_Stoppage',
        'weight_class',
        'Stance'
    ]
    
    big_winner = big_winner.drop(columns = drop_cols)



    return big_winner, win_pct