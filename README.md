# PA1473 - Software Development: Agile Project (Template)

## Template information
This template should help your team write a good readme-file for your project. (The file is called README.md in your project directory.)
You are of course free to add more sections to your readme if you want to.

Readme-files on GitHub are formatted using Markdown. You can find information about how to format using Markdown here: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Your readme-file should include the following sections:


## Introduction

This is the EV3 sortning system for the Robot Arm H25


## Getting started
How to set up the project steps

1. Hardware Requirements: Ensure that you have the LEGO EV3 Robot arm H25 

2. Software Requirements: Make sure you have the following software installed: 
    - Install Python 3.6.0 or higher with PIP
    - Install an Editor to run python
    -  Install the required version of the LEGO EV3 MicroPython firmware on your EV3 Brick. Refer to the user guide on the EV3 extension tab for detailed instructions.

3. Project Setup: Set up your project by performing the following steps:

    - Create a new directory or clone the existing project repository.

    - Place the provided Python code file (containing the code you shared earlier) in your project directory.

4. Dependency Installation: Install the necessary dependencies by following these instructions:

    -   Open a command-line interface or terminal.

    - Paste the following into the terminal: pip install pybricks

    - This will install the Pybricks library, which is required to interact with the LEGO EV3 hardware components.

5. Hardware Connection: Ensure that your LEGO EV3 hardware components are properly connected to your computer or development environment. Follow the hardware setup instructions provided by LEGO for connecting the EV3 Brick to your system.

6. Code Execution: Now that your project is set up and dependencies are installed, you can execute the code by following these steps:

    - Run the provided Python code file using a Python interpreter compatible with LEGO EV3 MicroPython. You can use an integrated development environment (IDE) or execute the code through the command line.

    - Ensure that your LEGO EV3 Brick is turned on and connected to your computer.

    - Execute the code and observe the behavior of the EV3 robot based on the programmed instructions.



## Building and running

1. The project is simple to run just upload the code to the EV3 and run.

2. If you want to change pickup location change the list at line 24

3. If you want to change drop off location change the dict at line 26

4. Adjusting Claw Sensitivity

Sometimes, the claw may fail to open or close properly due to variations in the thresholds of different robots. To change the sensitivity of the open and close functions, follow these steps:

Locate line 68 in the code.

Modify the integer value on this line to adjust the sensitivity. Increasing the value makes the claw less sensitive, while decreasing it makes the claw more sensitive.

To determine the appropriate threshold for your specific robot, perform a test run.

During the test run, observe the behavior of the claw and check the debug menu for any returned values.

By adjusting the sensitivity, you can fine-tune the claw's operation to ensure proper opening and closing on your particular robot.

Note: The specific line number mentioned (line 68) is provided as an example. Please refer to your code and adjust the value accordingly.


## Features

Lastly, you should write which of the user stories you did and didn't develop in this project, in the form of a checklist. Like this:

- [x] US_1: As a customer, I want the robot to pick up items
- [x] US_1B: As a customer, I want the robot to pick up items from a designated position.

- [x] US_2: As a customer, I want the robot to drop off items
- [x] US_2B: As a customer, I want the robot to drop items off at a designated position.

- [x] US_3: As a customer, I want the robot to be able to determine if an item is present at a given location.

- [x] US_4: As a customer, I want the robot to tell me the color of an item.

- [x] US_5: As a customer, I want the robot to drop items off at different locations based on the color of the 
 item.

- [ ] US_6: As a customer, I want the robot to be able to pick up items from elevated positions. 

- [ ] US_7: Unknown

- [x] US_8: As a customer, I want to be able to calibrate items with three different colors and drop the items 
off at specific drop-off zones based on color.

- [x] US_9: As a customer, I want the robot to check the pickup location periodically to see if a new item has 
 arrived.

- [x] US_10: As a customer, I want the robots to sort items at a specific time. 

- [ ] US_11:  As a customer, I want two robots to communicate and work together on items sorting without 
 colliding with each other. 
 
- [ ] US_12: As a customer, I want to be able to manually set the locations and heights of one pick-up zone and two drop-off zones. (Implemented either by manually dragging the arm to a position or using buttons)     