# Pomodoro Timer with Background Music

This is a Pomodoro Timer application with the ability to play background music during the Pomodoro sessions. The timer follows the Pomodoro Technique which involves working in 25-minute intervals, separated by short breaks. After completing four Pomodoro sessions, a long break is taken.

## Installation and Usage

To use this application, you will need to have Python 3.7 or above installed on your computer. Clone this repository and install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

Then, run the following command to start the Streamlit application:

```bash
streamlit run app.py
```

Once the application has started, you will be prompted to upload an MP3 file for the background music. Then, enter the length of the Pomodoro session, short break, long break, and the number of Pomodoro sessions before a long break.

Click on the "Start Pomodoro Timer" button to start the timer. The timer will display the remaining time for the current Pomodoro session, short break, or long break. The timer will automatically switch between Pomodoro sessions and breaks as per the configuration.

You can reset the timer at any time by clicking the "Reset Timer" button.

## Code

This application is built using the `streamlit` library in Python. The `pomodoro_timer` function is the core of the application, which takes in the length of the Pomodoro session, short break, long break, and the number of Pomodoro sessions before a long break as inputs.

The `countdown` function is used to display the remaining time for the current Pomodoro session, short break, or long break.

The `HTML` module from the `IPython.display` library is used to update the timer text dynamically. The `time` module is used to pause the execution of the program for one second to update the timer text.

The `st.file_uploader` and `st.audio` functions from the `streamlit` library are used to upload and play the background music.

The `st.markdown` function is used to add a background image to the application.

## Demo

You can try out the application at https://deepankarvarma-pomodoro-timer-using-python-app-f6yooi.streamlit.app/
