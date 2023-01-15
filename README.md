# Bank Payment Microservices

REST API Bank Payment

This is an API to do a simple bank transaction including create bank account, deposit, withdraw and check balance

The entire application is build with python programming language and django with Django Rest Framework

## Requirements
To run this api server, docker need to be installed first:
### Docker:
  #### Linux Ubuntu
      read installation docs below
      https://docs.docker.com/engine/install/ubuntu/

  #### Mac Os
      to install docker on mac, visit docker link below
      https://docs.docker.com/desktop/install/mac-install/

  #### Windows
      to install docker on Windows visit docker link below
      https://docs.docker.com/desktop/install/windows-install/
      
## How to run:
to run this docker required to be installed

     docker compose up

## REST API
### Create Bank Account

`POST /api/account/`
     curl -i -H 'Accept: application/json' -X POST http://localhost:8000/api/account/
#### Request Body
      {
        "name": "My Account",
        "deposit_amount": 5000.0,
        "phone_number": "0851999888",
        "tax_id": "999888",
        "email_address": "account@email.com",
        "address": "My Street"
      }
#### Response
      {
        "total_balance": 5000.0,
        "deposit_amount": 5000.0,
        "account_number": "085329928888105610",
        "name": "My Name",
        "phone_number": "085329928888",
        "tax_id": "105610",
        "email_address": "email@email.com",
        "address": "my address"
      }
      
### Get Account Balance

`POST /api/account/balance`
     curl -i -H 'Accept: application/json' -X POST http://localhost:8000/api/account/balance
#### Request Body
      {
        "user_id": "c16365f9-c8e7-4bee-aa9b-0f47682241f5" 
      }
#### Response
      {
        "total balance": 9999.0,
        "name": "My Name",
        "email": "email@gmail.com",
        "address": "my address",
        "phone_number": "08532323232"
      }
      
### Withdraw

`POST /api/transaction/`
     curl -i -H 'Accept: application/json' -X POST http://localhost:8000/api/transaction/
#### Request Body
      {
        "user_id": "c16365f9-c8e7-4bee-aa9b-0f47682241f5",
        "transaction_type": "withdraw",
        "transaction_amount": 800
      }
#### Response
      {
        "status_code": 200,
        "previous_balance": 69988.79999999997,
        "user_id": "c16365f9-c8e7-4bee-aa9b-0f47682241f5",
        "account_number": "08976363632",
        "name": "My Name",
        "total_balance": 69178.79999999997,
        "transaction_type": "withdraw",
        "transaction_amount": 800
      }

### Deposit

`POST /api/transaction/`
     curl -i -H 'Accept: application/json' -X POST http://localhost:8000/api/transaction/
#### Request Body
      {
        "user_id": "b7a190e1-c696-447f-a502-2ccc346debaa",
        "transaction_type": "deposit",
        "transaction_amount": 2000.2
      }
#### Response
      {
        "status_code": 200,
        "previous_balance": 69988.79999999997,
        "user_id": "c16365f9-c8e7-4bee-aa9b-0f47682241f5",
        "account_number": "087626236356",
        "name": "My Name",
        "total_balance": 69178.79999999997,
        "transaction_type": "withdraw",
        "transaction_amount": 800
      }
