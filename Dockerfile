version: "3.8"

services:
  client_jenkins:
    container_name: client_jenkins
    build: ./client
    ports:
      - "3001:3000"
    environment:
      - REACT_APP_YOUR_HOSTNAME=http://localhost:5001
    depends_on:
      - server_jenkins

  server_jenkins:
    container_name: server_jenkins
    build: ./server
    ports:
      - "5001:5000"
    env_file:
      - ./server/.env
