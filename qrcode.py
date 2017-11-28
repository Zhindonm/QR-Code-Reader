import qrtools
import sys

qr = qrtools.QR()
result = qr.decode(filename=sys.argv[1])

coded_value = qr.data
print coded_value
