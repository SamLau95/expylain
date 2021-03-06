# `expylain`

`expylain` is a Python package for Jupyter notebooks that enables rapid
interactive exploration of random processes. It is designed for ease-of-use in
learning contexts.

## Example

`expylain` works by taking `Data` and defining `Step`s that work on the data.
Each `Step` is just a Python function that takes in data from the previous
`Data` or `Step`. `Data` and its `Steps` are grouped in a `Process`.

For example, to flip a coin that lands heads with probability `p`:

```python
from random import random

def flip(coin, p=0.5):
    return coin[0] if random() < p else coin[1]

Process([
    Data(['H', 'T']),
    Step(flip),
])
```

**Output:**

```
Data: ['H', 'T']
          |
    flip  |
          v
         'H'

       [Rerun]
```

The real power of `expylain` results when using its built-in support for
interactive functions:

```python
Process([
    Data(['H', 'T']),
    # Specify a (start, end, step) for the arg p
    Step(flip, p=(0, 1, 0.1)),
])
```

**Output:**

```
Data: ['H', 'T']
          |
    flip  | p: 0 --- | ---- 1  [0.5]
          |
          v
         'H'

       [Rerun]
```

This allows you to interact and visualize random processes:

```python
from random import choices
from bqplot import pyplot as plt

def flip_n(coin, p=0.5, n=100):
    return choices(coin, weights=[p, 1-p], k=n)

def plot_flips(flips):
    heads, tails = flips.count('H'), flips.count('T')
    plt.bar(['H', 'T'], [heads, tails])

Process([
    Data(['H', 'T']),
    Step(flip_n, p=(0, 1, 0.1), n=(50, 500, 50)),
    Step(plot_flips),
])
```

**Output:**

```
Data: ['H', 'T']
          |
  flip_n  | p:  0 --- | --- 1    [0.5]
          | n: 50 --- | --- 500  [100]
          |
          v
 ['H', 'T', ..., 'H']
          |
plot_flips|
          v

      <bar_chart>

       [Rerun]
```

Processes can be composed, giving high expressivity. The `Repeat` constructor
allows the output of multiple runs of a process to become an input to a next
step:

```python
def count_heads(flips):
    return flips.count('H')

heads_in_n_flips = Process([
        Data(['H', 'T']),
        Step(flip_n, p=(0, 1, 0.1), n=(50, 500, 50))
        Step(count_heads)
    ],
    name='heads_in_n_flips',
)

distribution_of_heads = Process([
    Repeat(heads_in_n_flips, times=1000),
    Step(plt.hist),
])
```

**Output:**

```
+-------------------------------------------+
|   Data: ['H', 'T']                        |
|             |                             |
|     flip_n  | p:  0 --- | --- 1    [0.5]  |
|             | n: 50 --- | --- 500  [100]  |
|             |                             |
|             v                             | heads_in_n_flips
|    ['H', 'T', ..., 'H']                   |
|             |                             |
| count_heads |                             |
|             v                             |
|             48                            |
+-------------------------------------------+
              |
 Repeat(1000) |
              v
      [48, 49, ..., 50]
              |
              |
              v
          <histogram>

           [Rerun]
```

## Getting Started

Run these commands in your terminal to install `expylain` and its Jupyter
extension:

```
pip install expylain
jupyter nbextension enable --py --sys-prefix expylain
```
