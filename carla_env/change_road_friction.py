import carla

def change_friction_between_waypoints(start_waypoint, end_waypoint, friction):
    waypoints = []
    current_waypoint = start_waypoint.next(2.0)[0]  # Moves 2 meters ahead to start between waypoints
    while current_waypoint.transform.location.distance(end_waypoint.transform.location) > 2.0:
        waypoints.append(current_waypoint)
        current_waypoint = current_waypoint.next(2.0)[0]


    for waypoint in waypoints:
        waypoint.set_friction(friction)


client = carla.Client('localhost', 2000)
client.set_timeout(5.0)


world = client.get_world()
map = world.get_map()


start_location = carla.Location(x=100, y=200, z=0)  # Manually update with coordinates
end_location = carla.Location(x=150, y=200, z=0)   # Manually update with coordinates

start_waypoint = map.get_waypoint(start_location)
end_waypoint = map.get_waypoint(end_location)


# change_friction_between_waypoints(start_waypoint, end_waypoint, 0.8) // use this line to call from train.py
