#!/bin/bash
set -x
source ./.devcontainer/config.sh || echo "No 'config.sh' file found"

USERNAME=node
WORKSPACE_TEMP_CONFIG_DIR=${PWD}/${temp_config_dir}
HOME_DIR=/home/${USERNAME}

# """
# Moves a file or directory from the workspace dir to the home folder.
# """
move_to_home()
{
    local path=$1

    echo "${path}"

    full_path="${WORKSPACE_TEMP_CONFIG_DIR}"/"${path}"
    copy_path="${HOME_DIR}"/"${path}"

    echo "COPY_PATH ${copy_path} $full_path"

    if [ -d "${full_path}" ]
        then mkdir -p "${copy_path}" && cp -aR "${full_path}/." "${copy_path}" || echo "error copying file ${full_path}"
    elif [ -f "${full_path}" ]
        then cp "${full_path}" "${copy_path}" || echo "error copying folder ${full_path}"
    else echo "\"${full_path}\" is not valid";
        exit 1
    fi
}


for path in "${paths_to_port[@]}"
do
    echo "Moving path \"{$path}\""
    move_to_home "${path}"
done

# remove our config files in the temp folder (they have been copied to correct location)
rm -r "${WORKSPACE_TEMP_CONFIG_DIR}"

# install using commands specified in `config.sh`
install_cmds
