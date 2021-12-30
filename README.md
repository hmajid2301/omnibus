# Banter Bus Ominibus

A RESTful API to manage the games and questions for the Banter Bus application.

## Running using devcontainer

The easiest way to setup this project is to use vscode's development containers.
For this you will need:

- vscode
- [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

First make a copy of the example files:

```bash
cp .env.sample .env
cp .devcontainer/devcontainer.example.json .devcontainer/devcontainer.json
cp .devcontainer/config.example.sh .devcontainer/config.sh
```

> The reason for this is so we can customise our development environment. For example I like to use fish shell instead of bash.

### Example `config.sh` file

```bash
#!/bin/bash

# Name of the folder to copy files to in project (this folder should get deleted)
export temp_config_dir=.temp-config

# List of files to copy from host machine (relative to home directory) to docker container
export paths_to_port=(.config/fish)

# List of commands to run after the container is running
install_cmds() {
   apt-get install fish fzf httpie vim  -y
   curl -fsSL https://starship.rs/install.sh | bash -s -- --yes
}
```
