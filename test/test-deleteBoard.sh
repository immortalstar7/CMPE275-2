#!/bin/bash
#------------------Dhrumit Sheth------------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" -DELETE  http://localhost:8082/v1/deleteBoard/37df3b490a760f3b81eabe7d09001640/300
echo -e "\n"
