#!/bin/bash
#------------Darshit Kuwadia----------#
# test client access to our service

echo -e "\n"
curl -i -H "Accept: application/json" --data "board_name=Travel&board_id=100"  http://localhost:8082/v1/user/37df3b490a760f3b81eabe7d09001640/board
echo -e "\n"
