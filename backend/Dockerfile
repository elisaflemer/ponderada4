FROM nikolaik/python-nodejs

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install application dependencies (Node.js)
RUN npm install

COPY requirements.txt /app/

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Define the command to build your Node.js application
# Replace with the actual build command from your package.json if needed
CMD ["npm", "run", "dev"]
