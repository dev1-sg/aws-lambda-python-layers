SHELL=/bin/bash

.PHONY: bootstrap deploy

bootstrap:
	@sudo cdk bootstrap --qualifier layersdev

deploy:
	@sudo cdk deploy --context @aws-cdk/core:bootstrapQualifier=layersdev
