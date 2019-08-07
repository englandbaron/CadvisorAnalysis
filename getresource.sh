#!/usr/bin/env bash
folder=`date "+%Y_%m_%d_%H_%M_%S"`
mkdir $folder
curl http://node1:8080/api/v2.1/machine?recursive=true > $folder/machine.json &
#curl http://node1:8080/api/v2.1/summary?recursive=true > $folder/summary.json &
curl http://node1:8080/api/v2.1/stats?recursive=true > $folder/stats.json
curl http://node1:8080/api/v2.1/machinestats?recursive=true > $folder/machinestats.json &