
# Automated Faculty Feedback Form Filler for Amizone

_WHO DOESEN'T HATE FILLING AMIZONE FACULTY FEEDBACK FORMS???_
### Don't Worry I Got You Covered! ;)

This Python script automates the process of filling out faculty feedback forms on the Amizone student portal (Amity University). It is designed to save time and reduce effort during semester-end evaluations by automating repetitive tasks. 

### It takes less than *5 minutes* to fill feedback for all Faculties using this Bot.

## Features

- **Exclusive to Amity University**: Specifically tailored for the Amizone.net student portal.
- **Customizable Responses**: Choose individual feedback responses (e.g., "agree," "neutral," "disagree","strongly-disagree") for each faculty member.
- **Automated Feedback Submission**: Fills in and submits the feedback form for a selected faculty member in seconds.
- **Step-by-Step Execution**: Works one faculty member at a time, requiring manual switching to the next feedback form.

## How It Works

1. Login to Amizone: Visit [Amizone.net](https://s.amizone.net/) and log in using your credentials.
2. Navigate to the Feedback Form: From the left-hand sidebar, open the **My Faculty** section and select the feedback form for a specific faculty member.
3. Run the Script: Open a terminal and execute the script using Python. Enter your feedback choice when prompted (e.g., "agree," "neutral," "disagree"). Switch back to the browser within **5 seconds** of running the script.
4. Automation in Action: The script will automatically scroll, select responses, and submit the feedback.
5. Repeat: Execute the script again for the next faculty member's feedback form.

## Installation and Setup

### Prerequisites

- **Python Version**: Ensure Python 3.6+ is installed on your system. [Download Python](https://www.python.org/downloads/).
- **Supported Operating System**: Windows. (_For my fellow *Linux and Apple* users skip the winsound library installation and use the Linux Script_)
- **Python Libraries**: The script uses the following libraries:
  - `pyautogui`: For automating mouse clicks and scrolling.
  - `winsound`: For audio feedback (built into Python on Windows).

### Installation Steps

1. Clone this repository or download the script file:
   ```bash
   git clone https://github.com/nexiouscaliver/amizone-faculty-feedback-bot.git
   ```
2. Install the required Python dependencies:
   ```bash
   pip install pyautogui
   ```
3. Verify the setup by running:
   ```bash
   python --version
   ```

## Usage Instructions

1. Open the feedback form for a specific faculty member on the Amizone.net portal.
2. Run the script using the following command:
   ```bash
   python auto-faculty-feedback-amizone.py
   ```
3. Enter your feedback choice when prompted:
   - Options: `agree`, `neutral`, `disagree`, `strongly-disagree`.
4. Switch back to the browser within **5 seconds** and wait for the script to complete filling the form. DO NOT PANIC as it will control your mouse for a while
5. Repeat the process for each faculty member.

## System Requirements

- **Operating System**: Windows, Linux, Mac.
- **Python Version**: 3.6 or higher.
- **Dependencies**: `pyautogui`.

### How to Install Python

1. Download Python from [python.org](https://www.python.org/downloads/).
2. Run the installer and check the option "Add Python to PATH."
3. Verify the installation by running:
   ```bash
   python --version
   ```

## Video Demonstration

[Demo Video](#)  
*To be available soon*

## Repository Description

This repository provides a script to automate the submission of faculty feedback forms on Amizone.net. By automating repetitive tasks, it reduces the effort and time required to complete semester-end evaluations. The script allows users to customize feedback responses for each faculty member and runs seamlessly on Windows systems.

## Disclaimer

- **Manual Execution for Each Faculty**: The script requires manual execution for each faculty member.
- **Browser Interaction Required**: Ensure the browser is active with the correct feedback form before running the script.
- **Exclusivity**: Designed solely for use on the Amizone.net platform.

Enjoy automating your feedback submissions and saving valuable time!

## License

MIT ;)

**Free Software For My Fellow Mates, Hell Yeah!**
