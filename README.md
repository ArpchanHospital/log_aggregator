This utility aggregates files from the speicifed location in config.json, it zips them up into a single
file using zlib for compression and then emails them to a given email address using gmail's SMTP relay

Usage:
First modify the config.json according to needs.
python Controller.py [smtp.username] [smtp.password] [from.email.id] [to.email.id]