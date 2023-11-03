import hashlib


PUBLIC_KEY = 'e018c8a076151664e39f004fc6ccca13'
PRIVATE_KEY = 'f5e9842caaab96f2f3454a8f544d3bead7163739'
TS = "1"
TO_HASH = TS + PRIVATE_KEY + PUBLIC_KEY
HASHED = hashlib.md5(TO_HASH.encode())

MARVEL_DICT = {
    "PUBLIC_KEY": PUBLIC_KEY,
    "PRIVATE_KEY": PRIVATE_KEY,
    "TS": TS,
    "TO_HASH": TO_HASH,
    "HASHED": hashlib.md5(TO_HASH.encode()),
    "URL": "http://gateway.marvel.com/v1/public/" + "comics",
}


def get_marvel_params():
    return {
        "ts": MARVEL_DICT['TS'],
        "apikey": MARVEL_DICT['PUBLIC_KEY'],
        "hash": MARVEL_DICT['HASHED'].hexdigest(),
        "limit": "50",
        "offset": "0"
    }
