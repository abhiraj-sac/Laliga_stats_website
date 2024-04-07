import streamlit as st
import pandas as pd
import helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
# import streamlit as st
from PIL import Image

# Load image



new_df = pd.read_csv('filters.csv')
fil = pd.read_csv('filtereddata.csv')
# st.header('hello bhai')
st.sidebar.header("Laliga Stats")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('numerical scrutiny', 'Clubs Stats', 'One vs One Stats','Graphics oasis')
)

# st.dataframe(df)

if user_menu == 'numerical scrutiny':
    image = Image.open('messi01.jpg')

    # Display image
    # st.image(image, caption='Que sera sera', use_column_width=True)
    st.image(image, caption='Que sera sera',
             use_column_width=True,  # Fit image to column width
             output_format='auto',  # Automatically choose optimal format
             width=None,  # Set width (in pixels) if needed
             clamp=False,  # Do not clip image size
             channels='RGB',  # Set color channels  # Set output image format
             )
    st.header("Most Buzzy Months")
    monthly_attendance = new_df.groupby('month')['attendance'].sum()
    att = monthly_attendance.sort_values()
    monthly_attendance_dict = att.to_dict()
    monthly_attendance = new_df.groupby('month')['attendance'].sum()
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    # Loop through the monthly_attendance_dict items and display month names
    for month, attendance in monthly_attendance_dict.items():
        month_name = month_names.get(month, "Unknown")
        st.write(f" {month_name}    holds      Attendance: {attendance}")
    st.header("How's the Fame Game? Find Out Which Teams Are Stealing the Spotlight!")
    helper.attendance(new_df)
    st.header("Calling the Shots: Discover Which Referee Has Ruled the Field and for How Long!")
    helper.refrees(fil)

if user_menu == 'Clubs Stats':
    imaget = Image.open('messsiii.jpg')

    # Display image
    st.image(imaget, caption='Que sera sera', use_column_width=True)

    clublist = new_df['team'].dropna().unique().tolist()
    clublist.sort()
    # clublist
    selected = st.sidebar.selectbox("Clubs", clublist)
    values = new_df[new_df['team'] == selected]['result'].value_counts().to_dict()
    # values['W']
    # st.header(f"The {selected} has recorded {values['W']} won, {values['L']} loass  and  {values['D']} draws")
    helper.clubsreport(new_df, selected)

if user_menu == 'One vs One Stats':

    clublist = new_df['team'].dropna().unique().tolist()
    home_team = st.sidebar.selectbox("HomeTeam", clublist)
    away_team = st.sidebar.selectbox("AwayTeam", clublist)
    df = fil[(fil['team'] == home_team) & (fil['opponent'] == away_team)]
    st.header(f"Home team is {home_team} and Away team is  {away_team}")

    df = fil[(fil['team'] == home_team) & (fil['opponent'] == away_team)]
    dfs = df[df['poss'] < 99]
    m = dfs['poss'].mean()
    if not df.empty:
        m=int(dfs['poss'].mean())

    data = list(df['poss'])
    val = df['result'].value_counts()
    st.write(val)
    # st.write(f"{home_team} has won {val[0]} and lost {val[1]} against {away_team}")
    st.subheader(f"{home_team} has a possession around {m} against {away_team}")
    att = df['attendance'].mean()
    st.subheader(f"Mean attendance of crowd is {att}")
    ref = df['referee'].to_list()
    st.subheader("The Unparalleled Referee: Who Commanded the Field the Most in This Match?")
    list =[]
    c=0
    for i in ref:
        if c ==4:
            break
        st.write(i)
        c=c+1














    # # Create a selectbox for selecting a year
    # selected_year = st.selectbox('Select a year')
    #
    # # Print the selected year
    # st.write('You selected:', selected_year)
    # # helper.onevsone(fil,home_team,away_team,selected_year)
    #
    # dfs = fil[fil['poss'] < 99]
    # m = dfs['poss'].mean()
    # st.write(f"average poss is {m}")
    # #
    # data = list(new_df['poss'])
    # val = df['result'].value_counts()
    # # st.write(f"{home_team} has won {val[0]} and lost {val[1]} against {away_team}")
    # # st.write(f"{home_team} has a possession around {m} against {away_team}")
    # att = df['attendance'].mean()
    # st.header(f"Mean attendance of crowd is {att}")
    # ref = df['referee'].to_list()
    # st.header("Match refrees are")
if user_menu == 'Graphics oasis':
    helper.graphics(fil)


