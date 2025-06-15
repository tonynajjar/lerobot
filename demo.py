import os
import time

# os.system("python -m lerobot.replay --robot.type=so101_follower --robot.disable_torque_on_disconnect=False --robot.port=/dev/ttyACM0 --robot.id=blitzers_follower --dataset.repo_id=tonynajjar/record-test --dataset.episode=0")
# os.system("python /home/tony/lerobot/move_neutral.py")
os.system("python /home/tony/lerobot/move_up.py")
os.system("rm -r /home/tony/.cache/huggingface/lerobot/HovorunB/eval_pick-model-bhd-9")
os.system("python -m lerobot.record --robot.type=so101_follower  --robot.port=/dev/ttyACM0 --robot.id=blitzers_follower --robot.cameras=\"{arm: {type: opencv, index_or_path: 4, width: 640, height: 480, fps: 30}}\" --dataset.single_task=\"pick a piece\" --dataset.repo_id=HovorunB/eval_pick-model-bhd-9 --dataset.num_episodes=1  --policy.path=HovorunB/pick-model-johannes")
os.system("rm -r /home/tony/.cache/huggingface/lerobot/HovorunB/eval_drop-model-5")
os.system("python -m lerobot.record2 --robot.type=so101_follower  --robot.port=/dev/ttyACM0 --robot.id=blitzers_follower --robot.cameras=\"{arm: {type: opencv, index_or_path: 4, width: 640, height: 480, fps: 30}}\" --dataset.single_task=\"pick a piece\" --dataset.repo_id=HovorunB/eval_drop-model-5 --dataset.episode_time_s=6000 --policy.path=HovorunB/drop-model-1")
