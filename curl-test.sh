#!/bin/bash

BASE_URL="http://localhost:5000"

echo "=== Testing Timeline Post APIs ==="
echo

# Test POST /api/timeline_post
echo "1. Testing POST /api/timeline_post"
echo "Creating a new timeline post..."
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "content": "This is a test timeline post!"
  }' \
  "$BASE_URL/api/timeline_post"

echo
echo

# Test GET /api/timeline_post
echo "2. Testing GET /api/timeline_post"
echo "Retrieving all timeline posts..."
curl -X GET \
  -H "Content-Type: application/json" \
  "$BASE_URL/api/timeline_post"

echo
echo
echo "=== Tests completed ==="
