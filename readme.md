# lambda-python-layers

### Prerequisites

- python3
- python3-pip
- python3-venv
- make
- aws-cli
- aws-cdk
- docker

### Getting started

```bash
python3 -m venv venv
pip install -r requirements.txt
```

```bash
make bootstrap
make deploy
```

### Add New layers

Create layers at `src/layers/common/<layers-name>/requirements.txt`

```bash
mkdir -p src/layers/common/<layers-name>
```

You may add packages to requirements.txt

```bash
touch src/layers/python/common/<layers-name>/requirements.txt
```

Deploy resources

```bash
make deploy
```
