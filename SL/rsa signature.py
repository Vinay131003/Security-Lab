def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def key_generation(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    if e >= phi or gcd(e, phi) != 1:
        raise ValueError("Invalid choice of e")
    d = mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def sign_message(message, private_key):
    d, n = private_key
    signature = pow(message, d, n)
    return signature

def verify_signature(signature, message, public_key):
    e, n = public_key
    computed_message = pow(signature, e, n)
    if computed_message == message:
        return True
    else:
        return False

# Input from the user
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter public key e: "))
message = int(input("Enter the message: "))

# Key generation
public_key, private_key = key_generation(p, q, e)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

# Sign generation
signature = sign_message(message, private_key)
print("Digital Signature:", signature)

# Verification
received_signature = int(input("Enter the received signature: "))
print("Received Message:", message)
if verify_signature(received_signature, message, public_key):
    print("The message is authentic.")
else:
    print("Message is altered. Discard.")