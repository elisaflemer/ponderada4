# Use an official Node.js runtime as the parent image
FROM node:14
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install application dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Define the command to run your Node.js application
CMD ["npm", "run", "dev"]