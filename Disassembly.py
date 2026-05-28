# This is the code for the project made by group 243

# For movel the tool position is used
# For movej the joint angles are used
# Note that all angles are measured in radians
# Note all lengths are measured in meters


import time
import urx
import math
import numpy as np


def disassemble():
    # Connect to the UR5 robot
    robot_ip = "192.168.0.10"
    try:
        print(f"Connecting to UR5 at {robot_ip}...")
        rob = urx.Robot(robot_ip)
    except Exception as e:
        print(f"Failed to connect to the robot: {e}")
        return
    print("Connected to UR5 successfully.")

    v_j_mult = 3
    a_j_mult = 15
    linear_mult = math.pi

    joint_speed_limiter = 1 / a_j_mult * math.pi

    # Joint speed and acceleration profiles (rad/s, rad/s^2)
    v_j = 1.050 * v_j_mult
    a_j = 1.400 * a_j_mult
    # Linear speed and acceleration profiles (m/s, m/s^2)
    v_l = 0.250 * linear_mult
    a_l = 1.200 * linear_mult

    # Define Reference Frame (x, y, z, rx, ry, rz)
    # ref_frame = [-0.353200, -0.353200, 0.000000, 0.000000, 0.000000, -2.356194]

    # Define TCP transformation from the wrist
    rob.set_tcp((0, 0, 0.125, 0, 0, 0))

    def gripper_activation():
        rob.set_digital_out(0, False)
        rob.set_digital_out(1, False)
        time.sleep(0.1)

    # Opens or closes gripper based on the input of "Open"
    def gripper(Open):
        if Open:  # Opens gripper
            rob.set_digital_out(0, True)
            rob.set_digital_out(1, False)
            time.sleep(0.1)
        elif not Open:  # Closes gripper
            rob.set_digital_out(0, False)
            rob.set_digital_out(1, True)
            time.sleep(0.1)

    ### Sequences for different removal processes:

    def home():
        rob.movej(np.radians([-135.000000, -90.000000, -90.000000, -90.000000, 90.000000, 0.000000]), acc=a_j * joint_speed_limiter, vel=v_j * joint_speed_limiter, wait=True, threshold=None)

    def lid():
        # Move to lid and grasp
        rob.movej(np.radians([-134.132713, -97.686727, -115.031895, -57.281154, 90.000217, 0.867287]), acc=a_j, vel=v_j,  wait=True, threshold=None)
        rob.movel([-0.413657467, -0.269407684, 0.035000000, np.radians(-68.882960), np.radians(-166.298177), np.radians(-0.001600)], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(False)

        # Move lid to drop
        rob.movej(np.radians([-134.132713, -97.686727, -115.031895, -57.281154, 90.000217, 0.867287]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movej(np.radians([-124.270263, -50.925563, -146.519454, -72.555242, 89.999824, 10.729737]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movel([-0.203411286, -0.104416337, 0.015106000, -1.202345, -2.902479, -0.000008], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(True)
        rob.movej(np.radians([-124.270263, -50.925563, -146.519454, -72.555242, 89.999824, 10.729737]), acc=a_j, vel=v_j, wait=True, threshold=None)

    def module_1():
        # Move to module 1 and grasp
        rob.movej(np.radians([-139.361732, -91.828288, -123.644443, -54.527269, 90.000000, -94.361732]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movel([-0.395626244, -0.195515025, 0.024500000, np.radians(-68.883018), np.radians(166.298316), np.radians(0.000000)], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(False)
        rob.movej(np.radians([-139.361732, -91.828288, -123.644443, -54.527269, 90.000000, -94.361732]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # Drop sequence:
        #rob.movej(np.radians([-112.756823, -88.319239, -127.699794, -53.980968, 90.000000, -67.756823]), acc=a_j, vel=v_j, wait=True, threshold=None)
        #rob.movel([-0.255265548, -0.325976226, 0.022500000, -1.202335, 2.902453, -0.000000], acc=a_l, vel=v_l, wait=True, threshold=None)
        #gripper(True)
        #rob.movej(np.radians([-112.756823, -88.319239, -127.699794, -53.980968, 90.000000, -67.756823]), acc=a_j, vel=v_j, wait=True, threshold=None)

    def module_2():
        # Move to module 2 and grasp
        rob.movej(np.radians([-129.635641, -88.738403, -126.754671, -54.506927, 90.000000, -84.635641]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movel([-0.342239682, -0.241830519, 0.024500000, np.radians(-68.883018), np.radians(166.298316), np.radians(-0.000000)], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(False)
        rob.movej(np.radians([-129.635641, -88.738403, -126.754671, -54.506927, 90.000000, -84.635641]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # Drop sequence:
        # rob.movej(np.radians([-102.643647, -90.754114, -125.291313, -53.954573, 90.000000, -57.643647]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # rob.movel([-0.197989899, -0.383251875, 0.022500000, -1.202335, 2.902453, -0.000000], acc=a_l, vel=v_l, wait=True, threshold=None)
        # gripper(True)
        # rob.movej(np.radians([-102.643647, -90.754114, -125.291313, -53.954573, 90.000000, -57.643647]), acc=a_j, vel=v_j, wait=True, threshold=None)

    def module_3():
        # Move to module 3 and grasp
        rob.movej(np.radians([-138.506672, -97.586607, -117.259688, -55.153705, 90.000000, -93.506672]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movel([-0.426385389, -0.231223917, 0.024500000, np.radians(-68.883018), np.radians(166.298316), np.radians(0.000000)], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(False)
        rob.movej(np.radians([-138.506672, -97.586607, -117.259688, -55.153705, 90.000000, -93.506672]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # Drop sequence:
        # rob.movej(np.radians([-115.046166, -94.704355, -121.089307, -54.206337, 90.000000, -70.046166]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # rob.movel([-0.288499567, -0.359210245, 0.022500000, -1.202335, 2.902453, -0.000000], acc=a_l, vel=v_l, wait=True, threshold=None)
        # gripper(True)
        # rob.movej(np.radians([-115.046166, -94.704355, -121.089307, -54.206337, 90.000000, -70.046166]), acc=a_j, vel=v_j, wait=True, threshold=None)

    def module_4():
        # Move to module 4 and grasp
        rob.movej(np.radians([-129.834236, -94.867901, -120.368875, -54.763224, 90.000000, -84.834236]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movel([-0.372822050, -0.276301975, 0.024500000, np.radians(-68.883018), np.radians(166.298316), np.radians(0.000000)], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(False)
        rob.movej(np.radians([-129.834236, -94.867901, -120.368875, -54.763224, 90.000000, -84.834236]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # Drop sequence:
        # rob.movej(np.radians([-105.773672, -96.738190, -118.784942, -54.476868, 90.000000, -60.773672]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # rob.movel([-0.231223917, -0.416485894, 0.022500000, -1.202335, 2.902453, 0.000000], acc=a_l, vel=v_l, wait=True, threshold=None)
        # gripper(True)
        # rob.movej(np.radians([-105.773672, -96.738190, -118.784942, -54.476868, 90.000000, -60.773672]), acc=a_j, vel=v_j, wait=True, threshold=None)

    def module_5():
        # Move to module 5 and grasp
        rob.movej(np.radians([-137.891558, -103.027796, -110.542616, -56.429588, 90.000000, -92.891558]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movel([-0.456967757, -0.265695373, 0.024500000, np.radians(-68.883018), np.radians(166.298316), np.radians(0.000000)], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(False)
        rob.movej(np.radians([-137.891558, -103.027796, -110.542616, -56.429588, 90.000000, -92.891558]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # Drop sequence:
        # rob.movej(np.radians([-116.907609, -100.666746, -114.068567, -55.264686, 90.000000, -71.907609]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # rob.movel([-0.321733585, -0.392444264, 0.022500000, -1.202335, 2.902453, -0.000000], acc=a_l, vel=v_l, wait=True, threshold=None)
        # gripper(True)
        # rob.movej(np.radians([-116.907609, -100.666746, -114.068567, -55.264686, 90.000000, -71.907609]), acc=a_j, vel=v_j, wait=True, threshold=None)

    def module_6():
        # Move to module 6 and grasp
        rob.movej(np.radians([-129.948662, -100.751050, -113.431860, -55.817090, 90.000000, -84.948662]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movel([-0.403757972, -0.311834091, 0.024500000, np.radians(-68.883018), np.radians(166.298316), np.radians(0.000000)], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(False)
        rob.movej(np.radians([-129.948662, -100.751050, -113.431860, -55.817090, 90.000000, -84.948662]), acc=a_j,vel=v_j, wait=True, threshold=None)
        # Drop sequence:
        # rob.movej(np.radians([-108.364526, -102.425720, -111.846417, -55.727863, 90.000000, -63.364526]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # rob.movel([-0.264457936, -0.449719913, 0.022500000, -1.202335, 2.902453, -0.000000], acc=a_l, vel=v_l, wait=True, threshold=None)
        # gripper(True)
        # rob.movej(np.radians([-108.364526, -102.425720, -111.846417, -55.727863, 90.000000, -63.364526]), acc=a_j, vel=v_j, wait=True, threshold=None)

    def module_7():
        # Move to module 7 and grasp
        rob.movej(np.radians([-137.371217, -108.468082, -103.202328, -58.329590, 90.000000, -92.371217]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movel([-0.488257232, -0.300873935, 0.024500000, np.radians(-68.883018), np.radians(166.298316), np.radians(0.000000)], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(False)
        rob.movej(np.radians([-137.371217, -108.468082, -103.202328, -58.329590, 90.000000, -92.371217]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # Drop sequence:
        # rob.movej(np.radians([-118.451024, -106.378003, -106.614325, -57.007672, 90.000000, -73.451024]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # rob.movel([-0.354967604, -0.425678282, 0.022500000, -1.202335, 2.902453, -0.000000], acc=a_l, vel=v_l, wait=True, threshold=None)
        # gripper(True)
        # rob.movej(np.radians([-118.451024, -106.378003, -106.614325, -57.007672, 90.000000, -73.451024]), acc=a_j, vel=v_j, wait=True, threshold=None)

    def module_8():
        # Move to module 8 and grasp
        rob.movej(np.radians([-130.036470, -106.322598, -106.168516, -57.508886, 90.000000, -85.036470]), acc=a_j, vel=v_j, wait=True, threshold=None)
        rob.movel([-0.434163564, -0.346835876, 0.024500000, np.radians(-68.883018), np.radians(166.298316), np.radians(0.000000)], acc=a_l, vel=v_l, wait=True, threshold=None)
        gripper(False)
        rob.movej(np.radians([-130.036470, -106.322598, -106.168516, -57.508886, 90.000000, -85.036470]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # Drop sequence:
        # rob.movej(np.radians([-110.541762, -107.947393, -104.448336, -57.604271, 90.000000, -65.541762]), acc=a_j, vel=v_j, wait=True, threshold=None)
        # rob.movel([-0.297691955, -0.482953932, 0.022500000, -1.202335, 2.902453, -0.000000], acc=a_l, vel=v_l, wait=True, threshold=None)
        # gripper(True)
        # rob.movej(np.radians([-110.541762, -107.947393, -104.448336, -57.604271, 90.000000, -65.541762]), acc=a_j, vel=v_j, wait=True, threshold=None)

    ###Drop sequences:
    #[[approach(movej)], [drop(movel)]]
    drop_sequence_positions=[
        # Drop 1
        [np.radians([-112.756823, -88.319239, -127.699794, -53.980968, 90.000000, -67.756823]), [-0.255265548, -0.325976226, 0.022500000, -1.202335, 2.902453, -0.000000]],
        # Drop 2
        [np.radians([-102.643647, -90.754114, -125.291313, -53.954573, 90.000000, -57.643647]), [-0.197989899, -0.383251875, 0.022500000, -1.202335, 2.902453, -0.000000]],
        # Drop 3
        [np.radians([-115.046166, -94.704355, -121.089307, -54.206337, 90.000000, -70.046166]), [-0.288499567, -0.359210245, 0.022500000, -1.202335, 2.902453, -0.000000]],
        # Drop 4
        [np.radians([-105.773672, -96.738190, -118.784942, -54.476868, 90.000000, -60.773672]), [-0.231223917, -0.416485894, 0.022500000, -1.202335, 2.902453, 0.000000]],
        # Drop 5
        [np.radians([-116.907609, -100.666746, -114.068567, -55.264686, 90.000000, -71.907609]), [-0.321733585, -0.392444264, 0.022500000, -1.202335, 2.902453, -0.000000]],
        # Drop 6
        [np.radians([-108.364526, -102.425720, -111.846417, -55.727863, 90.000000, -63.364526]), [-0.264457936, -0.449719913, 0.022500000, -1.202335, 2.902453, -0.000000]],
        # Drop 7
        [np.radians([-118.451024, -106.378003, -106.614325, -57.007672, 90.000000, -73.451024]), [-0.354967604, -0.425678282, 0.022500000, -1.202335, 2.902453, -0.000000]],
        # Drop 8
        [np.radians([-110.541762, -107.947393, -104.448336, -57.604271, 90.000000, -65.541762]), [-0.297691955, -0.482953932, 0.022500000, -1.202335, 2.902453, -0.000000]],
    ]

    # Main sequence
    try:
        gripper_activation()
        gripper(True)

        a = [] # empty array for user input

        b_input = "" # The amount of faulty modules decided by the user
        while not (b_input.isdigit() and 0 <= int(b_input) <= 8):
            b_input = input("How many items do you want to enter? (1-8): ")
            if not (b_input.isdigit() and 0 <= int(b_input) <= 8):
                print("Invalid choice! You must enter a number between 1 and 8.")

        b = int(b_input)

        # The loop runs only until the list reaches the desired size 'b'
        while len(a) < b:
            user_input = input(f"Enter item {len(a) + 1} (1-8): ")

            if user_input.isdigit() and 0 <= int(user_input) <= 8:
                a.append(int(user_input))
            else:
                print("Invalid choice! Input must be a whole number between 1 and 8.")

        print(f"Sequence accepted: {a}")
        time.sleep(2)

        home()
        lid() #To simulate a real visual system the lid should be removed before getting user input

        for sequence_step, i in enumerate(a):
            if sequence_step >= len(drop_sequence_positions):
                print(f"Error: Not enough positions defined for step {sequence_step + 1}!")
                break

            approach_pose = drop_sequence_positions[sequence_step][0]
            drop_pose = drop_sequence_positions[sequence_step][1]

            if i ==1:
                module_1()
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
                rob.movel(drop_pose, acc=a_l, vel=v_l, wait=True, threshold=None)
                gripper(True)
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
            elif i==2:
                module_2()
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
                rob.movel(drop_pose, acc=a_l, vel=v_l, wait=True, threshold=None)
                gripper(True)
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
            elif i==3:
                module_3()
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
                rob.movel(drop_pose, acc=a_l, vel=v_l, wait=True, threshold=None)
                gripper(True)
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
            elif i==4:
                module_4()
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
                rob.movel(drop_pose, acc=a_l, vel=v_l, wait=True, threshold=None)
                gripper(True)
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
            elif i==5:
                module_5()
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
                rob.movel(drop_pose, acc=a_l, vel=v_l, wait=True, threshold=None)
                gripper(True)
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
            elif i==6:
                module_6()
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
                rob.movel(drop_pose, acc=a_l, vel=v_l, wait=True, threshold=None)
                gripper(True)
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
            elif i==7:
                module_7()
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
                rob.movel(drop_pose, acc=a_l, vel=v_l, wait=True, threshold=None)
                gripper(True)
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
            elif i==8:
                module_8()
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)
                rob.movel(drop_pose, acc=a_l, vel=v_l, wait=True, threshold=None)
                gripper(True)
                rob.movej(approach_pose, acc=a_j, vel=v_j, wait=True, threshold=None)

        home() # return to neutral position after last movement

        print("Sequence complete.")

    except Exception as run_error:
        print(f"An error occurred during runtime: {run_error}")

    finally:
        rob.close()
        print("Disconnected safely from UR5.")


# Execution of program
disassemble()