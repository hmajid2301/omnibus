#!/bin/bash

export temp_config_dir=.temp-config
export paths_to_port=(.config/fish)

install_cmds() {
  sudo apt-get install fish fzf httpie vim  -y
  curl -fsSL https://starship.rs/install.sh | bash -s -- --yes
}
