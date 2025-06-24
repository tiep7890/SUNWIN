#!/bin/bash
echo "🚀 Installing dependencies..."
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install -r requirements.txt

echo "📂 Initializing bot database..."
python3 botv4.py &
sleep 5
pkill -f botv4.py

echo "🔥 Starting fake server and bot..."
nohup python3 sunwin_mock_server.py > server.log 2>&1 &
nohup python3 botv4.py > bot.log 2>&1 &
echo "✅ All services started successfully!"