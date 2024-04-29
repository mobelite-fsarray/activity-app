from firebase_admin import auth

def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        # If the user is found, attempt to sign in with the provided credentials
        auth_user = auth.verify_password_reset_code(user.uid, password)
        return auth_user
    except auth.AuthError as e:
        # Handle authentication errors
        print(f"Authentication failed: {e}")
        return None