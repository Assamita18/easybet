import typer
import requests
import json
from tabulate import tabulate
from datetime import datetime
from typing import Optional

app = typer.Typer()
API_BASE_URL = "http://localhost:8000"

@app.command()
def register(username: str):
    """Register a new user"""
    response = requests.post(
        f"{API_BASE_URL}/users/",
        json={"username": username}
    )
    if response.status_code == 200:
        user = response.json()
        print(f"User registered with ID: {user['id']}")
        print(f"Initial balance: ${user['balance']}")
    else:
        print(f"Error: {response.json()['detail']}")

@app.command()
def show_user(username: str):
    """Show user details"""
    response = requests.get(f"{API_BASE_URL}/users/by-username/{username}")
    if response.status_code == 200:
        user = response.json()
        print(f"User ID: {user['id']}")
        print(f"Username: {user['username']}")
        print(f"Balance: ${user['balance']}")
    else:
        print(f"Error: {response.json()['detail']}")

@app.command()
def list_events(status: Optional[str] = None):
    """List all events or filter by status (upcoming, live, completed)"""
    url = f"{API_BASE_URL}/events/"
    if status:
        url += f"?status={status}"
    
    response = requests.get(url)
    if response.status_code == 200:
        events = response.json()
        if not events:
            print("No events found.")
            return
        
        table_data = []
        for event in events:
            start_time = datetime.fromisoformat(event['start_time'].replace('Z', '+00:00'))
            table_data.append([
                event['id'],
                event['name'],
                event['game'],
                f"{event['team_a']} vs {event['team_b']}",
                f"{event['odds_a']} / {event['odds_b']}",
                start_time.strftime('%Y-%m-%d %H:%M'),
                event['status'],
                event['winner'] if event['winner'] else 'N/A'
            ])
        
        headers = ["ID", "Name", "Game", "Teams", "Odds (A/B)", "Start Time", "Status", "Winner"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print(f"Error: {response.json()['detail']}")

@app.command()
def create_event(
    name: str, 
    game: str, 
    team_a: str, 
    team_b: str, 
    odds_a: float, 
    odds_b: float, 
    start_time: str
):
    """Create a new event (start_time format: YYYY-MM-DD HH:MM)"""
    # Convert start_time to ISO format
    try:
        dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        iso_time = dt.isoformat()
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD HH:MM")
        return
    
    response = requests.post(
        f"{API_BASE_URL}/events/",
        json={
            "name": name,
            "game": game,
            "team_a": team_a,
            "team_b": team_b,
            "odds_a": odds_a,
            "odds_b": odds_b,
            "start_time": iso_time
        }
    )
    
    if response.status_code == 200:
        event = response.json()
        print(f"Event created with ID: {event['id']}")
    else:
        print(f"Error: {response.json()['detail']}")

@app.command()
def place_bet(user_id: int, event_id: int, amount: float, team: str):
    """Place a bet (team must be 'team_a' or 'team_b')"""
    if team not in ["team_a", "team_b"]:
        print("Error: Team must be 'team_a' or 'team_b'")
        return
    
    response = requests.post(
        f"{API_BASE_URL}/bets/?user_id={user_id}",
        json={
            "event_id": event_id,
            "amount": amount,
            "team": team
        }
    )
    
    if response.status_code == 200:
        bet = response.json()
        print(f"Bet placed with ID: {bet['id']}")
        print(f"Potential payout: ${bet['potential_payout']}")
    else:
        print(f"Error: {response.json()['detail']}")

@app.command()
def complete_event(event_id: int, winner: str):
    """Complete an event and set the winner (team_a, team_b, or draw)"""
    if winner not in ["team_a", "team_b", "draw"]:
        print("Error: Winner must be 'team_a', 'team_b', or 'draw'")
        return
    
    response = requests.put(
        f"{API_BASE_URL}/events/{event_id}/complete?winner={winner}"
    )
    
    if response.status_code == 200:
        print(f"Event {event_id} completed with winner: {winner}")
        
        # Settle bets for this event
        settle_response = requests.post(f"{API_BASE_URL}/events/{event_id}/settle")
        if settle_response.status_code == 200:
            settle_result = settle_response.json()
            print(settle_result["message"])
    else:
        print(f"Error: {response.json()['detail']}")

@app.command()
def show_user_bets(user_id: int, status: Optional[str] = None):
    """Show bets for a user, optionally filtered by status (pending, won, lost)"""
    url = f"{API_BASE_URL}/bets/user/{user_id}"
    if status:
        url += f"?status={status}"
    
    response = requests.get(url)
    if response.status_code == 200:
        bets = response.json()
        if not bets:
            print("No bets found.")
            return
        
        table_data = []
        for bet in bets:
            placed_at = datetime.fromisoformat(bet['placed_at'].replace('Z', '+00:00'))
            table_data.append([
                bet['id'],
                bet['event_id'],
                bet['team'],
                f"${bet['amount']}",
                bet['odds'],
                f"${bet['potential_payout']}",
                placed_at.strftime('%Y-%m-%d %H:%M'),
                bet['status']
            ])
        
        headers = ["ID", "Event ID", "Team", "Amount", "Odds", "Potential Payout", "Placed At", "Status"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print(f"Error: {response.json()['detail']}")

if __name__ == "__main__":
    app() 