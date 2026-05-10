def job_scheduling(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    schedule = [None] * max_deadline

    for job in jobs:

        for j in range(job[1] - 1, -1, -1):

            if schedule[j] is None:
                schedule[j] = job[0]
                break

    return schedule

n = int(input("Enter number of jobs: "))

jobs = []

for _ in range(n):

    job_id = input("Enter Job ID: ")
    deadline = int(input("Enter Deadline: "))
    profit = int(input("Enter Profit: "))

    jobs.append((job_id, deadline, profit))

print("Job Schedule:")
print(job_scheduling(jobs))

#----------------------OUTPUT----------------------
Enter number of jobs: 4
Enter Job ID: A
Enter Deadline: 4
Enter Profit: 20
Enter Job ID: B
Enter Deadline: 1
Enter Profit: 10
Enter Job ID: C
Enter Deadline: 2
Enter Profit: 40
Enter Job ID: D
Enter Deadline: 1
Enter Profit: 30
Job Schedule:
['C', 'D', 'A', None]
