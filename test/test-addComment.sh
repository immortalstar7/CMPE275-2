#!/bin/bash
#----------------Kavish Parikh----------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --data "comment=I love travelling"  http://localhost:8082/v1/37df3b490a760f3b81eabe7d09001640/boards/100/pins/9e660b3c4b28e2c174736b0621001d89/comment
echo -e "\n"
