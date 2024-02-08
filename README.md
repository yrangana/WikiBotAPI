[![Python application test with Github Actions](https://github.com/yrangana/WikiBotAPI/actions/workflows/main.yml/badge.svg)](https://github.com/yrangana/WikiBotAPI/actions/workflows/main.yml)

# WikiBotAPI
WikiBotAPI is an application programming interface used to interact with Wikipedia articles. The API provides a command line interface to search for articles and retrieve the content from articles based on the search query.
The API also provides a RESTful web service.
The WikiBotAPI is containerized using Docker and tested on AWS App Runner.

## Clone the repository
```bash
git clone https://github.com/yrangana/WikiBotAPI.git
```

## Install dependencies
```bash
make install
```

## Run test cases
```bash
make test
```

## Test using command line interface
```bash
python fire-cli.py --query "Sri Lanka" --length 2
```

## Run the application on local
```bash
python main.py
```

## Create docker image
```bash
Docker build -t wikibotapi .
```

## Run the application
```bash
Docker run -p 8081:8081 wikibotapi
```

## invoke test script
```bash
invoke.sh
```

## RESTful web service
```bash
curl -X 'POST' \
  'http://0.0.0.0:8081/wikipedia_summary' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Sri Lanka",
  "sentences": 1
}'
```

## License
[MIT](https://github.com/yrangana/WikiBotAPI/blob/main/LICENSE)

