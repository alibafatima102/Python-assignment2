# Engine class
class Engine:
    def start(self):
        print("Engine started!")

# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Engine object passed to Car
    
    def start_car(self):
        print("Car is ready to go.")
        self.engine.start()  # Accessing Engine's method via Car

# Create an Engine object
my_engine = Engine()

# Pass Engine object to Car
my_car = Car(my_engine)

# Start the car, which starts the engine
my_car.start_car()
