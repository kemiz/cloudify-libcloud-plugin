## Local Blueprint

[This blueprint](local-blueprint.yaml) allows you to provision VMs on any supported clouds using your local machine. <br>
Let see how this is done:

### Step 0: Prerequisites

The Cloudify libcloud plugin uses a Cloud Configuration Service to obtain the respective cloud configurations. <br>
Follow the instructions [here]('https://github.com/kemiz/cloud-config-service/tree/master/blueprints/local-blueprint') to deploy the [Cloud Configuration Service](https://github.com/kemiz/cloud-config-service).

### Step 1: Initialize

`cfy local init -p local-blueprint.yaml` <br>

This command (as the name suggests) initializes your working directory to work with the given blueprint.
Now, you can run any type of workflows on this blueprint. <br>

### Step 2: Install

Lets run the `install` workflow: <br>

```bash
cfy local execute -w install
2015-09-15 13:17:05 CFY <local> Starting 'install' workflow execution
2015-09-15 13:17:05 CFY <local> [vm_templates_edc62] Creating node
2015-09-15 13:17:05 CFY <local> [abstract_server_59407] Creating node
2015-09-15 13:17:05 CFY <local> [abstract_server_59407.create] Sending task 'libcloud_plugin.compute.create'
2015-09-15 13:17:05 CFY <local> [abstract_server_59407.create] Task started 'libcloud_plugin.compute.create'
2015-09-15 13:17:05 LOG <local> [abstract_server_59407.create] INFO: provider_config: {'name': 'ec2_giga', 'parameters': {}, 'resource_id': '', 'key_name': 'christos-us-east-1', 'ec2_region_name': 'us-east-1', 'aws_access_key_id': '***', 'key_path': '~/.ssh/christos-us-east-1.pem', 'aws_secret_access_key': '***', 'type': 'aws', 'use_external_resource': False}. vm_config: {u'image': u'ubuntu_trusty', u'size': u'large'}. provider: awstemplates: {u'size_templates': {u'openstack': {u'large': u'standard.xlarge'}, u'aws': {u'large': u'm3.xlarge'}}, u'image_templates': {u'openstack': {u'ubuntu_trusty': {u'image_id': u'55aa4df7-1996-4507-955f-30f72d970836', u'user': u'ubuntu'}}, u'aws': {u'ubuntu_trusty': {u'image_id': u'ami-d05e75b8', u'user': u'ubuntu', u'agent_package_url': u''}}}}
2015-09-15 13:17:05 LOG <local> [abstract_server_59407.create] INFO: Getting the image and size templates for the requested provider
2015-09-15 13:17:05 LOG <local> [abstract_server_59407.create] INFO: image_templates: {u'ubuntu_trusty': {u'image_id': u'ami-d05e75b8', u'user': u'ubuntu', u'agent_package_url': u''}}. size_templates: {u'large': u'm3.xlarge'}
2015-09-15 13:17:05 LOG <local> [abstract_server_59407.create] INFO: Getting the image_id and size_id for the requested provider
2015-09-15 13:17:05 LOG <local> [abstract_server_59407.create] INFO: image_id: ami-d05e75b8. size: m3.xlarge
2015-09-15 13:17:05 LOG <local> [abstract_server_59407.create] INFO: Creating IaaS driver instance for: aws
2015-09-15 13:17:05 LOG <local> [abstract_server_59407.create] INFO: Creating parameters for instance
2015-09-15 13:17:05 LOG <local> [abstract_server_59407.create] INFO: Provisioning VM on {'ex_keyname': 'christos-us-east-1', 'image': <NodeImage: id=ami-d05e75b8, name=None, driver=Amazon EC2  ...>, 'name': 'test_node', 'size': <NodeSize: id=m3.xlarge, name=Extra Large Instance, ram=15360 disk=80000 bandwidth=None price=0.28 driver=Amazon EC2 ...>} using the following parameters: {'ex_keyname': 'christos-us-east-1', 'image': <NodeImage: id=ami-d05e75b8, name=None, driver=Amazon EC2  ...>, 'name': 'test_node', 'size': <NodeSize: id=m3.xlarge, name=Extra Large Instance, ram=15360 disk=80000 bandwidth=None price=0.28 driver=Amazon EC2 ...>}
2015-09-15 13:17:13 LOG <local> [abstract_server_59407.create] INFO: Waiting for state: 0
2015-09-15 13:17:19 LOG <local> [abstract_server_59407.create] INFO: Waiting for state: 0
2015-09-15 13:17:26 LOG <local> [abstract_server_59407.create] INFO: Waiting for state: 0
2015-09-15 13:17:32 LOG <local> [abstract_server_59407.create] INFO: Waiting for state: 0
2015-09-15 13:17:38 LOG <local> [abstract_server_59407.create] INFO: Waiting for state: 0
2015-09-15 13:17:38 LOG <local> [abstract_server_59407.create] INFO: Provisioned VM. Node id: i-2ad963ff, IP: 10.157.142.102
2015-09-15 13:17:38 CFY <local> [abstract_server_59407.create] Task succeeded 'libcloud_plugin.compute.create'
2015-09-15 13:17:38 CFY <local> [vm_templates_edc62] Configuring node
2015-09-15 13:17:38 CFY <local> [abstract_server_59407] Configuring node
2015-09-15 13:17:38 CFY <local> [vm_templates_edc62] Starting node
2015-09-15 13:17:39 CFY <local> [abstract_server_59407] Starting node
2015-09-15 13:17:39 CFY <local> [abstract_server_59407.start] Sending task 'libcloud_plugin.compute.start'
2015-09-15 13:17:39 CFY <local> [abstract_server_59407.start] Task started 'libcloud_plugin.compute.start'
2015-09-15 13:17:39 CFY <local> [abstract_server_59407.start] Task succeeded 'libcloud_plugin.compute.start'
2015-09-15 13:17:39 CFY <local> 'install' workflow execution succeeded
```

This command will provision a new VM on the cloud of your choice.

(It's all installed under the `tmp` directory by default)<br>
Once its done, you should be able to execute a GET request to [http://localhost:8180/clouds](http://localhost:8180/clouds) and see the result.
**Note that the result should be an array of cloud configurations as in the 'test_cloud_config.yaml'**
<br>


### Step 3: Uninstall

To uninstall the application we run the `uninstall` workflow: <br>

`cfy local execute -w uninstall`
