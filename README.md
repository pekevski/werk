# werk
script that creates an alias that opens up all the applications you need to start WERK

# setup
## Save the werk.py script where ever you like.
Create an alias for the script:

### macOs: 
add `alias werk='python3 "$HOME"/<directory>/werk.py'` to `~/.zshrc`
run `source ~/.zshrc`

### Linux: 
add `alias werk='python3 "$HOME"/<directory>/werk.py'` to `~/.bash_profile`
run `source ~/.bash_profile`

Now you can run `werk` in any terminal to load your apps.

# notes
if you would like to customise which apps open; then edit the `werk.py` script to your liking.
