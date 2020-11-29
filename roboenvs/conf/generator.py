from dataclasses import dataclass, field
from typing import List, Any

from hydra_configs.obstacle import ObstacleConf, CircleConf
from hydra_configs.obstacle_group import ObstacleGroupConf

# Maps located in 'path'
# These will be generated on.
maps = ['citymaps/berlin.png']

# Obstacle groups
# Describes parameterized collections of obstacles.
obstacle_groups = [
    ObstacleGroupConf(num=10,
                      obs=CircleConf(x_pos=2.0,y_pos=2.0,x_vel=1.0,y_vel=1.0),
                      pos_var=0.3,
                      vel_var=0.1
                     ),
    ObstacleGroupConf(num=2,
                      obs=CircleConf,
                     ),
                  ]
@dataclass
class EnvGeneratorConf:
    output_dir_name: str = 'envreps'
    envs_per_map: int = 2
    maps: List[str] = field(default_factory=lambda: maps) 
    obstacle_groups: List[ObstacleGroupConf] = field(default_factory=lambda: obstacle_groups)

