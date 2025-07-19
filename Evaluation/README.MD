# Environments description

## Gridworld

In its original presentation, the GridWorld environment is a standard benchmark for Q-learning, 
familiar to most \ac{RL} developers. For the study we use a larger GridWorld environment consisting 
of a $n \times m$ rectangular  board/grid ($10\times 10$ in our implementation), in which each tile 
$(i,j)$ represents a specific state of the board. Tiles in the board may be  walls, which agents cannot 
cross, or have a special exit status for agents to exit the board and terminate the episode. Exit tiles 
give a reward (positive of 1 or negative of -1) to agents, as shown in in the figure. All tile 
types are unknown to the agent. The agent moves from a fixed starting point in the board, the top left 
corner at position $(0,0)$, searching for the goal state (i.e., exit states with positive reward of 1). The 
agent moves from state to state, avoiding  obstacles and undesired exit states (with a reward of -1).

![gridworld](https://github.com/larodriguez22/Flik_Experiments/blob/gh-pages/img/gridworld_example.png)

The implementation of GridWorld introduces a bug in the definition of the $\epsilon$ hyperparameter, 
which leads to undesired behavior in the probability with which actions are taken by the agent, 
promoting exploitation without learning. The undesired behavior is given as the $\epsilon$ value is too 
small (e.g., $0.1$) so that no or seldom exploration (taking a random action at each state) of the agent 
is allowed for the first couple of iterations. Afterwards, suing the epsilon decay strategy, the agent will 
consistently exploit the best action, which will be suboptimal if not wrong, to define its policy. This is 
an undesired behavior specially for training purposes as an agent should have a large probability to 
choose other actions and explore the grid. 

The objective of this task is that the study participants use <span style="font-variant:small-caps;">Flik</span> to navigate through the code and find 
out why the agent is not learning properly. Eventually, the participants should come out with the 
solution of increasing the value of $\epsilon$. 

## Rooms
The four rooms maze environment has a similar composition to GridWorld, consisting of a 
$13\times 13$ board/grid divided in $4$ sections (i.e., rooms), with walls between them, and a door 
opening to go from one room to another, as shown in the Figure. The agent's objective in this 
environment is to exit through the upper-left room (the green square door in tile $(0,3)$) in the fewest 
possible number of steps. Reaching the exit state gives a reward of $1$ to the agent, and no 
other action gives a reward to the agent. In each episode the agent starts from any valid position in the 
grid, e.g., the yellow square in the bottom-right room in the figure. 

![rooms](https://github.com/larodriguez22/Flik_Experiments/blob/gh-pages/img/rooms_example.png)

In this program, we introduced a bug in the implementation of the Bellman equation, exchanging the  
use of the the learning rate ($\alpha$) like:

- Original equation: $Q(s, a) \leftarrow (1-\alpha) Q(s, a) + \alpha \left( r + \gamma \max_{a'} Q(s', a') \right)$
- Erroneous equation implemented: $Q(s, a) \leftarrow  \alpha Q(s, a) + (1-\alpha) \left( r + \gamma \max_{a'} Q(s', a') \right)$

In the original equation, $(1-\alpha) Q(s, a)$ is the current value and $\gamma \max_{a'} Q(s', a')$ 
is the maximum reward that can be obtained from state $s'$. This means that if the learning rate is 
very small the calculation of the current value will give a larger importance to the previously observed 
Q-values, leading to very little to no changes of the calculated Q-value. The effect of this behavior is 
that the agent learns short steps towards the optimal policy. In the Q-learning formula, the learning rate 
$\alpha$ defines how much old $Q(s,a)$ estimates are revised based on the new information. The 
learning rate ensures that, over time, the algorithm balances past knowledge with current learning, 
gradually incorporating new information while retaining important aspects of previous learning. 
Changing the equation in this way will disrupt the algorithm's balancing of previous and new 
knowledge. Specifically, $(1-\alpha)$ scales the difference between the new estimate and the old 
estimate. This makes the new information less influential as $\alpha$ gets larger, while the old value 
gets re-scaled by $\alpha$,  which does not align with the expected behavior of a Q-learning update. 

The objective of this task is that the participants use <span style="font-variant:small-caps;">Flik</span> 
to navigate through the code and find out the reason why the agent is not learning properly, afterwards 
we expected the participant to figure out a solution adjusting the proper value to update the Q-learning 
equation.

## Driving assistant

The Driving Assistant environment focuses on an agent that must learn to drive, in a two lane road, by 
a given set of road rules. In this case, the agent is expected to learn to drive on the correct lane 
(determined by the reward), at the allowed speed, taking over slow traffic, and not crashing. 
The state of the environment is defines as a three tuple determined by the current speed of the vehicle, 
the current lane, and the proximity to the vehicle in front. To move in the environment, the agent has 
the following five possible actions to execute at every time-step: `straight`, 
`slow_down`, `speed_up`, `steer_left`, `steer_right`. Finally, the agent receives  
negative rewards for the undesired behavior, $-800$ for crashing or coming to a full stop, $-600$ for 
driving too fast (over the $60Km/h$ speed limit), $-600$ for driving too slow (under $50Km/h$), 
$-500$ for driving on the wrong lane (the driving lane is the right lane of the road in our example). 
Additionally, the agent receives a reward of $50$ whenever there is no car in front.

Unlike the previous environment, study participants have not interacted with similar environments, 
not being a grid-based environment like GridWorld. Additionally, this environment is not episodic, as 
the vehicles can continuously drive. Nonetheless, the execution finishes and is immediately restarted 
upon a crash. The figure shows the visual interface of this environment, where the 
agent's vehicle corresponds to the blue rectangle on top, and driving traffic is represented by red 
rectangles appearing either at the right lane (the driving lane at bottom of the interface), or the left lane 
(top of the interface).

![assistant](https://github.com/larodriguez22/Flik_Experiments/blob/gh-pages/img/cars_example.png)

The bug introduced in this application is in the reward function, not motivating the agent to drive at 
the speed limit. The policy learned by the agent emerges as going very slowly or stopping altogether 
to avoid crashes, which is not the expected behavior. 

The objective of this task is that participants explore the program using 
<span style="font-variant:small-caps;">Flik</span> and observe the behavior 
of the reward and update it so that the agent can learn to drive appropriately as expected.
This is the largest task for the participants to analyze with <span style="font-variant:small-caps;">Flik</span>. 
