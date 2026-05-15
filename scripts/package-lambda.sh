#!/bin/bash

set -e

cd lambda/grafana_plugin_installer

rm -rf package
mkdir package

pip3 install -r requirements.txt -t package/

cp index.py package/

cd package

zip -r ../../grafana-plugin-installer.zip .
