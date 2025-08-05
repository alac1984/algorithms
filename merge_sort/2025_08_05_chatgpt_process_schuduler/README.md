### Problem — *Process Scheduler in Linked List* (medium level)

A microkernel maintains its **ready queue of processes** as a **singly linked list** (`LinkedList`).  
Each node stores two integers:

| Field | Meaning                                                         |
|-------|-----------------------------------------------------------------|
| `pid` | Unique process identifier (1 ≤ `pid` ≤ 10^9)                    |
| `prio`| Priority; **lower values = higher priority** (0 ≤ `prio` ≤ 10^5) |

When the scheduler runs, it **reorders** the list to prioritize higher-priority processes first.  
Sorting rules:

1. **Ascending priority** (lower `prio` comes first).
2. For equal priority, **ascending PID**.

Your challenge is to implement **in-place Merge Sort** for linked lists to sort this queue:

* ✅ **Time** `O(n log n)`
* ✅ **Extra space** `O(1)` beyond recursion stack (do not copy data to an array).
* ✅ **Stable** — if `prio` and `pid` are equal, preserve original relative order.

---

#### Input Format

```
n
pid₁ prio₁
pid₂ prio₂
…
pidₙ prioₙ
```

* `1 ≤ n ≤ 10⁵`

Processes are listed in arrival order (head = first line after `n`).

#### Output Format

Print the sorted list, **one node per line**, in the same format:

```
pid prio
```

from first to last node.

---

#### Example

**Input**

```
5
42 3
17 1
8  3
13 0
99 1
```

**Expected Output**

```
13 0
17 1
99 1
42 3
8  3
```

---

##### Notes

* You may define custom node/list classes/structures as long as constraints are met.
* Automated tests handle up to 100,000 nodes; solutions converting the list to an array or using `O(n)` extra space will fail.

---

**When finished, submit:**

1. Your complete code.
2. Brief explanation (max 10 lines) of your strategy and complexity analysis.

Good luck—I look forward to your solution!
