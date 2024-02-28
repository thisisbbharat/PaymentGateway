# Use the official Node.js image as a base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock) into the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend code into the container
COPY . .

# Build the frontend code
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Command to run the frontend server
CMD ["npm", "start"]
