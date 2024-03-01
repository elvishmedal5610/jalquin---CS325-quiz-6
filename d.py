#This program satisfies the D in SOLID by allowing us to easily switch or extend logging capabilities by simply providing a different 
#implementation of the Logger interface without modifying the application logic
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class LoggingLibraryLogger(Logger):
    def log(self, message):
        print("Logging message:", message)

class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def do_something(self):
        self.logger.log("Doing something...")

def main():
    logger = LoggingLibraryLogger()

    app = Application(logger)

    app.do_something()

if __name__ == "__main__":
    main()
