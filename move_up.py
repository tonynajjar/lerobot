from lerobot.common.robots.so101_follower import SO101FollowerConfig, SO101Follower
import time
robot_config = SO101FollowerConfig(
    port="/dev/ttyACM0",
    id="blitzers_follower",
)

robot = SO101Follower(robot_config)
robot.connect()

if __name__ == "__main__":
    rook_a = {'shoulder_pan.pos': -10.766961651917413, 'shoulder_lift.pos': -13.75683634833824, 'elbow_flex.pos': 2.673312188491167, 'wrist_flex.pos': 99.83043662568883, 'wrist_roll.pos': 99.68545216251638, 'gripper.pos': 14.559068219633945}
    robot.send_action(rook_a)