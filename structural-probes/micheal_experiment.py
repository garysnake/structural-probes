from run_experiment import setup_new_experiment_dir, execute_experiment
import yaml
import torch

# CHANGE PATH
CONFIG_FILE = '/home/garysnake/Desktop/structural-probes/experiments/config/bert_base_distance_cola.yaml'
EXPERIMENT_NAME = '/home/garysnake/Desktop/structural-probes/experiments/results/bert_base_distance_cola'
SEED = 123

class Object(object):
    pass

cli_args = Object()
cli_args.experiment_config = CONFIG_FILE
cli_args.results_dir = EXPERIMENT_NAME
cli_args.train_probe = True
cli_args.report_results = True
cli_args.seed = SEED

yaml_args = yaml.load(open(cli_args.experiment_config), Loader=yaml.FullLoader)
setup_new_experiment_dir(cli_args, yaml_args, cli_args.results_dir)

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
yaml_args['device'] = device

execute_experiment(yaml_args, train_probe=cli_args.train_probe, report_results=cli_args.report_results)