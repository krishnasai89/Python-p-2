# Installing required Python packages
*we need to download important packages for this application.*

*Open your terminal and run the following command.*

- getpass:
  
*This will hide the password input in the terminal*

```terminal 
pip install getpass
```
*Now that we have the packages, we are ready to import it in our python script.*

```py
from getpass import getpass
```

###  - What Is the getpass Module?

- *The getpass module provides a secure way to prompt users for passwords without displaying them (echoing) on the screen.*

- *It’s commonly used in command-line interfaces (CLI) or terminal-based applications.*

### - Functions in the getpass Module:

- *getpass.getpass(prompt='Password: ', stream=None):*

- *Prompts the user for a password without echoing the input.*

- *The user is prompted using the string prompt, which defaults to 'Password: '.**

- *On Unix systems, the prompt is written to the file-like object stream (usually /dev/tty) or, if unavailable, to sys.stderr.*

- *If echo-free input is unavailable, getpass() falls back to printing a warning message and reads from sys.stdin.*

- getpass.getuser():*

- *Returns the “login name” of the user.*

- *It checks environment variables (LOGNAME, USER, LNAME, and USERNAME) and returns the first non-empty value found.*

- *If none are set, it retrieves the login name from the password database .*

### - Use Cases:

- *You can use getpass whenever you need to securely accept a password or sensitive input from users without revealing it on the screen.*

- *It’s commonly used in authentication systems, password management tools, and other security-related applications.*
