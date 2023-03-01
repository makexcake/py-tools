import boto3

# The following code can be used to monitor activa clusters
# status.

# list all clusters
def list_clusters():
    eks_client = boto3.client('eks')
    clusters = eks_client.list_clusters()
    return clusters['clusters']



# return list with the statuses of all available clusters
def get_cluster_status():

    eks_client = boto3.client('eks') 

    cluster_name_list = list_clusters()

    all_cluster_statuses = []

    for cluster_name in cluster_name_list:
        response = eks_client.describe_cluster(name=cluster_name)

        cluster_status_list = {'name': response['cluster']['name'],
                             'version': response['cluster']['version'], 
                             'status': response['cluster']['status']
                             }
        all_cluster_statuses.append(cluster_status_list)

    return all_cluster_statuses