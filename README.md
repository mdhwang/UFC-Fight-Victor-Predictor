# Let's Get Ready to RUMBLE
## Data Centric Approach to the UFC (Ultimate Fighting Championship)

The purpose of this project is to use historical UFC fight data to determine and identify the tendencies that are most conducive to winning the competition.  Ultimately, the model can be used to predict winners of future fights with some degree of certainty.

Data was obtained from https://www.kaggle.com/rajeevw/ufcdata

5144 bouts ranging from UFC origins in 1993 to mid 2019

Stats for all fighters ranging from the basic statistics (height, weight, age, etc.) to fighter characteristics (ie, avg punches thrown vs landed)

Data was cleaned and missing values determined via KNN 

Data was formatted so each row represented an individual fighter during a particular fight versus the matchup between two fighters as originally formatted.  The result (target) was if they won the fight or not. 

A classifier model (XG Boost Classifier) was trained using data from 2018 and previous and used to predict the outcome and compare to fights that have already occurred in 2019.

After hyperparameter tuning, the model had 62.5% accuracy and identified the following as importnat features:

Age
Average Opponent Takedown %
Average Opponent Significant Strike %
Reach
Average Head Landed

Future work includes fine tuning the decision boundary to become more accurate.
