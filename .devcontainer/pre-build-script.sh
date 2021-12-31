#!/bin/bash
set -x
source ./.devcontainer/config.sh

# Delete our temp directory if one already exists
if [ -d "./${temp_config_dir}" ]; then rm -Rf "./${temp_config_dir}"; fi
mkdir "./${temp_config_dir}"

# """
# Moves a file or directory from the host to the workspace folder so that it
# can be used by the dev container. This needs to be done since the root's
# home directory is out of scope for the workspace, so desired files from outside
# of the workspace scope need to be ported over before hand.
# """
move_to_workspace()
{
    local path=$1

    full_path=~/$path
    copy_path=./${temp_config_dir}/${path}

    echo "Copying ${full_path} to ${copy_path}"

    if [ -d "${full_path}" ]
        then mkdir -p "./${copy_path}" && cp -aR "${full_path}/." "${copy_path}" || echo "error copying folder ${full_path}"
    elif [ -f "${full_path}" ]
        then cp "${full_path}" "./${copy_path}" || echo "error copying file ${full_path}"
    else echo "${full_path} is not valid";
        exit 1
    fi
}

for path in "${paths_to_port[@]}"
do
    move_to_workspace "${path}"
done