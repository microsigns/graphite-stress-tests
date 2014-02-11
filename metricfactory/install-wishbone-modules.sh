#! /usr/bin/env bash
git clone https://github.com/Lacrymology/wishboneModules.git

pushd wishboneModules/wb_output_tcp
python setup.py install
popd

