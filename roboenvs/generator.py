import os
import hydra
from omegaconf import OmegaConf
from pathlib import Path
import numpy
import csv

from hydra.core.config_store import ConfigStore
from conf.generator import EnvGeneratorConf

class EnvGenerator(object):
    def __init__(self, cfg):
        self.cfg = cfg
        self.output_dir = Path(hydra.utils.get_original_cwd()).parent.joinpath('envreps')
        self.output_dir.mkdir(parents=True, exist_ok=True) 
        self.envrep_dict = dict()

        print(f'[EnvGenerator] Output Dir: {self.output_dir.absolute()}')

    def generate_envreps(self):
        for m in self.cfg.maps:

            self.envrep_dict[m] = [] 
            for env_num in range(self.cfg.envs_per_map):

                obs_group_list = []
                for obs_group in self.cfg.obstacle_groups:         
                    distr = eval('numpy.random.'+obs_group.distribution)

                    obs_list = []
                    for obs_num in range(obs_group.num):
                        obs_dict = {
                            'type': 'circle',
                            'radius': 0.1,
                            'x_pos': round(distr(obs_group.obs.x_pos, obs_group.pos_var),3),
                            'y_pos': round(distr(obs_group.obs.y_pos, obs_group.pos_var),3),
                            'x_vel': round(distr(obs_group.obs.x_vel, obs_group.vel_var),3),
                            'y_vel': round(distr(obs_group.obs.y_vel, obs_group.vel_var),3),
                            }
                        obs_list.append(obs_dict)

                    obs_group_list.append(obs_list)

                self.envrep_dict[m].append(obs_group_list)

    def write_csvs(self):
            counter = 0
            for env in self.envrep_dict:
                env_name = env.split('.')[0].replace('/','-')
                for obs_group_list in self.envrep_dict[env]:
                    # write new file for every obs_group_list for each map
                    with open(self.output_dir.joinpath(f'{counter:03}_{env_name}.csv'), \
                    'w+', newline='') as outcsv:
                        writer = csv.writer(outcsv)

                        writer.writerow([env]) # first row writes the relative path/name of base map 
                        for obs_group in obs_group_list:
                            # get the keys and data for the first obs in this obs_group_list
                            # (all obstacles are same type)
                            key_list = obs_group[0].keys()
                            
                            # write obs group header
                            writer.writerow([str(k) for k in key_list])

                            # write obstacles
                            for obs in obs_group:
                                writer.writerow([str(obs[k]) for k in key_list])
                    counter += 1

from hydra.conf import HydraConf, RunDir

cs = ConfigStore.instance()
cs.store(name="config", node=EnvGeneratorConf)

# this line merges conf/config.yaml with the structured config above, 'config'
@hydra.main(config_path='conf', config_name='config')  
def main(cfg):
    print(OmegaConf.to_yaml(cfg))
    envgen = EnvGenerator(cfg)
    envgen.generate_envreps()
    envgen.write_csvs()
    print('Writing complete.')

if __name__ == '__main__':
    main()
