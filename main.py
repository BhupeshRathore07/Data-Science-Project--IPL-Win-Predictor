import streamlit as st
import pickle
import pandas as pd

st.set_page_config(layout="wide")

st.title('IPL 2022 Win Predictor')
teams = [
    'Chennai Super Kings',
    'Delhi Capitals',
    'Royal Challengers Bangalore',
    'Mumbai Indians',
    'Kolkata Knight Riders',
    'Rajasthan Royals',
    'Sunrisers Hyderabad',
    'Punjab Kings',
    'Gujarat Titans',
    'Lucknow Super Giants']

cities = ['Mumbai', 'Johannesburg', 'Hyderabad', 'Chennai', 'Abu Dhabi',
       'Chandigarh', 'Lucknow', 'Centurion', 'Delhi', 'Durban',
       'Bengaluru', 'Ahemdabad', 'Kolkata', 'Ahmedabad', 'Jaipur',
       'Port Elizabeth', 'East London', 'Sharjah', 'Dubai', 'Cape Town',
       'Bloemfontein', 'Kimberley']


pipe = pickle.load(open('pipe.pkl', 'rb'))

col1, col2, col3 = st.columns(3)

with col1:
    battingTeam = st.selectbox("Select the Batting Team", sorted(teams))
with col2:
    bowlingTeam = st.selectbox("Select the Bowling Team", sorted(teams))
with col3:
    citySelected = st.selectbox("Select the City", sorted(cities))

col1, col2, col3, col4 = st.columns(4)

with col1:
    target = st.number_input("Target")
with col2:
    score = st.number_input("Current Score")
with col3:
    overs = st.number_input("Overs Completed")
with col4:
    wickets = st.number_input("Wickets Fallen")


if st.button("Predict Probability"):
    runsLeft = target - score
    ballsLeft = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runsLeft*6)/ballsLeft
    input_df = pd.DataFrame({'BattingTeam':[battingTeam], 'BowlingTeam':[bowlingTeam],'City':[citySelected],
                             'runs_left':[runsLeft],'balls_left':[ballsLeft],
                             'wickets_left':[wickets],'total_run_x':[target],'crr':[crr], 'rrr':[rrr]})
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    st.subheader(battingTeam + "- " + str(round(win*100)) + "%")
    st.subheader(bowlingTeam + "- " + str(round(loss*100)) + "%")