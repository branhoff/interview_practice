"""
## Maximize Capital
A busy investor with an initial capital, `c`, needs an automated investment
program. They can select `k` distinct projects from a list of `n`  projects with
corresponding capitals requirements and expected profits. For a given project
`i`, its capital requirement is `capitals[i]`,and the profit it yields is
`profits[i]`.

The goal is to maximize their cumulative capital by selecting a maximum of `k`
distinct projects to invest in, subject to the constraint that the investor’s
current capital must be greater than or equal to the capital requirement of all
selected projects.

When a selected project from the identified ones is finished, the pure profit
from the project, along with the starting capital of that project is returned to
the investor. This amount will be added to the total capital held by the
investor. Now, the investor can invest in more projects with the new total
capital. It is important to note that each project can only be invested once.

As a basic risk-mitigation measure, the investor wants to limit the number of
projects they invest in. For example, if `k` is $2$, the program should identify
the two projects that maximize the investor’s profits while ensuring that the
investor’s capital is sufficient to invest in the projects.

Overall, the program should help the investor to make informed investment
decisions by picking a list of a maximum of k distinct projects to maximize the
final profit while mitigating the risk.

**Constraints**
- $1 \leq$ `k` $\leq 10^3$
- $0 \leq$ `c` $\leq 10^9$
- $1 \leq$ `n` $\leq 10^3$
- `k` $\leq$ `n`
- `n` $==$ `profits.length`
- `n` $==$ `capitals.length`
- $0 \leq$ `profits[i]` $\leq 10^4$
- $0 \leq$ `capitals[i]` $\leq 10^9$
"""
from heapq import heappush


def maximum_capital(c, k, capitals, profits):
  capitals_min_heap = []

  for x in range(0, len(capitals)):
    heappush(capitals_min_heap, (capitals[x]))

  return capitals_min_heap


def print_capitals_min_heap(capitals):
  arr = []
  for i in range(len(capitals)):
    arr.append(capitals[i])
    print("\t", arr)


def main():
  input = (
    (1, 2, [1, 2, 2, 3], [2, 4, 6, 8]),
    (2, 3, [1, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
    (1, 3, [1, 2, 3, 4], [1, 3, 5, 7]),
    (7, 2, [6, 7, 8, 10], [4, 8, 12, 14]),
    (2, 4, [2, 3, 5, 6, 8, 12], [1, 2, 5, 6, 8, 9])
  )
  num = 1
  for i in input:
    print(f"{num}.\tGiven Capitals: {i[2]}")
    print("\tAdding capital values...")
    capital = maximum_capital(i[0], i[1], i[2], i[3])
    print_capitals_min_heap(capital)
    print("-" * 100, "\n")
    num += 1


if __name__ == "__main__":
  main()
