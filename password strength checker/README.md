# Installing required Python packages

we need to download two important packages for this application.

Open your terminal and run the following command.

- zxcvbn:

   *You can now use the zxcvbn() function to analyze the strength of a password. Pass the password as the first parameter, and optionally provide a list of user-provided inputs (such as names or other context) as the user_inputs parameter.*
  
```terminal
pip install zxcvbn
```

- getpass:
  
 *You can now use the getpass.getpass() function to securely read passwords without displaying them on the screen.*
 
```terminal
pip install getpass
```
*Now that we have the packages, we are ready to import it in our python script.*

```py
from zxcvbn import zxcvbn
```

##  - Importing the zxcvbn Module:

 *The line from zxcvbn import zxcvbn brings in the zxcvbn module, which is a realistic password strength estimator.*

 *The original zxcvbn library was written in JavaScript by the team at Dropbox.*

##  - Checking Password Strength:

 *The user is prompted to enter a password (securely, without echoing it on the screen).*

 *The zxcvbn() function analyzes the password and provides the following information:*

 *The password itself.*

 *A score (from 0 to 4) indicating its strength.*

 *An estimate of how long it would take to crack the password in different scenarios.*

 *Feedback and suggestions for improving the password.*
