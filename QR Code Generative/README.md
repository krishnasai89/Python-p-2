## Installing required python packages
- qrcode:*qrcode library is a pure Python QR code generator that allows you to create QR codes effortlessly. It’s like having a digital stencil for encoding information*
```terminal
pip install qrcode
```
*Now that we have the packages, we are ready to import it in our python script.*
```py
import qrcode
```
## OUTPUT:
![image desc](./QRcode.png)

- Importing the qrcode Module:

*The line import qrcode brings in the qrcode module, which allows you to generate QR codes from any kind of data.*

- Generating the QR Code:

*You’ve specified the data for your QR code: a URL pointing to your GitHub profile (https://github.com/vellampallikrishnasaigifhub).

The qrcode.make(data) function creates a QR code image based on the provided data.

The resulting QR code is stored in the qr variable.*

- Saving the QR Code Image:

*The qr.save("github.png") line saves the QR code image as a PNG file named “github.png” in your current working directory.

Now you have a file containing your GitHub QR code!*

- Print Confirmation:

*The last line prints a message to let you know that the QR code has been generated and saved successfully.*
