import boto3

# The following functions are exampleas of extracting only
# the relevant data for ec2 resourses monitoring

# returns list of instances statuses
def get_instance_status():

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instance_status()
    
    all_instances_status_list = []

    for status in response['InstanceStatuses']:

        instance_id = status['InstanceId']
        system_state = status['InstanceState']['Name']
        instance_status = status['InstanceStatus']['Status']

        instance_status_comlpete = {'id': instance_id, 'state': system_state, 'status': instance_status}

        all_instances_status_list.append(instance_status_comlpete)

        
    return all_instances_status_list


# get vpcs
def get_vpc():

    ec2_client = boto3.client('ec2')

    available_vpcs = ec2_client.describe_vpcs()
    vpcs = available_vpcs["Vpcs"]

    for vpc in vpcs:
        print(vpc["VpcId"])


# returns detailed volume list
def get_volumes():

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_volumes()

    complete_volume_list = []

    # extract data from boto3 output from every volume to it's dictionary
    for volume in response['Volumes']:
        volume_dict = {}

        volume_dict['volume_id'] = volume['VolumeId']        
        volume_dict['volume_type'] = volume['VolumeType']
        volume_dict['volume_state'] = volume['State']

        for attachment in volume['Attachments']:
            volume_dict['instance_id'] = attachment['InstanceId']
            volume_dict['attachment_state'] = attachment['State']

        # add dictionary to returned list     
        complete_volume_list.append(volume_dict)
    
    return complete_volume_list

