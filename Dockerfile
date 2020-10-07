FROM python:3

# Send Python output straight to the terminal
ENV PYTHONUNBUFFERED=1

# Create our application directory
RUN mkdir /code
WORKDIR /code

# Install requirements
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the application code
COPY . /code/
