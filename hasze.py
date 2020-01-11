import hashlib
h = hashlib.new('ripemd160')
h.update(b"Nobody inspects the spammish repetition")
print(h.hexdigest())
