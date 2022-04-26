# IPL-Win-Predictor
Over the period of decade, the craze of cricket and IPL in India has exponentially increased. As a Data science enthusiast, working on data of IPL is always fun.
Today I’m creating end-to-end project, where after submitting the target score with some required fields, the model predicts the chance for batting team whether they will achieve the target or not and the output is shown in percentage after calculating the probabilities using Logistic Regression.

## Data Set

Data is obtained from Kaggle as IPL Data Set, 2008 - 2021. Link for the Data set is : https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset .
This data set contains two csv (‘comma separated values’) files, where one file gives the details for every match played in IPL with details like winning team, loosing team, venue, toss, total runs scored, date, league stage, and even more. While other csv file gives ball-by-ball details of each and every match where, columns like innings, ball_number, total_run, etc. are useful.

## Preprocessing the data
After collecting the data it is necessary to preprocess the data as per the model requirement. Here in preprocessing, we removes null values, converting few columns into binary (0’s and 1's), and extracting the required only columns for modelling.

### Matches Data Set

Here is the head of raw data of matches played:

![Every match data set](https://miro.medium.com/max/1400/1*yKyuQMBGJJCE0xWeaGyWOQ.jpeg)

Here is the head of required data for modelling from matches csv file:

![Required Columns from Match Data set and creating new MatchDF](https://miro.medium.com/max/1400/1*tuSkRNDAKdfGf1QeDYQzNQ.jpeg)

### Ball-by-ball Data Set
Here is the head of raw data of ball-by-ball details:

![Raw data from Ball-by-ball data set](https://miro.medium.com/max/1400/1*V7kJkGW94jOHGydhIvw30A.jpeg)


### Final Data Set
Here is the final data set after concatenating both tables using their unique match ID.

Final DataFrame with new cols as crr, nrr, balls_left, wicket_left, runs_left

![Final DataFrame with new cols as crr, nrr, balls_left, wicket_left, runs_left](https://miro.medium.com/max/1400/1*1EsliaQiPXDoCiH3mhvOyQ.jpeg)

## Modelling

Once we extracted the exact data it is very easy to model the predictor using sklearn.

Steps followed here:
* splitting data into train and test data set using model_selection in sklearn
* converting it into 2d list using OneHotEncoder
* now using logistic regression for prediction and getting results in probabilities
* converging it into pipeline with step 1 as OneHotEncoder and step 2 as logistic regression.

Here, accuracy is also checked and compared Random Forest Classifier. Even though Random Forest Classifier produces much better accuracy compared to Logistic Regression but aren’t prefered in predictor models considering the fact that they produce stiff probabilities which is not much of a help. Thus, in this predictor, Logistic regression > Random forest classifier.

## Uploading using Streamlit and Heroku

Now, once model is ready it’s time to deploy the project using streamlit and Heroku.

Steps followed here are:
* Converting pipeline into pickle.
* using pickle and data set in creating streamlit website
* inputted taken are batting team, bowling team, venue, stadium, target, current score, wickets fallen, overs done.
* converting results probabilities into percentage using the inputted data.

Here is the final output of website published:

![final output](https://miro.medium.com/max/1400/1*V7kJkGW94jOHGydhIvw30A.jpeg)

## Conclusion
Here concluding this project, I had gone through lot data processing techniques which are equally important as modelling.

Here is the link for the website: https://bhupesh-ipl-win-predictor.herokuapp.com/
