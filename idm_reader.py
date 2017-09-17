import nfc
import binascii

def connected(tag):
    idm = binascii.hexlify(tag.idm)
    print(idm)
    return idm

clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected}) # now touch a tag
clf.close()
