from aws_cdk import Stack
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python_alpha import PythonLayerVersion
from constructs import Construct
from pathlib import Path
import re

class LambdaPythonLayers(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        root_dir = Path(__file__).parent / "layers"  # points to src/layers

        for group_dir in root_dir.iterdir():
            if not group_dir.is_dir():
                continue

            for layer_dir in group_dir.iterdir():
                if not layer_dir.is_dir():
                    continue

                requirements_file = layer_dir / "requirements.txt"
                if not requirements_file.exists():
                    continue

                dependencies = []
                with open(requirements_file) as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        match = re.match(r"([\w\-]+)==([\d\.]+)", line)
                        if not match:
                            print(f"Skipping {layer_dir}: invalid format in line '{line}'")
                            dependencies = None
                            break
                        dependencies.append(match.groups())

                if dependencies is None:
                    continue

                description = ", ".join(f"{pkg}=={ver}" for pkg, ver in dependencies)
                full_layer_name = f"{group_dir.name}_{layer_dir.name}"

                PythonLayerVersion(
                    self, full_layer_name,
                    entry=str(layer_dir),
                    compatible_runtimes=[Runtime.PYTHON_3_11],
                    description=f"Python dependencies: {description}"
                )