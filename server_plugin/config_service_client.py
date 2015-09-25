import requests
from cloudify import ctx

__author__ = 'kemi'


def get_clouds_by_provider(provider, service_base_url='localhost', port='8180', **_):
    return requests.get('http://{0}:{1}/clouds/get_by_provider/{2}'.format(service_base_url, port, provider))


def get_cloud_by_id(cloud_id, service_base_url='localhost', port='8180', **_):
    ctx.logger.info('http://{0}:{1}/clouds/get_by_id/{2}'.format(service_base_url, port, cloud_id))
    return requests.get('http://{0}:{1}/clouds/get_by_id/{2}'.format(service_base_url, port, cloud_id))


def add_cloud(cloud, service_base_url='localhost', port='8180', **_):
    return requests.post('http://{0}:{1}/clouds/'.format(service_base_url, port), cloud)


def remove_cloud(cloud_id, service_base_url='localhost', port='8180', **_):
    return requests.delete('http://{0}:{1}/clouds/delete/{2}'.format(service_base_url, port, cloud_id))


def get_status(service_base_url='localhost', port='8180', **_):
    return requests.get('http://{0}:{1}/status'.format(service_base_url, port))


def get_image_by_provider(service_base_url, port, provider, image):
    request = 'http://{0}:{1}/templates/' \
              'get_image_by_provider?image={2}&provider={3}'\
        .format(service_base_url, port, image, provider)
    ctx.logger.info(request)
    return requests.get(request)


def get_size_by_provider(provider, size, port, service_base_url):
    request = 'http://{0}:{1}/templates/' \
              'get_size_by_provider?size={2}&provider={3}' \
        .format(service_base_url, port, size, provider)
    ctx.logger.info(request)
    return requests.get(request)
