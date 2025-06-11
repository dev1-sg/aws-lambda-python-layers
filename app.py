#!/usr/bin/env python3

import aws_cdk as cdk
from src.stack import LambdaPythonLayers

app = cdk.App()

LambdaPythonLayers(app, "LambdaPythonLayers")

app.synth()
