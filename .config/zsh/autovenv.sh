function autovenv() {
    if [ -d "./venv/" ]; then
        source "./venv/bin/activate"
        VENV_ROOT=$PWD
        export VENV_ROOT
    else
        if [ ! -z ${VIRTUAL_ENV+x} ]; then
            if [[ $PWD != $VENV_ROOT* ]]; then
                unset VENV_ROOT
                deactivate
            fi
        fi
    fi
}

chpwd_functions+=(autovenv)
