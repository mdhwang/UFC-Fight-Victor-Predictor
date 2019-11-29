# UFC Fight Victor Predictor
## Data Centric Approach to the UFC (Ultimate Fighting Championship) - Let's Get Ready to Rumble!

## Setting the Stage

Friday, October 18th, 2019, UFC on ESPN 6 Main Event - Dominick Reyes vs. Chris Weidman Light Heavyweight bout.  
Question on everyone's mind was who was going to win the fight?  
The only question on my mind was can I train a machine learning algorithm to answer that question for me?

The UFC (Ultimate Fighting Championship) is a modern day gladiator style competition where two fighters enter the octagon arena to test their hand to hand combat skills against each other to determine who is the superior fighter.

![](/images/UFC.png)

With available historical UFC fight data from (www.UFCstats.com), this information can be used to train a statistical model to predict (with hopefully some degree of certainty) the winner of an upcoming fight.

Of course there are countless unknowns and confounding variables outside the scope of this dataset that will limit the efectiveness of this model, but hey, why not?

Fortunately user Rajeevw on Kaggle developed a webscriping process to pull the data from www.UFCstats.com seen here:

[Kaggle Link!](https://www.kaggle.com/rajeevw/ufcdata)

Shout out to you Rajeevw, you da real MVP.

## Inisde the Data

The dataset contained 5144 total fights ranging from the conception of the UFC in 1993 to mid 2019 when the data was collected.  

![UFC Fights Over Time](/images/FightsVsYear.png)

There was a spike in interest in the UFC starting in 2005 which can mainly attributed to the premier of The Ultimate Fighter on Spike TV and the popularity of Monster Energy drinks.

![The Ultimate Fighter](/images/tuf.png)

Here is an intial peek at the dataset:

![snapshot](/images/dataset_snapshot.png)


Each row inside this dataset represents a completed fight between two competitors.  Their individual stats leading up to the fight are given as well as the winner of the fight.

There are basic stats such as:
- Age
- Height
- Weight
- Reach
- etc.

But there are also some more interesting behavioral stats given that are more indicative of style such as:
- Punches Attempted / Landed
- Kicks Attempted / Landed
- Takedowns Attempted / Landed
- etc.

I wanted to determine from this data if there are any commonalities / differences of the traits between winners and losers in the UFC and identify key indicators of winning.

## EDA - Exploratory Data Analysis

Dataset was split and grouped into the winners and losers to see if there are any obvious trends right off the bat.

GRAPH

GRAPH

GRAPH

GRAPH

Results make intuitive sense, but there are underlying complexities that can be uncovered with Machine Learning.

## Data Pre-Processing

Prior to any processing, a couple of gaps in the data were identified through EDA.  Many of the fighter's reach information was missing as well as a small number of easy lookup values.

Luckily there is a strong correlation between a human's height and arm length:

GRAPH

So I used KNN to fill in the missing NaN values.

Now the data was filled, it was reconfigured into a single dataframe with winner and losing being the labels of a binary classifier.

This allows us to hone in on the traits of winners and losers

The dataset was also split with the fights that occured in 2019 to be used as a test validation set and all fights from 1993 to 2018 to be used to train the model.


HOWEVER, this big caveat is that we lose the "matchup" portion as we are looking at the fighters individually versus against a specific opponent.



## Modeling

Multiple statistical classification models with tested to see which performed the best with the task at hand.  

- Logisitic Regression Classifier
- Random Forest Classifier
- XG Boost Classifier

A grid search was performed to tune the hyperparameters of each model to see which yielded the highest accuracy.


## Results

XGBOOST ended up being the most accurate with a score of ______

Most influential characteristics were identified as:
- Age
- Reach
- Opponent landed hits low

Which make intuitive sense.

Errors looked like _______, other conclusions here

## Back to the Topic

Regarding the Reyes vs. Weidman fight, my model predicted the below:

Dominick Reyes - 62% chance of winning a future fight
Chris Weidman - 53% chance of winning a future fight

Since I was sleep deprived and hyped at the time, I decided it would be a good idea to put money down and put full faith into my model by betting on the fight.

I was rewarded.

Reyes KOed Weidman in the second round.

But let's make sure I didn't just get lucky.

## Performance Since Initial Modeling and Decision Boundary Tuning

Since the intitial model was created - 123 fights have occured and it is performing at an accuracy of _____

Decision boundary was adjusted like so:



Time to make some moolah.

## Next Steps

Perfomance wise, I definitely like to increase the accuracy.  Potentially by adding in additional information to the dataset it can become a better predictor.

Style wise, I would like to make a user friendly interface to easy use of the system.





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
