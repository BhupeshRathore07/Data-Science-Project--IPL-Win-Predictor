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

Here is the head of required data for modelling from matches csv file:

### Ball-by-ball Data Set
Here is the head of raw data of ball-by-ball details:

Here is the head of required data for modelling from ball-by-ball csv file:

### Final Data Set
Here is the final data set after concatenating both tables using their unique match ID.

## Modelling

Once we extracted the exact data it is very easy to model the predictor using sklearn.

Steps followed here:
1. splitting data into train and test data set using model_selection in sklearn
2. converting it into 2d list using OneHotEncoder
3. now using logistic regression for prediction and getting results in probabilities
4. converging it into pipeline with step 1 as OneHotEncoder and step 2 as logistic regression.

Here, accuracy is also checked and compared Random Forest Classifier. Even though Random Forest Classifier produces much better accuracy compared to Logistic Regression but aren’t prefered in predictor models considering the fact that they produce stiff probabilities which is not much of a help. Thus, in this predictor, Logistic regression > Random forest classifier.

## Uploading using Streamlit and Heroku

Now, once model is ready it’s time to deploy the project using streamlit and Heroku.

Steps followed here are:
1. Converting pipeline into pickle.
2. using pickle and data set in creating streamlit website
3. converting results probabilities into percentage using the inputted data

## Conclusion
Link for the webiste: https://bhupesh-ipl-win-predictor.herokuapp.com/
