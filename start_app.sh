#!/bin/bash

# Create data directory if it doesn't exist
mkdir -p app/data

# Check if dependencies are installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it and try again."
    exit 1
fi

# Install dependencies (uncomment if you want to run this every time)
# python3 -m pip install -r requirements.txt

# Kill any existing uvicorn processes
pkill -f "uvicorn app.main:app" || true

# Start the FastAPI server
echo "Starting EasyBet API server..."
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Store the process ID
PID=$!
echo $PID > .app_pid
echo "Server started with PID: $PID"
echo "You can access the API at http://localhost:8000"
echo "API documentation is available at http://localhost:8000/docs" 