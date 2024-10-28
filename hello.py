import re
import pybullet as p
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def parse_prompt(prompt):
    # Extract speed, vehicle types, and location details
    speeds = re.findall(r"(\d+)\s*km/h", prompt)
    vehicle_types = re.findall(r"(\w+)-wheeler", prompt)
    accident_type = re.search(r"(collision|accident|impact)", prompt)
    
    # Process extracted details
    data = {
        "speeds": [int(speed) for speed in speeds],
        "vehicle_types": vehicle_types,
        "accident_type": accident_type.group(0) if accident_type else "unknown",
    }
    return data

# Example prompt
prompt = "On 4-lane divided national highways in Chennai’s Northern Districts, a two-wheeler and a four-wheeler head-on collision occurs. The two-wheeler is traveling at 80 km/h, while the four-wheeler is traveling at 120 km/h, resulting in a fatal injury to the rider."
parsed_data = parse_prompt(prompt)
print(parsed_data)
import pybullet as p
import time

# Connect to PyBullet Physics Simulation
p.connect(p.GUI)

# Set up simulation environment
p.setGravity(0, 0, -10)

# Load basic shapes for vehicles
plane_id = p.loadURDF("plane.urdf")
vehicle1 = p.loadURDF("r2d2.urdf", basePosition=[-10, 0, 0.1], baseVelocity=[80 / 3.6, 0, 0])  # 80 km/h in m/s
vehicle2 = p.loadURDF("r2d2.urdf", basePosition=[10, 0, 0.1], baseVelocity=[-120 / 3.6, 0, 0])  # 120 km/h in m/s

# Run simulation loop
for i in range(300):
    p.stepSimulation()
    time.sleep(1 / 240.0)

# Disconnect after simulation
p.disconnect()
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Basic setup for visualization
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-1, 1)

# Initialize vehicle positions
vehicle1_pos, = ax.plot([], [], 'bo', markersize=10)  # Blue dot for vehicle 1
vehicle2_pos, = ax.plot([], [], 'ro', markersize=10)  # Red dot for vehicle 2

# Animation function
def animate(i):
    # Update positions based on time
    vehicle1_x = -10 + (80 / 3.6) * (i / 30)
    vehicle2_x = 10 - (120 / 3.6) * (i / 30)
    
    vehicle1_pos.set_data(vehicle1_x, 0)
    vehicle2_pos.set_data(vehicle2_x, 0)
    
    return vehicle1_pos, vehicle2_pos

# Run animation
ani = animation.FuncAnimation(fig, animate, frames=60, interval=50, blit=True)
plt.show()
