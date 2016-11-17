# Cracking the Coding Interview Challenges

Coding problems from Cracking the Coding Interview

## Queues: A Tale of Two Stacks

**file**: queues_using_two_stacks.cpp

**What is a Queue?** A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

* Enqueue: add a new element to the end of the queue.
* Dequeue: remove the element from the front of the queue and return it.
* In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:
	* 1 x: Enqueue element  into the end of the queue
	* 2: Dequeue the element at the front of the queue
	* 3: Print the element at the front of the queue

Input Format

The first line contains a single integer, q, denoting the number of queries. 
Each line i of the q subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query type, but only query 1 is followed by an additional space-separated value, x, denoting the value to be enqueued.
