import boto3 
import operator

# The following functions can be used to automate snapshot
# managent.


ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

# creates volume snapshot for all volumes with specific volume tag
def create_vol_snapshot(tag, value):
    
    volumes = ec2_client.describe_volumes(
        Filters = [
            {
                'Name': f'tag:{tag}',
                'Values': [value]
            }
        ]
    )
    for volume in volumes['Volumes']:
        new_snapshot = ec2_resource.create_snapshot(
            Description=value,
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)



# clean old snapshots of volumes with specific tags
def clean_vol_snapshots(tag, value):

    # get volumes with selected tags
    volumes = ec2_client.describe_volumes(
        Filters = [
            {
                'Name': f'tag:{tag}',
                'Values': [value]
            }
        ]
    )

    for volume in volumes['Volumes']:

        # get snapshots list
        snapshots = ec2_client.describe_snapshots(
            OwnerIds=['self'],
            Filters = [
                {
                    'Name': 'volume-id',
                    'Values': [volume['VolumeId']]
                }
            ]
        )

        # sort snapshots by time
        sorted_snapshots = sorted(snapshots['Snapshots'], key=operator.itemgetter('StartTime'), reverse=True)

        # remove all snapshots accept the last
        for snapshot in sorted_snapshots[1:]:
            ec2_client.delete_snapshot(
                SnapshotId = snapshot['SnapshotId']
            )






        