# http://www.apache.org/licenses/LICENSE-2.0.txt
# Copyright 2016 Intel Corporation
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

################# URL Format ####################
# /light/color/*/mode/*/duration/*

#this is specific to my machine because of the sys.path.insert

import sys
sys.path.insert(0, '/vagrant/blynclight')
from argparse import ArgumentParser
import blynclight
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/blynclight/<string:mode>/<string:color>/<int:iterations>", methods = ['POST'])
def trigger(mode, color, iterations):
	options = {'pulse': blynclight.pulseServer,
		'cycle': blynclight.cycleServer,
		'flash': blynclight.flashServer
	}

	options[mode](color=color, iterations=iterations)
	return 'OK\n'

@app.route("/blynclight/flash/<string:color>/", methods = ['POST'])
def flash(color): 
	return redirect(url_for('trigger', mode='pulse', color=color, iterations=1))

if __name__ == "__main__": 
	app.run(host='0.0.0.0')











