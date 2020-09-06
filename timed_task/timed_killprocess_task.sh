#! /bin/sh
ps -ef|grep "python capture_raw_4M_2hour *"|awk '{print $2}'|xargs kill -9

