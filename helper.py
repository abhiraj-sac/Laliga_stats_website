import streamlit
# import streamlit as st
import matplotlib.pyplot as plt


def attendance(new_df):
    grouped = new_df.groupby(['team', 'opponent', 'attendance'])
    result = grouped.sum('attendance')
    # result.to_dict()
    gp = new_df.groupby(['opponent', 'team'])['attendance'].sum()
    gp
    # gp.to_dict()
    maximum = max(gp.items(), key=lambda x: x[1])
    one, two = maximum
    minimum = min(gp.items(), key=lambda x: x[1])
    three, four = minimum
    streamlit.write(f"Maximum crowd is pulled by {one[0]} and {one[1]} match and the total attendance is {two}")
    streamlit.write(f"Minimum crows is pulled by {three[0]} and {three[1]} match and the total  attendance is {four}")


def refrees(new_df):
    ref = new_df['referee'].value_counts().to_dict()
    for i, j in ref.items():
        if j >= 250:
            streamlit.write(f"Whistle Master: Mr.{i} Referee Commands the Field in {j} Matches!")
            streamlit.write(j)
        elif j < 250 and j > 100:
            streamlit.write(f"Mr.{i} Referee Commands the Field in {j} Matches!")
            streamlit.write(j)


def clubsreport(new_df, selected):
    values = new_df[new_df['team'] == selected]['result'].value_counts().to_dict()
    # values['W']
    streamlit.header(f"The {selected} has recorded {values['W']} won, {values['L']} loss  and  {values['D']} draws")

    maximum_attendeance = int(new_df[new_df['team'] == selected]['attendance'].max())
    # maximum_attendeance.astype("int32")
    streamlit.header(f"Maximum crowd pulled is {maximum_attendeance}")

    average_crowd = int(new_df[new_df['team'] == selected]['attendance'].mean())
    streamlit.header(f"{selected} pulls mean crowd  which is around {average_crowd}")

    captain = new_df[new_df['team'] == selected]['captain'].mode()[0]
    streamlit.header(f"The player who served as captain for his team the most times is {captain}")

    barcelona_results = new_df[(new_df['team'] == selected) & (new_df['result'] == 'W')]
    opponent_wins_count = barcelona_results.groupby('opponent')['result'].count()
    team_results = opponent_wins_count.to_dict()
    max_team = max(team_results.items(), key=lambda x: x[1])
    max_team_name, max_team_value = max_team
    streamlit.write(f"Team which {selected} has beaten most number of time is ", max_team_name)
    streamlit.write(f"Number of time {selected} beaten {max_team_name} is", max_team_value)

    new_df = new_df[new_df['poss'] < 99]
    possession = int(new_df[new_df['team'] == selected]['poss'].mean())
    streamlit.write(f"The average possession of the {selected} is {possession}.")


def onevsone(new_df, your_team, opponent, year):
    df = new_df[(new_df['team'] == your_team) & (new_df['opponent'] == opponent) & (new_df['year'] == year)]
    m = df['poss'].mean()
    data = list(df['poss'])
    val = df['result'].value_counts()
    streamlit.write(val)

    dfs = df[df['poss'] < 99]
    m = dfs['poss'].mean()
    streamlit.write(f"average poss is {m}")

    # streamlit.write(f"{your_team} has won {val[0]} and lost {val[1]} against {opponent}")
    # streamlit.write(f"{your_team} has a possession around {m} against {opponent}")
    # att = df['attendance'].mean()
    # print(f"Mean attendance of crowd is {att}")
    # ref = df['referee'].to_list()
    # print("Match refrees are")
    # for i in ref:
    #     print(i)
    # print(ref)


def graphics(new_df):
    streamlit.subheader("Identify the premier team with the highest number of victories.")



    # Filter the DataFrame for rows where the result is 'W' (win)
    wins_df = new_df[new_df['result'] == 'W']

    # Group by team and count the number of wins for each team
    win_counts = wins_df['team'].value_counts()

    # Select the top 10 teams with the most wins
    top_10_teams = win_counts.head(10)

    # Plot a pie chart for the top 10 teams
    fig, ax = plt.subplots()
    ax.pie(top_10_teams, labels=top_10_teams.index, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Display the pie chart using Streamlit
    streamlit.pyplot(fig)


    streamlit.subheader("Determine the Laliga team exhibiting superior possession statistics, reflecting a strategic advantage and adept gameplay.")
    results = new_df.groupby('team')['poss'].mean()
    sorted_results = results.sort_values(ascending=False)
    # sorted_results.plot(kind='bar')
    streamlit.bar_chart(sorted_results)

    streamlit.subheader("Unveil the captain who reigns supreme in victories")
    results = new_df[new_df['result'] == 'W'].groupby('captain').count()
    sorted_results = results['result'].sort_values(ascending=False)
    top_20_results = sorted_results.head(20)
    streamlit.bar_chart(top_20_results)
