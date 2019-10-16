
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
import math

def dummies(df, col_name):
   return pd.concat([df.drop(col_name, axis=1), pd.get_dummies(df[col_name])], axis=1)

def data_cleaning(df):
    #Removes Unwatned Columns
    #Removes Unwanted Weight Classes
    #Calculate KNN missing Reach Vals
    #Reduce Outlier Data (Weights)
    #Fills Null Values (AGE)
    #Converts Categorical to Dummies
    #Converts Binary to Boolean
    

    #define wanted columns from OG data
    desired_cols = [
        'Winner',
        'weight_class',
        'B_age',
        'B_Height_cms',
        'B_Reach_cms',
        'B_Weight_lbs',
        'R_Height_cms',
        'R_Reach_cms',
        'R_Weight_lbs',
        'R_age',]

    df = df[desired_cols]


    #Fill NaN age values with column means ¯\_(ツ)_/¯
    df["B_age"] = df["B_age"].fillna(df["B_age"].mean())
    df["R_age"] = df["R_age"].fillna(df["R_age"].mean())
    

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
    df["R_Reach_cms"] = df.apply(lambda x: nay.predict(np.array(x["R_Height_cms"]).reshape(1,1))[0][0] if math.isnan(x["R_Reach_cms"]) else x["R_Reach_cms"],axis=1)
    df["B_Reach_cms"] = df.apply(lambda x: nay.predict(np.array(x["B_Height_cms"]).reshape(1,1))[0][0] if math.isnan(x["B_Reach_cms"]) else x["B_Reach_cms"],axis=1)


    #Remove unwanted weight divisions (ROWS)
    to_drop = ['Open Weight',
               'Catch Weight',
               "Women's Strawweight",
               "Women's Flyweight",
               "Women's Bantamweight",
               "Women's Featherweight"]
    for each in to_drop:
        df = df[df["weight_class"]!=each]
    
    #Convert Binary Winner to Boolean
    df["Winner"] = df["Winner"].apply(lambda x: True if x == "Red" else False)
    
    #Calculate Delta Values (RED WINNER MINUS BLUE LOSER)
    df["Reach_Delta"] = df["R_Reach_cms"] - df["B_Reach_cms"]
    df["Height_Delta"] = df["R_Height_cms"] - df["B_Height_cms"]
    df["Weight_Delta"] = df["R_Weight_lbs"] - df["B_Weight_lbs"]
    df["age_Delta"] = df["R_age"] - df["B_age"]
    
    
    #Drop Figthers over the 265 Heavyweight limit
    df = df[df["R_Weight_lbs"]<=265]
    df = df[df["B_Weight_lbs"]<=265]
    
    #Drop Red vs Blue Data Columns
    cols = ["R_Reach_cms",
            "B_Reach_cms",
            "R_Height_cms",
            "B_Height_cms",
            "R_Weight_lbs",
            "B_Weight_lbs",
            "R_age",
            "B_age"]
    df = df.drop(columns = cols)
    
    df = dummies(df,"weight_class")
    
    
    return df