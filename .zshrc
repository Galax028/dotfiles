# Shell history
HISTFILE=~/.zsh_history
HISTSIZE=1000
SAVEHIST=3000

# Autocompletion
zstyle :compinstall filename "/home/galax/.zshrc"

autoload -Uz compinit && compinit
autoload -Uz bashcompinit && bashcompinit

# Node version manager
source /usr/share/nvm/init-nvm.sh

# Aliases
source ~/.config/zsh/aliases.sh

# Plugions
source ~/.config/zsh/plugins.zsh

# Starship prompt
eval "$(starship init zsh)"

