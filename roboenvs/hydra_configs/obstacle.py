from dataclasses import dataclass, field
from typing import Any

@dataclass
class ObstacleConf:
    x_pos: float = 0.0
    y_pos: float = 0.0
    x_vel: float = 0.0
    y_vel: float = 0.0

@dataclass
class CircleConf(ObstacleConf):
    obs_type: str = 'circle'
    radius: float = 0.1



