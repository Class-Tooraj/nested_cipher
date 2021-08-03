###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORTS
from base64 import urlsafe_b64encode, urlsafe_b64decode

b64_encode = urlsafe_b64encode
b64_decode = urlsafe_b64decode


# ALL BASE 64 ENCODER
def ab64_encode(data: bytes) -> bytes:
    data = b64_encode(data).decode()
    data = (b64_encode(i.encode('ascii')) for i in data)
    return b64_encode(b' '.join(iter(data)))

# ALL BASE 64 DECODER
def ab64_decode(data: bytes) -> bytes:
    data = b64_decode(data).decode('ascii').split(' ')
    data = (b64_decode(i.encode('ascii')) for i in data)
    return b64_decode(b''.join(iter(data)))

# --- ~ --- #

# MID BASE 64 ENCODER
def mb64_encode(data: bytes) -> bytes:
    data = b64_encode(data).decode('ascii')
    mid = len(data) // 2
    data = data[mid :] + data[: mid]
    return b64_encode(data.encode('ascii'))

# MID BASE 64 DECODER
def mb64_decode(data: bytes) -> bytes:
    data = b64_decode(data).decode('ascii')
    mid = len(data) // 2
    data = data[mid :] + data[: mid]
    return b64_decode(data.encode('ascii'))

# --- ~ --- #

# REVERSED BASE 64 ENCODER
def rb64_encode(data: bytes) -> bytes:
    data = b64_encode(data).decode('ascii')
    data = b64_encode(''.join(reversed(data)).encode('ascii')).decode('ascii')
    return b64_encode(''.join(reversed(data)).encode('ascii'))

# REVERSED BASE 64 DECODER
def rb64_decode(data: bytes) -> bytes:
    data = b64_decode(data).decode('ascii')
    data = b64_decode(''.join(reversed(data)).encode('ascii')).decode('ascii')
    return b64_decode(''.join(reversed(data)).encode('ascii'))

# --- ~ --- #

# EXCLUSIVE BASE 64 ENCODER
def eb64_encode(data: bytes) -> bytes:
    data = ab64_encode(data).decode('ascii')
    data = (ab64_encode(i.encode('ascii')) for i in data)
    return mb64_encode(b' '.join(iter(data)))

# EXCLUSIVE BASE 64 DECODER
def eb64_decode(data: bytes) -> bytes:
    data = mb64_decode(data).decode('ascii').split(' ')
    data = (ab64_decode(i.encode('ascii')) for i in data)
    return ab64_decode(b''.join(iter(data)))

# --- ~ --- #

# LONG BASE 64 ENCODER
def lb64_encode(data: bytes) -> bytes:
    data = mb64_encode(data).decode('ascii')
    data = (mb64_encode(i.encode('ascii')) for i in data)
    return mb64_encode(b' '.join(iter(data)))

# LONG BASE 64 DECODER
def lb64_decode(data: bytes) -> bytes:
    data = mb64_decode(data).decode('ascii').split(' ')
    data = (mb64_decode(i.encode('ascii')) for i in data)
    return mb64_decode(b''.join(iter(data)))

# --- ~ --- #

# REVERSE ALL BASE 64 ENCODER
def rab64_encode(data: bytes) -> bytes:
    return ab64_encode(rb64_encode(data))

# REVERSE ALL BASE 64 DECODER
def rab64_decode(data: bytes) -> bytes:
    return rb64_decode(ab64_decode(data))

# --- ~ --- #

# REVERSE MID BASE 64 ENCODER
def rmb64_encode(data: bytes) -> bytes:
    return mb64_encode(rb64_encode(data))

# REVERSE MID BASE 64 DECODER
def rmb64_decode(data: bytes) -> bytes:
    return rb64_decode(mb64_decode(data))

# --- ~ --- #

# REVERSE EXCLUSIVE BASE 64 ENCODER
def reb64_encode(data: bytes) -> bytes:
    return eb64_encode(rb64_encode(data))

# REVERSE EXCLUSIVE BASE 64 DECODER
def reb64_decode(data: bytes) -> bytes:
    return rb64_decode(eb64_decode(data))

# --- ~ --- #

# REVERSE LONG BASE 64 ENCODER
def rlb64_encode(data: bytes) -> bytes:
    return eb64_encode(rb64_encode(data))

# REVERSE LONG BASE 64 DECODER
def rlb64_decode(data: bytes) -> bytes:
    return rb64_decode(eb64_decode(data))

__all__ = (
    'ab64_encode',
    'ab64_decode',
    'mb64_encode',
    'mb64_decode',
    'eb64_encode',
    'eb64_decode',
    'lb64_encode',
    'lb64_decode',
    'rb64_encode',
    'rb64_decode',
    'rab64_encode',
    'rab64_decode',
    'rmb64_encode',
    'rmb64_decode',
    'reb64_encode',
    'reb64_decode',
    'rlb64_encode',
    'rlb64_decode',
    )
