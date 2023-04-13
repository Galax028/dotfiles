for file in $XDG_CONFIG_HOME/zsh/*; do
    source $file
done

source /usr/share/nvm/init-nvm.sh

eval "$(starship init zsh)"
