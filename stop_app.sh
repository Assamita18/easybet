#!/bin/bash

# Check if PID file exists
if [ -f .app_pid ]; then
    PID=$(cat .app_pid)
    echo "Found PID file with process ID: $PID"
    
    # Check if process is running
    if ps -p $PID > /dev/null; then
        echo "Stopping EasyBet server with PID: $PID"
        kill $PID
        rm .app_pid
        echo "Server stopped successfully."
    else
        echo "Process with PID $PID is not running."
        rm .app_pid
        echo "Removed stale PID file."
    fi
else
    # Try to find and kill any uvicorn processes related to the app
    echo "No PID file found. Attempting to find and stop uvicorn processes..."
    pkill -f "uvicorn app.main:app" && echo "Found and stopped uvicorn processes." || echo "No running uvicorn processes found."
fi

# Final check for any remaining processes
if pgrep -f "uvicorn app.main:app" > /dev/null; then
    echo "WARNING: Some processes might still be running. Forcing termination..."
    pkill -9 -f "uvicorn app.main:app"
    echo "Forced termination complete."
fi

echo "EasyBet server has been stopped." 