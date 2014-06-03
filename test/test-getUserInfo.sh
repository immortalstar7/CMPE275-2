#!/bin/bash
#------------------Dhrumit Sheth------------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" -GET  http://localhost:8082/v1/user/ecdc815363c7dc543996f151490018bd
echo -e "\n"