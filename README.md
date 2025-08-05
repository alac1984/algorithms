# Algorithms

> "Premature optimisation is the root of all evil." — *Donald Knuth*

Welcome to my **Algorithms Laboratory**. This repository hosts my personal implementations of classic algorithms alongside problem‑specific solutions where each algorithm played a decisive role.

I keep this repo public so potential employers (that might be you!) can see how I think, code, test, and document my learning journey.

---

## 📁 Repository layout

```text
algorithms/
├── merge_sort/              # Algorithm folder
│   ├── implementation/      # Clean, reusable versions of the algorithm
│   │   └── merge_sort.py
│   ├── counting_inversions/ # Problem solved with merge sort
│   │   ├── README.md        # Problem statement, approach, complexity analysis
│   │   └── solution.py
│   └── ...
├── binary_search/
│   └── ...
└── README.md
```

* **One algorithm → one folder** at the repo root (e.g. `merge_sort`).
* **One problem → one sub‑folder** inside the algorithm directory.
* **`implementation/`** keeps generic, unit‑tested versions of the algorithm separated from problem‑specific code.

---

## 🚀 Getting started

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-user>/algorithms.git
   cd algorithms
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   .venv\\Scripts\\activate         # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > Dependencies are minimal (usually just `pytest` and `mypy`).

4. **Run tests**

   ```bash
   pytest
   ```

---

## 🧰 Tech & practices

| Area          | Stack / Approach                                                                   |
| ------------- | ---------------------------------------------------------------------------------- |
| Languages     | Primarily **Python 3.12**; occasionally C++ or Java for benchmarks                 |
| Code style    | [PEP 8](https://peps.python.org/pep-0008/) + [Black](https://github.com/psf/black) |
| Static typing | [`mypy`](https://mypy-lang.org/) in *strict* mode                                  |
| Testing       | `pytest` with ≥90 % coverage                                                       |
| CI/CD         | GitHub Actions (lint, type‑check, tests)                                           |

---

## 🗺️ Roadmap

* [ ] Add **Quick Sort**, **Dijkstra’s algorithm**, and **Fenwick Tree**
* [ ] Benchmark section comparing theoretical vs. empirical performance
* [ ] Blog posts breaking down each algorithm step‑by‑step

Feel free to open issues or pull requests—even typo fixes are appreciated!

---

## 📜 License

[MIT](LICENSE) – study, modify, and share freely.

---

## 👤 Author

**André Carvalho**
Developer • Educator • Algorithms & Data‑Science Enthusiast
📫 [LinkedIn](https://www.linkedin.com/in/andrecarvalho) • [Twitter](https://twitter.com/<your-user>)

> Feedback is welcome! Open an issue or send me a message.
