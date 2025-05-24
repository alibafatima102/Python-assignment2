class Logger:
    # Constructor
    def __init__(self):
        print("🟢 Logger object created.")

    # Destructor
    def __del__(self):
        print("🔴 Logger object destroyed.")

# Creating an object of Logger
log = Logger()

# Optional: Forcing object deletion (for demonstration)
del log  # This will immediately call the destructor (if no references remain)
