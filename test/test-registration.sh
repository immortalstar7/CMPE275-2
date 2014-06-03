#!/bin/bash
#-----------------Manushi Doshi---------------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --data "name='name'&value='bar'"  http://localhost:8082/moo/data
echo -e "\n"
