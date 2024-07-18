from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Edge:
    # from
    f: int
    # to
    t: int

    def reversed(self):
        return Edge(self.t, self.f)
    def __str__(self) -> str:
        return f"{self.f} --> {self.t}"

if __name__ == '__main__':
    edge1 = Edge(1,2)
    edge2 = Edge(3,4)