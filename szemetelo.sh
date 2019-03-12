#!/bin/bash

echo ">> How many e-mails do you want to send?"

read a;

echo ">> How many seconds should be left between two mails?"

read b;

COUNTER=$a
       until [  $COUNTER -lt 1 ]; do
           echo $COUNTER". e-mail";
           sleep $b; python3 send_email.py
           let COUNTER-=1
       done
