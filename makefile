SHELL=/bin/bash

.PHONY: bootstrap deploy

bootstrap:
	@cdk bootstrap --qualifier layersdev

deploy:
	@cdk deploy --context @aws-cdk/core:bootstrapQualifier=layersdev
