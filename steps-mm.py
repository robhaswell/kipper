import argparse
full_steps_per_rotation = 200
microsteps = 16

parser = argparse.ArgumentParser(description='Calculate the number of steps to rotate a stepper motor.')
parser.add_argument("steps_per_mm", type=float, help="The number of steps per mm")
args = parser.parse_args()

steps_per_mm = args.steps_per_mm

rotation_distance = full_steps_per_rotation * microsteps / steps_per_mm

print(rotation_distance)
