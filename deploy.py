from ssmparameters import SSM_PARAMETERS
from subprocess import DEVNULL
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    for ssm_parameter in SSM_PARAMETERS:
        if ssm_parameter.get("value"):
            subprocess.check_call(["aws", "ssm", "put-parameter",
                                   "--name", ssm_parameter.get("name"),
                                   "--type", ssm_parameter.get("type"),
                                   "--value", ssm_parameter.get("value")], stdout=DEVNULL)
            logger.info("Added {} to SSM".format(ssm_parameter.get("name")))
        else:
            logger.error("Missing SSM Parameters")
            return
    logger.info("Installing Node Packages")
    subprocess.check_call(["npm", "install"])
    subprocess.check_call(["sls", "deploy", "-v"])


if __name__ == '__main__':
    main()
