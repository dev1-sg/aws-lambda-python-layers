#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import Tags
from layers.lambda_layers_stack import LambdaLayersStack

app = cdk.App()

LambdaLayersStack(app, "LambdaLayersStack")

app.synth()
