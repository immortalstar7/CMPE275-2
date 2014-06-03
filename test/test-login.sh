#!/bin/bash
#-----------------Manushi Doshi---------------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --data "username=rshah&password=rshah123"  http://localhost:8082/v1/login
echo -e "\n"
