#!/bin/bash

CITY=$1
curl -s "https://wttr.in/${CITY}?format=%t"