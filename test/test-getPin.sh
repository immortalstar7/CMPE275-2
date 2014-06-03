#!/bin/bash
#----------------Kavish Parikh----------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" -GET  http://localhost:8082/v1/pins/37df3b490a760f3b81eabe7d09001580
echo -e "\n"