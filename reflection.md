# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The first thing that I noticed was the debugger view had the wrong information on it. The correct number in the view is incorrect. Also after you win the game's rest button doesn't work, so you need to refresh the page to start a new game. And the score increases on wrong guesses.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code to help me with identifying some of the bugs. For the first problem, I had already I identified that there was something wrong with the debugger, the warning messages, and the restart game button. I told Claude about them and it helped me identify other bugs that were present in the `main.py` file. Claude showed me that the guess check logic was inverted, so I was able to make the warning messages for wrong guesses accurate.
I don't think that the show hint button should be an option, since without it toggled you have no idea how close you are to the right answer. Also when it brought the helper functions into the `logic_utils.py` it didn't remove them from the `app.py` file so I had to remove the code and import the `logic_ultils.py`
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I used the coverage module in Python to evaluate the test coverage of my python `logic_utils.py`. I evaluated bugs based on the intent of the function. For example the casting ints to strings to comparison of int value, which clearly is a logic bug, so I fixed the logic with Claude and ensured that every other instances of code like that was refactored.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

When it comes to testing with a project that uses Streamlit you have to do seperate types of tests since Python doesn't really have good tools for testing a webpage, so you would have to implement intergration tests and see live builds to troubleshoot. While with the Python functions, you are easily able to test them with the convention testing frameworks that the Python ecosystem provides like unittest or pytest.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I wouldn't have an ai agent generate the entire codebase, since I would like to build it myself so that I have a better understanding of the code that I am working on. The sweeping changes that I allowed Claude to do on this project isn't something that I would do at work. What I really like about using Claude was having it scan the codebase for potential issues and being able to manually verifying them myself. Claude and other ai agents are best used a buddy to help you brainstorm and clean up code, but you should be the one driving the ship.
