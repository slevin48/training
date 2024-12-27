import streamlit as st
import pandas as pd
from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import leaguegamefinder, playergamelog

# App title and layout
st.set_page_config(page_title="NBA Stats App", page_icon="🏀", layout="wide")
st.title("Basketboule 🏀")
st.sidebar.title("Explore NBA Stats")

menu = st.sidebar.selectbox("Menu", ["Home", "Teams", "Players", "Games"])

if menu == "Home":
    st.header("Welcome to Basketboule")
    st.write("Explore NBA teams, players, and game data in one place.")

if menu == "Teams":
    st.header("NBA Teams")
    
    # Get team data
    nba_teams = teams.get_teams()
    team_names = [team['full_name'] for team in nba_teams]
    
    # Dropdown to select a team
    selected_team = st.selectbox("Select a Team", team_names)
    team_data = next(team for team in nba_teams if team['full_name'] == selected_team)
    
    # Display team information
    st.subheader(f"{team_data['full_name']}")
    st.write(f"Team ID: {team_data['id']}")
    st.write(f"Abbreviation: {team_data['abbreviation']}")
    st.write(f"City: {team_data['city']}")

if menu == "Games":
    st.header("NBA Games")
    
    # Select team to filter games
    team_names = [team['full_name'] for team in teams.get_teams()]
    selected_team = st.selectbox("Select a Team", team_names)
    team_id = next(team['id'] for team in teams.get_teams() if team['full_name'] == selected_team)
    
    # Retrieve game data
    game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = game_finder.get_data_frames()[0]
    
    # Display games
    st.dataframe(games[['GAME_DATE', 'MATCHUP', 'WL', 'PTS', 'REB', 'AST']])

if menu == "Players":
    st.header("NBA Players")
    
    # Search for a player by name
    player_name = st.text_input("Enter Player Name")
    if player_name:
        nba_players = players.get_players()
        player = next((p for p in nba_players if player_name.lower() in p['full_name'].lower()), None)
        
        if player:
            st.subheader(f"Player: {player['full_name']}")
            st.write(f"Player ID: {player['id']}")
            st.write(f"Team: {player.get('team', 'N/A')}")
            
            # Get game log
            player_log = playergamelog.PlayerGameLog(player_id=player['id'])
            games = player_log.get_data_frames()[0]
            
            # Display recent game performance
            st.write("Last Game Performance")
            st.dataframe(games[['GAME_DATE', 'MATCHUP', 'PTS', 'REB', 'AST', 'STL', 'BLK']].head(1))
            
        else:
            st.warning("Player not found. Try again.")
