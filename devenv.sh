#! /bin/bash

conda env update --prune -f environment.yml -p ./conda

git config --local include.path ../.gitconfig

