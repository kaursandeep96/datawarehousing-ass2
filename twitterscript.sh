#!/bin/sh

python3 twitter.py
sleep 0.5
python3 senti.py
sleep 0.5
python3 elastictwitter.py
