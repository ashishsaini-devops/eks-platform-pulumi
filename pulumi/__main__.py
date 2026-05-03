import pulumi
import pulumi_aws as aws
import pulumi_eks as eks

# Create an EKS cluster
cluster = eks.Cluster(
    "eks-cluster",
    instance_type="t3.medium",
    desired_capacity=2,
    min_size=1,
    max_size=3,
)

# Export kubeconfig
pulumi.export("kubeconfig", cluster.kubeconfig)
