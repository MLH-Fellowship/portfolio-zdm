#!/bin/bash

BASE_URL="http://localhost:5000"

RANDOM_NUM=$((RANDOM))
TEST_NAME="test User $RANDOM_NUM"
TEST_EMAIL="testuser$RANDOM_NUM@example.com"
TEST_CONTENT="test"

curl -X POST "$BASE_URL/api/timeline_post" \
  -d "name=$TEST_NAME" \
  -d "email=$TEST_EMAIL" \
  -d "content=$TEST_CONTENT" \

curl -s "$BASE_URL/api/timeline_post"