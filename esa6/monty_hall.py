import random


def monty_hall_simulation(num_experiments):
    success_with_change = 0
    success_without_change = 0

    for _ in range(num_experiments):
        doors = [0, 0, 1]  # 0 = goat, 1 = car
        random.shuffle(doors)

        initial_value = random.randint(0, 2)
        opened_door = next(i for i in range(3) if i != initial_value and doors[i] == 0)

        if doors[initial_value] == 1:
            success_without_change += 1
        else:
            success_with_change += 1

    return success_with_change, success_without_change


num_experiments = 100
success_change, success_no_change = monty_hall_simulation(num_experiments)
print(f"Erfolgreich bei Wechsel: {success_change}")
print(f"Erfolgreich bei Nicht-Wechsel: {success_no_change}")
