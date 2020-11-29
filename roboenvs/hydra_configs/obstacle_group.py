from dataclasses import dataclass, field
from typing import Any
from hydra_configs.obstacle import ObstacleConf, CircleConf

@dataclass
class ObstacleGroupConf:
    num: int = 200
    distribution: str = 'normal'
    pos_var: float = 0.0 
    vel_var: float = 0.0 
    obs: ObstacleConf = CircleConf 



