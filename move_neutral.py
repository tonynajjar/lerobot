from lerobot.common.robots.so101_follower import SO101FollowerConfig, SO101Follower
import time
robot_config = SO101FollowerConfig(
    port="/dev/ttyACM0",
    id="blitzers_follower",
)

robot = SO101Follower(robot_config)
robot.connect()

if __name__ == "__main__":
    queen_a = {'shoulder_pan.pos': 100.25958702064898, 'shoulder_lift.pos': -43.289861169541446, 'elbow_flex.pos': 36.29361123697328, 'wrist_flex.pos': 100.0, 'wrist_roll.pos': 79.23984272608126, 'gripper.pos': 11.73044925124792}
    robot.send_action(queen_a)