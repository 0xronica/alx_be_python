from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    Shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for Shape in Shapes:
        print(f"The area of the {Shape.__class__.__name__} is: {Shape.area()}")

if __name__ == "__main__":
    main()
