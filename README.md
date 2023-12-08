# Loan Management System

Loan Management System is a web application built on Django
framework that allows users to apply for loans, manage contracts,
and browse products and manufacturers.

## Installation

### Pre-requisites

To install Loan Management System make sure that you already have
Docker and Docker Compose installed on your local machine.
Check out docker documentation to install:
- Docker: https://docs.docker.com/engine/install/
- Docker Compose: https://docs.docker.com/compose/install/

### Clone the repository to your local machine

`git clone https://github.com/AndrewYatskevich/loan-management-system.git`

### Move to the root folder of the project

`cd loan-management-system/`

### Create the .env file and fill it out

- Create the .env file `touch .env`
- Fill out the .env file by referring to .env.example

### Run Docker Compose to spin up the application

`docker compose up -d`

## Usage

The application is available on 0.0.0.0:8000 host.
The following functionality has been implemented:
- Endpoint to fetch unique manufacturers ids by contract id

## License
MIT © [Andrew Yatskevich](https://github.com/AndrewYatskevich)
