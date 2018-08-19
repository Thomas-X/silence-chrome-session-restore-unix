# how to use
* download zip of repo
* tar xf (zip file name)
* mkdir ~/.customscripts
* mv (.py script) ~/.customscripts/silencechrome.py
* crontab -e
* add the line `@reboot python3 ~/.customscripts/silencechrome.py`
* now on the next reboot of your system chrome never bugs you about restoring session, ever. Enjoy
