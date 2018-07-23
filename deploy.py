from ssmparameters import SSM_PARAMETERS

import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SSM_COMMAND = "aws ssm put-parameter --name {} --type {} --value {}"
SERVERLESS_COMMAND = "serverless deploy"


def main():
    for ssm_parameter in SSM_PARAMETERS:
        if ssm_parameter.get("value"):
            os.system(SSM_COMMAND.format(ssm_parameter.get("name"),
                                         ssm_parameter.get("type"),
                                         ssm_parameter.get("value")))
            logger.info("Added {} to SSM".format(ssm_parameter.get("name")))
        else:
            logger.error("Missing SSM Parameters")
            return


if __name__ == '__main__':
    main()
