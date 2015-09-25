#!/usr/bin/env bash
pip uninstall -y cloudify-libcloud-plugin
pip install --no-deps /Users/kemi/Documents/Development/cloudify-libcloud-plugin-official
cfy local init -p local-blueprint.yaml
cfy local execute -w install

