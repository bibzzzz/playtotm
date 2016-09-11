# playtotm

Repository for turn based game hosted at www.playtotm.com

## Key contributors:

* Nathan Phennel - front-end, dev-ops
* Habib Adam - game-engine, database structure

## Local environment setup:

1. Download web2by for mac: http://www.web2py.com/examples/static/web2py_osx.zip
1. Once downloaded, unzip and it goes to */Applicaitons* folder
1. Open Terminal
1. Go into the web2py applications folder:
 * ```cd /Applications/web2py.app/Contents/Resources/applications ```
1. Cloning your repo into your local web2py framework:
 * ```git clone https://github.com/bibzzzz/playtotm.git ```

Now we can pull and push code using this dir and github. And share identical setups to make it easier to resolve issues.

### To code:
1. Open up your favorite IDE (my fave atm is [vscode](https://code.visualstudio.com/download) from mcsft)
1. Open the web2py app in the ide (may not work on all IDEs)
1. Use the side nav panel to find "Contents/Resources/applications/playtotm/"
1. Magic finger keyboard dance

#### To Test Code:
1. Double-click the web2py app
2. In the app window, type in any password (required for local admin site access)
3. Click *"Start-Server"*
4. Open Chrome icognito (or opera if you're cool like me... ☺)
5. Pop into the address bar:
 * ```http://127.0.0.1:8700/playtotm/default/index```
6. Change something, refresh. May need to clear cache in browser for some things.