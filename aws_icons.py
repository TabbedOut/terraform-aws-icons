"""
Annotate Terraform graphs with AWS icons.

Usage: Takes graphviz input from `terraform graph` on stdin and ouputs graphviz
to stdout.
"""
import os
import re
import sys


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

ICONS = {
    'aws_autoscaling_group': 'Compute_AmazonEC2_AutoScaling.png',
    'aws_db_instance': 'Database_AmazonRDS_RDSDBinstance.png',
    'aws_db_subnet_group': '',
    'aws_ebs_volume': 'Storage-Content-Delivery_AmazonEBS.png',
    'aws_elasticache_cluster': 'Database_AmazonElasticCache.png',
    'aws_elasticache_subnet_group': '',
    'aws_elb': 'Compute_ElasticLoadBalancing.png',
    'aws_iam_access_key': 'Security-Identity_AWSIAM_addon.png',
    'aws_iam_instance_profile': 'Security-Identity_AWSIAM.png',
    'aws_iam_role_policy': '',
    'aws_iam_user': '',
    'aws_iam_user_policy': '',
    'aws_launch_configuration': '',
    'aws_iam_role': 'Security-Identity_AWSIAM_role.png',
    'aws_instance': 'Compute_AmazonEC2_instance.png',
    'aws_route53_record': 'Networking_AmazonRoute53.png',
    'aws_s3_bucket': 'Storage-Content-Delivery_AmazonS3_bucket.png',
    'aws_security_group': '',
    'aws_volume_attachment': '',
}


def repl_func(matchobj):
    resource_type = matchobj.group(2)
    icon = ICONS.get(resource_type)
    if icon is None:
        sys.stderr.write('Unknown resource: {}\n'.format(resource_type))
    if not icon:
        return matchobj.group(0)

    return (
        'label = <<TABLE BORDER="0"><TR><TD><IMG SRC="{1}"/></TD><TD>{0}</TD></TR></TABLE>>,'
        .format(
            matchobj.group(1),
            os.path.join(BASE_DIR, 'icons', icon),
        )
    )


def main():
    text = sys.stdin.read()

    new_text = re.sub(r'label = "((aws_.+)\..+)",', repl_func, text)

    sys.stdout.write(new_text)


if __name__ == '__main__':
    main()
