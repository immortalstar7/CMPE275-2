#!/bin/bash
#------------Darshit Kuwadia----------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" -GET  http://localhost:8082/v1/boards
echo -e "\n"
