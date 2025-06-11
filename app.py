#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import Tags
from layers.stack import LambdaLayersStack

app = cdk.App()

LambdaLayersStack(app, "LambdaLayersStack")

app.synth()
