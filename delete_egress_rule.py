#By MuZakkir Saifi

# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the AWS REGION")

# this is the configration for the logger

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=REGION)


def del_rule(grp_id, grp_rule_ids):
 
    try:
        res = vpc_client.revoke_security_group_egress(
            GroupId=grp_id,
            SecurityGroupRuleIds=grp_rule_ids)

    except ClientError:
        logger_for.exception('Egress security group rule can not be deleted.')
        raise
    else:
        return res


if __name__ == '__main__':
    GRP_ID = input("Please enter the security group id")
    SECURITY_GROUP_RULE_ID =['sgr-0f7468cfded']
    logger_for.info(f'Please wait, We are removing a security group egress rule(s)...')
    rule = del_rule(GRP_ID, SECURITY_GROUP_RULE_ID)
    logger_for.info(
        f'Wow, Your security group egress rule(s) has been deleted: \n{json.dumps(rule, indent=4)}'
    )
