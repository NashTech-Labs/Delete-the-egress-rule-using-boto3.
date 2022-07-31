# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def del_egress_rule(security_group_id, security_group_rule_ids):
 
    try:
        response = vpc_client.revoke_security_group_egress(
            GroupId=security_group_id,
            SecurityGroupRuleIds=security_group_rule_ids)

    except ClientError:
        logger.exception('Egress security group rule can not be deleted.')
        raise
    else:
        return response


if __name__ == '__main__':
    SECURITY_GROUP_ID = input("Please enter the security group id")
    SECURITY_GROUP_RULE_ID = input("Please enter the security group rule id")
    logger.info(f'Please wait, We are removing a security group egress rule(s)...')
    rule = del_egress_rule(SECURITY_GROUP_ID, SECURITY_GROUP_RULE_ID)
    logger.info(
        f'Wow, Your security group egress rule(s) has been deleted: \n{json.dumps(rule, indent=4)}'
    )