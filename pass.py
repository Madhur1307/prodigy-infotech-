import re  

def assess_password_strength(password):
    strength = 0
    feedback = []

    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, $).")

    
    if strength == 5:
        strength_level = "Very Strong"
    elif strength == 4:
        strength_level = "Strong"
    elif strength == 3:
        strength_level = "Moderate"
    elif strength == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    return strength_level, feedback


password = input("Enter your password: ")
strength_level, feedback = assess_password_strength(password)

print(f"Password Strength: {strength_level}")
for msg in feedback:
    print(f"- {msg}")
