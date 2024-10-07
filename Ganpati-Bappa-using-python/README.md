## Now that we have the packages, we are ready to import it in our python script.

- turtle:
  *turtle for creative coding,If you’re having trouble installing it, don't worry, turtle comes pre-installed with Python. You should be able to use it without needing to install anything.*
  
```py
from turtle import *
```


### - Setting Up the Environment:

- *The from turtle import * line imports the turtle module, which provides a way to create graphics using a virtual “turtle.”*

- *The title('CoderHuBhai') sets the title of the turtle graphics window.*

- *The bgcolor("black") sets the background color to black.*

- *The speed(4) sets the drawing speed (4 is moderate).*

### - Drawing the Turtle Art:

- *The code defines a function called CoderHu(x, y) that moves the turtle cursor to the specified coordinates (x, y).*

- *The turtle then draws various shapes, including the trunk, eyes, tilak, crown, legs, and hands.*

- *Each shape is drawn using a combination of circle, forward, left, and other turtle commands.*

- *Colors are set using pencolor and fillcolor.*

- *The begin_fill() and end_fill() commands are used to fill shapes with color.*

### - Creating Symmetry:

*The left and right ears, legs, and hands are drawn symmetrically.*

### - Finishing Touches:

- *The turtle’s position is reset to the center using home().*

- *The screen is cleared using clearscreen().*

###   - Hiding the Turtle Cursor:

- *The hideturtle() command hides the turtle cursor.*

- *The done() command keeps the drawing window open until the user closes it.*
