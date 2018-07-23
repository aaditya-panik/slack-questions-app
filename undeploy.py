from ssmparameters import SSM_PARAMETERS
from subprocess import DEVNULL

import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info("Removing all resources from AWS")
    subprocess.check_call(["sls", "remove", "-v"])
    for ssm_parameter in SSM_PARAMETERS:
        subprocess.check_call(["aws", "ssm", "delete-parameter",
                               "--name", ssm_parameter.get("name")], stdout=DEVNULL)
        logger.info("Removed {} from SSM".format(ssm_parameter.get("name")))


if __name__ == '__main__':
    main()
