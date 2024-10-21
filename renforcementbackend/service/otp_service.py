import pyotp

def generate_otp(secret_key):
    totp = pyotp.TOTP(secret_key) 
    return totp.now()  

def verify_otp(secret_key, user_input_otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(user_input_otp)
