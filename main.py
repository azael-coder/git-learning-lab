def motor_status(current):
    if current > 20:
        return "OVERLOAD"
    return "NORMAL"

print(motor_status(15))
print(motor_status(25))
