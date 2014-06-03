#!/bin/bash
#------------------Rajvi Shah-------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --data "pin_name=Paris&pin_path=/home/rajvi/Pictures/fire eye.png"  http://localhost:8082/v1/user/37df3b490a760f3b81eabe7d09001640/pin
echo -e "\n"
