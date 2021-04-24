# FastAPI Experiments


## Setup dev

```bash
$ docker build -t fastapi-nlp-bert:latest -f Dockerfile.dev .

$ docker run -it -p 5000:5000 --name fastapi-nlp-bert -v C:/Users/YIsaienkov/Documents/fastapi-experiments/:/app/ --rm fastapi-nlp-bert /bin/bash
```

## Setup prod

```bash
$ docker build -t fastapi-nlp-bert:latest -f Dockerfile .

$ docker run -p 5000:5000 -e PORT=5000 fastapi-nlp-bert:latest
```

