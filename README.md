# EasyBet - E-Sports Betting System

A simple betting system for e-sports events with a command-line interface and REST API.

## Features

- Create and manage user accounts
- View and create e-sports events
- Place bets on events
- Automatic bet settlement when events complete
- Command-line interface for easy interaction
- REST API for integration with other systems

## Tech Stack

- Python 3.8+
- FastAPI for API endpoints
- SQLite for database
- SQLAlchemy for ORM
- Typer for command-line interface
- Tabulate for CLI table display

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/easybet.git
cd easybet
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

### Start the API server

```
python -m app.main
```

The API server will start at http://localhost:8000. You can access the interactive API documentation at http://localhost:8000/docs.

### Using the Startup and Shutdown Scripts

For convenience, you can use the provided shell scripts to start and stop the application:

#### Starting the application
```
./start_app.sh
```
This script will:
- Create the necessary data directory
- Check for Python installation
- Stop any existing server instances
- Start the FastAPI server
- Store the process ID for later use

#### Stopping the application
```
./stop_app.sh
```
This script will:
- Stop the server gracefully using the saved process ID
- Fall back to finding and stopping all relevant uvicorn processes
- Perform a final check to ensure all processes are terminated

### CLI Commands

The system provides a command-line interface for common operations:

#### User Management

- Register a new user:
```
python cli.py register USERNAME
```

- Show user details:
```
python cli.py show-user USERNAME
```

#### Event Management

- List all events:
```
python cli.py list-events
```

- List events by status:
```
python cli.py list-events --status=upcoming
```

- Create a new event:
```
python cli.py create-event "Tournament Finals" "League of Legends" "Team A" "Team B" 1.5 2.5 "2023-12-31 18:00"
```

- Complete an event:
```
python cli.py complete-event EVENT_ID team_a
```

#### Betting

- Place a bet:
```
python cli.py place-bet USER_ID EVENT_ID AMOUNT team_a
```

- Show user bets:
```
python cli.py show-user-bets USER_ID
```

- Show user bets by status:
```
python cli.py show-user-bets USER_ID --status=pending
```

## API Endpoints

The system provides the following API endpoints:

### Users
- `GET /users/` - List all users
- `POST /users/` - Create a new user
- `GET /users/{user_id}` - Get user details by ID
- `GET /users/by-username/{username}` - Get user details by username

### Events
- `GET /events/` - List all events
- `POST /events/` - Create a new event
- `GET /events/{event_id}` - Get event details
- `PUT /events/{event_id}` - Update event details
- `PUT /events/{event_id}/complete` - Complete an event with a winner

### Bets
- `POST /bets/` - Place a bet
- `GET /bets/user/{user_id}` - Get bets for a user
- `GET /bets/event/{event_id}` - Get bets for an event

### Settlement
- `POST /events/{event_id}/settle` - Settle all bets for an event

## Database Schema

The system uses SQLite with the following schema:

- **Users**: Store user information and balances
- **Events**: Store e-sports events information
- **Bets**: Store user bets on events 