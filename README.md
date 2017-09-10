# Exercise 2 - Writing scripts and using GitHub
The exercise for this week is meant to help you better understand data types and lists in Python, and practice saving files to GitHub.
Below you have a series of "problems" in which you will be asked to solve by either downloading and modifying a starter script, or creating a new script file.
After making you changes, you will need to upload them to GitHub.
The answers to the questions in this week's exercise should be given by modifying the end of this document in the [section titled Answers](#answers).

Don't forget to check out the [hints for this week's exercise](https://geo-python.github.io/2017/lessons/L2/exercise-2-hints.html) if you're having trouble.

Scores on this exercise are out of **20 points**.

## Problem 1 - Making changes to a file in GitHub (*7 points*)
Your first task for this week is to make some modifications to the broken script [`station_ages.py`](station_ages.py) that is included in this week's exercise.
The script should allow users to find the age of an [FMI observation station](http://en.ilmatieteenlaitos.fi/observation-stations) by setting the `selectedStation` variable.
Don't worry about the case of a user entering a station name that is not on the list.

**Your score on this problem will be based on**

- Fixing **3 major code problems** to get this script working as expected
- Committing each change separately to GitHub without changing the script filename
- Listing the changes you needed to make to get the code working in plain English at the end of this file (see [Problem 3](#problem-3) below).

## Problem 2 - Creating and uploading a script to GitHub (*9 points*)
The table below presents [monthly average temperatures recorded at the Helsinki Malmi airport](https://www.timeanddate.com/weather/finland/helsinki/climate).

| Month     | Temperature [°C] |
| --------- | :--------------: |
| January   | -3.5             |
| February  | -4.5             |
| March     | -1.0             |
| April     | 4.0              |
| May       | 10.0             |
| June      | 15.0             |
| July      | 18.0             |
| August    | 16.0             |
| September | 11.5             |
| October   | 6.0              |
| November  | 2.0              |
| December  | -1.5             |

Create a script called `average_temps.py` that allows users to select a month and have the monthly average temperature printed to the screen.
For example, if the user sets month to "March", the script will display

```
The average temperature in Helsinki in March is -1.0
```
**Your score on this problem will be based on**

- Having your script display the monthly average temperature in a selected month, set by defining the variable `selectedMonth` near the top of the script.
- Having it work for all 12 months in the year.
- Using the basic script format described in [this week's lesson](https://geo-python.github.io/2017/lessons/L2/writing-scripts.html).
- Including comments that explain what most lines in the code do
- Uploading your script to your GitHub repository for this week's lesson with the name `average_temps.py`.
- Your answers to the three questions about the challenges you faced in writing your own script (see [Problem 3](#problem-3) below).

## Problem 3 - Answering questions using Markdown (*4 points*)
The last task in this week's exercise is to make some changes to this `README.md` file to provide answers to the following questions.

1. Under the heading for Problem 1 (`## Problem 1`), list the changes you needed to make to the code (in regular English, not Python code) to get it working.
You are welcome to use a numbered list if you like.
You can read about how to format numbered lists on the GitHub page about [GitHub-flavored Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/).
2. Add a heading for Problem 2 and beneath it list some of the challenges you faced in creating your own Python script from scratch.
What parts of the code were most difficult to create?
What things were you able to take from other resources in this week's lesson?
Any other comments about the difficulties in creating your own script?
3. Add a heading for Problem 3 and beneath it give your comments about this week's lesson.

    - What did you like?
    - What did you dislike?
    - What would you change?
4. Lastly, just for fun, add an image of an animal that you like along with a short caption giving its name and anything special you might like to add.
You can add an image by linking to a website, or by uploading an image to your GitHub repository and linking to that.
Since we've spoken briefly about software licencing, we suggest that you search for images in a repository that includes licencing information such as [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) or [Pixabay](https://pixabay.com/).
You are, of course, also welcome to upload your own animal images.
You can add it under the Problem 3 heading in the answers.

**Your score on this problem will be based on**

- Your answers to the three questions in part 3 of this problem
- Posting an image of a favorite animal using Markdown

# Answers
## Problem 1
This is some text.
You can use *italics* or **bold** text easily.
You may want to read a bit more about [formatting text in Github-flavored Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/).
You can see an example of how to display an image with a caption below.

![Text shown if image does not load](Images/green-tree-python.jpg)<br/>
*Figure 1: A green tree python*

Here is a bit more text beneath the image. Have fun!
