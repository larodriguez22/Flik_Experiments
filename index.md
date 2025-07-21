# <span style="font-variant:small-caps;">Flik</span>: A bug's life debugger

This online appendix presents the complete evaluation results for our work on debugging Reinforcement Learning (RL) programs with the <span style="font-variant:small-caps;">Flik</span> back-in-time debugger.

To evaluate <span style="font-variant:small-caps;">Flik</span> we have an empirical study with developers evaluating the debugger on 3 different programming tasks.

## Programming tasks

Currently there are 3 tasks in the evaluation of <span style="font-variant:small-caps;">Flik</span>:

1. Gridworld: An $n\times n$ matrix with two types of exit cells, traps (which give a bad reward to the agent) and exits (which give a positive reward to the agent). Additionally, there are blocked cells in which the agent cannot enter. The goal of the agent is to reach the exit cell.
1. Rooms: Is a grid-type environment with four smaller grids (a.k.a rooms) embedded into it. The rooms are connected through a door (an unblocked cell). The objective of the agent is to reach a specific point in the rooms (the exit in the top left room).
1. Driving Assistant: A two lane street where an agent must drive at the maximum speed, on the driving lane, overtaking slow driving vehicles, and without crashing.

The description of the three environments can be found [here](https://github.com/larodriguez22/Flik_Experiments/blob/main/Evaluation/README.MD).

## Empirical study

Our initial empirical study works consists of 27 participants who were asked to complete the three programming tasks. For each task the participants were asked to detect and fix the bug present in the implementation given to them.

In the case of Gridworld, the objective of the task is that the study participants use <span style="font-variant:small-caps;">Flik</span> to navigate through the code and find out why the agent is not learning properly. Eventually, the participants should come out with the solution of increasing the value of $\epsilon$.

In the case of Rooms, the objective of the task is that the participants use <span style="font-variant:small-caps;">Flik</span> to navigate through the code and find out the reason why the agent is not learning properly, afterwards we expected the participants to figure out a solution adjusting the proper value to update the Q-learning equation.

In the case of Driving Assistant, the objective of the task is that participants explore the program using <span style="font-variant:small-caps;">Flik</span> and observe the behavior of the reward and update it so that the agent can learn to drive appropriately as expected.

Finally the participants where asked to fill in a questionaire upon completing the tasks. The questionar was divided into three question groups. (1) General knowledge questions, (2) task questions, and (3) usability questions for the tool. for each of the question groups we present the questions and the obtained results.

The questionaire contains 23 multiple choice questions with a 5-points Likert scale, in which 5 means completely agree, and 1 means completely disagree. One of the questions was a yes or no question, to identify if the participants are willing to use the tool in the future. Finally, there are 10 open-answer questions, to dive deeper into feedback for the tool, and the tasks' complexity.

### 1. General knowledge

#### Questions

This section contains six questions, two of which contains 4 multiple choice questions, and two free text questions.

1. What is your experience using python?
1. Explain your experience using python
1. What is your experience using debuggers?
1. Explain your experience using debuggers
1. What is your experience using terminal?
1. What is your experience with Reinforcement Learning programs?

#### Results

Participant | What is your experience using python? | What is your experience using debuggers? | What is your experience using terminal? | What is your experience with Reinforcement Learning programs?
------ | ------ | ------ | ------ | ------
1	|	5	|	5	|	5	|	5
2	|	4	|	3	|	4	|	4
3	|	5	|	4	|	5	|	5
4	|	5	|	1	|	4	|	4
5	|	4	|	3	|	5	|	2
6	|	5	|	5	|	5	|	5
7	|	4	|	1	|	5	|	3
8	|	5	|	1	|	4	|	4
9	|	5	|	2	|	4	|	3
10	|	5	|	2	|	3	|	3
11	|	3	|	2	|	4	|	3
12	|	5	|	4	|	5	|	5
13	|	3	|	3	|	3	|	2
14	|	5	|	4	|	5	|	5
15	|	5	|	1	|	4	|	3
16	|	5	|	5	|	4	|	3
17	|	5	|	5	|	5	|	3
18	|	4	|	1	|	4	|	1
19	|	5	|	4	|	5	|	5
20	|	5	|	4	|	4	|	1
21	|	5	|	3	|	1	|	5
22	|	5	|	4	|	4	|	4
23	|	4	|	4	|	4	|	3
24	|	5	|	5	|	5	|	2
25	|	5	|	2	|	3	|	3
26	|	5	|	2	|	5	|	5
27	|	5	|	5	|	5	|	5

![python](./img/experience-python.png) | ![debugger](./img/experience-debuggers.png) | ![terminal](./img/experience-terminal.png) | ![rl](./img/experience-rl.png) |
--- | --- | --- | ---
Python experience | Debugger experience | Terminal experience | RL experience

### Task questions

Our second dataset is composed by different algorithms from the known domain of sorting. The objective of this evaluation is to assess the effectiveness of Out of Step to detect clones in small programs found in the wild.

Using a known domain enables us to validate the algorithms correctness, and to easily detect if the clones detected are true clones or false positives. This assessment is important to move forward to larger application domains with confidence about the validity of our results.

### Usability questions



<table>
<td> Algorithm </td> <td colspan=5> Languages (with LoC) </td>
<tr>
  <td>Bubble</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Heap</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Insertion</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Quick</td> <td> C++ </td> <td> Dart </td><td> Java <br> Java </td> <td> Kotlin <br> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Selection</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
<tr>
  <td>Shell</td> <td> C++ </td> <td> Dart </td><td> Java </td> <td> Kotlin </td> <td> Swift </td>
</tr>
</table>

Evaluation [results](./sorting.md)

**type** | **quantity** | **source of the repositories**
---- | ---- | ----
kotlin-dart | 50 | GitHub (4 Dart, 4 Kotlin), Students (21 Dart, 21 Kotlin)
kotlin-swift | 52 | GitHub (12 Kotlin, 12 Swift), Students (14 Kotlin, 14 Swift)
dart-swift | 14 | GitHub (3 Dart, 3 Swift), Students (4 Dart, 4 Swift)
