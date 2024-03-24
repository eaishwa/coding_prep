"""
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/description/

What is the question?
Given CPU with tasks and cooldown period, determine least number of slots to finish all tasks.

Final algorithm followed:
1. Just a formula, determine num slots for the max freq task, thats the kinda upper limit
2. After that add extra slots for other max freq tasks
3. Set the minimum output to be len(tasks), you always need that time!

Summary of common mistakes/tricks:
Knowing step 3 is hard!
"""
# Solution with comments
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Greedy Approach
        # Compute max slots needed to just fill the max freq task
        # After that just add number of max freq tasks to it
        # set min output to be len(tasks)

        ctr = Counter(tasks)
        max_freq = max(list(ctr.values()))
        num_max_freq_tasks = 0
        for k,v in ctr.items():
            if v == max_freq:
                num_max_freq_tasks += 1

        return max((max_freq-1)*(n) + max_freq + num_max_freq_tasks-1,
        len(tasks))