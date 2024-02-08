curl -X 'POST' \
  'http://0.0.0.0:8081/wikipedia_summary' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Sri Lanka",
  "sentences": 1
}'