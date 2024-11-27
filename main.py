import random
import time


class Elevator:
    def __init__(self, total_floors, capacity):
        self.total_floors = total_floors
        self.capacity = capacity
        self.current_floor = 1
        self.direction = 1
        self.passengers = []

    def simulate_turn(self):
        self.passengers = [p for p in self.passengers if p != self.current_floor]

        available_space = self.capacity - len(self.passengers)
        new_passenger_count = min(available_space, random.randint(1, 5))

        for _ in range(new_passenger_count):
            target_floor = random.randint(1, self.total_floors)
            if target_floor != self.current_floor:
                self.passengers.append(target_floor)

        self.current_floor += self.direction
        if self.current_floor in {self.total_floors, 1}:
            self.direction *= -1

    def status(self):
        direction_str = "up" if self.direction == 1 else "down"
        print(f"Elevator is on floor {self.current_floor}, moving {direction_str}.")
        print(f"Passengers: {self.passengers}")

def main():
    elevator = Elevator(total_floors=10, capacity=8)
    for turn in range(10):
        print(f"\n--- Turn {turn + 1} ---")
        elevator.status()
        elevator.simulate_turn()
        time.sleep(1)

    print("\nSimulation completed.")


if __name__ == "__main__":
    main()
