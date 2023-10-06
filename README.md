# ROS2 Teleoperation Package - `pkg_tele_1`

This ROS2 package, `pkg_tele_1`, provides teleoperation functionalities using keyboard inputs.

## Prerequisites

- ROS2 Foxy or later
- Ubuntu 20.04 or equivalent environment

## Directory Structure

```
.
├── build
│   ├── COLCON_IGNORE
│   ...
├── install
│   ├── COLCON_IGNORE
│   ...
├── log
│   ├── build_2023-10-06_13-02-49
│   ...
├── requirments.txt
└── src
    └── pkg_tele_1
        ├── launch
        ├── package.xml
        ├── pkg_tele_1
        ├── resource
        ├── setup.cfg
        ├── setup.py
        └── test
```

## Installation & Setup

1. Navigate to the workspace's `src` directory:
```bash
cd ~/ros2_ws/src/
```

2. Clone the repository from GitHub:
```bash
git clone [REPOSITORY_URL]
```

3. Build the workspace using `colcon`:
```bash
colcon build
```

4. Source the setup script to update your ROS2 environment:
```bash
source ~/ros2_ws/install/setup.bash
```

## Usage

To start the teleoperation using the provided launch file:
```bash
ros2 launch pkg_tele_1 launch_tele_1.py
```

## Contributing

Pull requests and contributions are welcome. For significant changes, discuss via issues before making a pull request.

## License
Please refer to the license file in the repository.
