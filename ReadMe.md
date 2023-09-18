# Run the tweet generator with Docker!

## 1. Build the image

`docker build -t tweet-generator-image .`

## 2. Run the container

`docker run -p 5001:5000 --rm --name tweet-generator-container tween-generator-image`

## 3. Access the tweet generator on your browser of choice

[http://localhost:5001](http://localhost:5001)
