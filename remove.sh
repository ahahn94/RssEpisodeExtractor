#!/usr/bin/env bash
python3 setup.py install --record files.txt
cat files.txt | xargs rm -rf
rm /usr/bin/rssepisodeextractor /usr/bin/rssepisodeextractor-gtk