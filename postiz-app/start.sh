#!/bin/bash
# Postiz App Startup Script
# Starts PostgreSQL, Redis, Temporal, and all Postiz services

set -e

export PATH="$PATH:/root/.temporalio/bin"

echo "=== Starting Postiz App ==="

# Start PostgreSQL if not running
if ! pg_isready -q 2>/dev/null; then
    echo "Starting PostgreSQL..."
    pg_ctlcluster 16 main start
fi

# Start Redis if not running
if ! redis-cli ping > /dev/null 2>&1; then
    echo "Starting Redis..."
    redis-server --daemonize yes
fi

# Start Temporal dev server if not running
if ! curl -s http://localhost:7233 > /dev/null 2>&1; then
    echo "Starting Temporal..."
    nohup temporal server start-dev --port 7233 --ui-port 8233 --db-filename /tmp/temporal.db > /tmp/temporal.log 2>&1 &
    sleep 3
fi

echo "PostgreSQL: $(pg_isready)"
echo "Redis: $(redis-cli ping)"
echo "Temporal: running on port 7233"

cd /home/user/petfactory-morocco/postiz-app/source

echo ""
echo "Starting Postiz services..."
echo "  Frontend:    http://localhost:4200"
echo "  Backend API: http://localhost:3000"
echo "  Temporal UI: http://localhost:8233"
echo ""

# Run in production mode
pnpm run pm2-run
