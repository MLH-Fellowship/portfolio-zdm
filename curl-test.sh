#!/bin/bash

RANDOM_NUM=$((RANDOM))
TEST_NAME="test User $RANDOM_NUM"
TEST_EMAIL="testuser$RANDOM_NUM@test.com"
TEST_CONTENT="test"

curl -X POST http://localhost:5000/api/timeline_post -d "name=$TEST_NAME&email=$TEST_EMAIL&content=$TEST_CONTENT"

curl "http://localhost:5000/api/timeline_post"