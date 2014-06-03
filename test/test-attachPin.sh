#!/bin/bash
#------------------Rajvi Shah-------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --data "pin_id=37df3b490a760f3b81eabe7d090027d4"  http://localhost:8082/v1/user/37df3b490a760f3b81eabe7d09001640/board/100
echo -e "\n"
