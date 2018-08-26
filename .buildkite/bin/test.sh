#! /bin/bash
set -ex

conda env create -p conda -f environment.yml
conda list -p conda

PATH=conda/bin/:$PATH

pytest -v --cov=./privileged_residues

codecov -F `echo ${BUILDKITE_LABEL} | sed -r -e 's/\W+/_/g' -e 's/_+$//'`
