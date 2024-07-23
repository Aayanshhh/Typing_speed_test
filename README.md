# Typing Speed Test

A typing speed test application built with Python's `tkinter` library. This application challenges users to type words as quickly as possible while tracking their typing speed and accuracy. The game features a modern, styled interface for an improved user experience.

## Features

- **Timed Test**: 60-second timer to measure typing speed.
- **Word Display**: Words are presented for typing.
- **Score Tracking**: Tracks the number of correct words typed out of total attempts.
- **Stylish Interface**: Modern and visually appealing design with customized buttons and fonts.
- **Start and Exit**: Start the test and exit the application with intuitive buttons.

## Controls

- **Start Button**: Begin the typing test.
- **Enter Key**: Submit typed words for checking.
- **Exit Button**: Quit the application.



## Gameplay

1. **Start the Test**: Click the 'Start' button to begin the 60-second typing test.
2. **Type the Words**: Type the words displayed in the text area as quickly and accurately as possible.
3. **Score**: Your score will be displayed as the number of correct words typed out of the total number of attempts.
4. **Game Over**: The test ends after 60 seconds. The input field will be disabled, and the final score will be displayed.
5. **Restart or Exit**: Click the 'Exit' button to quit the application.

## Code Overview

- **Initialization**: Sets up the main window and styling using `tkinter`.
- **Timer**: Manages the 60-second countdown and disables input at the end.
- **Word Display**: Fetches and displays words for typing.
- **Input Checking**: Validates user input against the displayed words.
- **Score Tracking**: Updates and displays the user's score.

### Code Structure

- **`fetch_words`**: Dummy function to simulate fetching words from an API.
- **`start_timer`**: Starts and updates the countdown timer.
- **`get_words`**: Fetches words and initiates the typing test.
- **`check_word`**: Validates typed words and updates the score.
- **`stop_exit`**: Stops the timer and exits the application.

## Dependencies

- Python 3.x
- `tkinter` (included with Python)



