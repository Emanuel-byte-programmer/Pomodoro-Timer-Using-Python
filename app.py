import streamlit as st
import time

# Set default timer values
pomodoro_time = 25
short_break_time = 5
long_break_time = 15

# Define function for Pomodoro timer
def pomodoro_timer(minutes):
    st.write(f"Time remaining: {minutes} minutes")
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        st.write(timer)
        time.sleep(1)
        seconds -= 1
    st.write("Time's up!")

# Define Streamlit app
def main():
    st.title("Pomodoro Timer")
    st.write("Select the timer duration below:")

    # Get user input for timer durations
    pomodoro_time = st.slider("Pomodoro time (minutes)", 1, 60, 25, 1)
    short_break_time = st.slider("Short break time (minutes)", 1, 60, 5, 1)
    long_break_time = st.slider("Long break time (minutes)", 1, 60, 15, 1)

    # Define button for starting Pomodoro timer
    if st.button("Start Pomodoro"):
        pomodoro_timer(pomodoro_time)
        st.write("Take a short break!")
        time.sleep(short_break_time * 60)
        st.write("Time for another Pomodoro!")
        pomodoro_timer(pomodoro_time)
        st.write("Take a short break!")
        time.sleep(short_break_time * 60)
        st.write("Time for another Pomodoro!")
        pomodoro_timer(pomodoro_time)
        st.write("Take a long break!")
        time.sleep(long_break_time * 60)
        st.write("Time to start again!")

if __name__ == "__main__":
    main()
