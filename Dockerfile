# Using an official python base image: https://hub.docker.com/_/python

# STEP 1. Install an optimized for python base iamge
FROM python:3.9-slim-bookworm

# STEP 2. Copy the source code (from Code) into the container /app
ADD Code /app

# STEP 3. Set working directory to /app so we can execute commands in it
WORKDIR /app

# STEP 4. Install required dependencies
RUN pip install -r requirements.txt

# STEP 5. Decclare env variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# STEP 6. Expore the port that Flask is running on
EXPOSE 5000

# STEP 7: Run Flask!
CMD ["flask", "run", "--host=0.0.0.0"]
