from __future__ import annotations
from edge import Edge
from dataclasses import dataclass

@dataclass
class WeightEdge(Edge):
    weight: float

    def reversed(self) -> WeightEdge:
        return WeightEdge(self.t, self.f, self.weight)

    def __lt__(self, other: WeightEdge) -> bool:
        return self.weight < other.weight

    def __str__(self):
        return f"{self.f} cost {self.weight} to {self.t}"


if __name__ == '__main__':
    weight_edge = WeightEdge(0, 1, 10.1)
    print(weight_edge)