# QR Code Reader
=============

###1. Introduction
This is a simple python program that reads strings encoded in QR codes.
Other encoding samples like images have not been properly tested.
You will need an aditional module named qrtools

###2. Dependencies

```
[sudo] pip install pypng
[sudo] pip install zbar
[sudo] pip install pillow
```

###3. Install
To install qrtools:

```
git clone https://github.com/primetang/qrtools.git
cd qrtools
[sudo] python setup.py install
```

Or directly through `pip` to install it:
```
[sudo] pip install qrtools
```

###4. Usage

```
python qrcode.py <path to qr code>
```

###5. Example
Running the following command:

```
python qrcode.py example/this-is-a-qr-code.png
```

Will produce the following output in stdout:

```
python qrcode.py example/this-is-a-qr-code.png
```
