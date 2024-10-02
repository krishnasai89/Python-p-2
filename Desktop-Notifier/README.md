## Installing required Python packages
*we need to download two important packages for this application.*

*Open your terminal and run the following command.*

- **1.requests** :

 *in case you want to fetch data from the web*

```terminal
 pip install requests
```

- **2. plyer** :

*For creating notifications on your PC*

```terminal
pip install plyer
```

*Now that we have the packages, we are ready to import it in our python script.*

```py
from plyer import notification
```

## Coding Timuu

- Now let's specify the parameters.

```py
from plyer import notification

title = 'Hi, Hello and Hi !'

message = 'If u reading this ~I LOVE U TO THE MOON AND BACK !!'

notification.notify(title = title,
                    message = message,
                    timeout = 5)
```

Parameters:

- `title (str`) : Title of the notification
- `message (str)` : Message of the notification
