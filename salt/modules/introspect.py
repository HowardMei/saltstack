# -*- coding: utf-8 -*-
'''
Functions to perform introspection on a minion, and return data in a format
usable by Salt States
'''

# Import python libs
from __future__ import absolute_import
import os

# Import 3rd-party libs
import salt.ext.six as six


def running_service_owners(
        exclude=('/dev', '/home', '/media', '/proc', '/run', '/sys/', '/tmp',
                 '/var')
    ):
    '''
    Determine which packages own the currently running services. By default,
    excludes files whose full path starts with ``/dev``, ``/home``, ``/media``,
    ``/proc``, ``/run``, ``/sys``, ``/tmp`` and ``/var``. This can be
    overridden by passing in a new list to ``exclude``.

    CLI Example:

        salt myminion introspect.running_service_owners
    '''
    error = {}
    if 'pkg.owner' not in __salt__:
        error['Unsupported Package Manager'] = (
            'The module for the package manager on this system does not '
            'support looking up which package(s) owns which file(s)'
        )

    if 'file.open_files' not in __salt__:
        error['Unsupported File Module'] = (
            'The file module on this system does not '
            'support looking up open files on the system'
        )

    if error:
        return {'Error': error}

    ret = {}
    open_files = __salt__['file.open_files']()

    execs = __salt__['service.execs']()
    for path in open_files:
        ignore = False
        for bad_dir in exclude:
            if path.startswith(bad_dir):
                ignore = True

        if ignore:
            continue

        if not os.access(path, os.X_OK):
            continue

        for service in execs:
            if path == execs[service]:
                pkg = __salt__['pkg.owner'](path)
                ret[service] = next(six.itervalues(pkg))

    return ret


def enabled_service_owners():
    '''
    Return which packages own each of the services that are currently enabled.

    CLI Example:

        salt myminion introspect.enabled_service_owners
    '''
    error = {}
    if 'pkg.owner' not in __salt__:
        error['Unsupported Package Manager'] = (
            'The module for the package manager on this system does not '
            'support looking up which package(s) owns which file(s)'
        )

    if 'service.show' not in __salt__:
        error['Unsupported Service Manager'] = (
            'The module for the service manager on this system does not '
            'support showing descriptive service data'
        )

    if error:
        return {'Error': error}

    ret = {}
    services = __salt__['service.get_enabled']()

    for service in services:
        data = __salt__['service.show'](service)
        if 'ExecStart' not in data:
            continue
        start_cmd = data['ExecStart']['path']
        pkg = __salt__['pkg.owner'](start_cmd)
        ret[service] = next(six.itervalues(pkg))

    return ret


def service_highstate(requires=True):
    '''
    Return running and enabled services in a highstate structure. By default
    also returns package dependencies for those services, which means that
    package definitions must be created outside this function. To drop the
    package dependencies, set ``requires`` to False.

    CLI Example:

        salt myminion introspect.service_highstate
        salt myminion introspect.service_highstate requires=False
    '''
    ret = {}
    running = running_service_owners()
    for service in running:
        ret[service] = {'service': ['running']}

        if requires:
            ret[service]['service'].append(
                {'require': {'pkg': running[service]}}
            )

    enabled = enabled_service_owners()
    for service in enabled:
        if service in ret:
            ret[service]['service'].append({'enabled': True})
        else:
            ret[service] = {'service': [{'enabled': True}]}

        if requires:
            exists = False
            for item in ret[service]['service']:
                if isinstance(item, dict) and next(six.iterkeys(item)) == 'require':
                    exists = True
            if not exists:
                ret[service]['service'].append(
                    {'require': {'pkg': enabled[service]}}
                )

    return ret


def saltstate_list():
    '''
    Returns the list of current states on the node
    CLI Example::
        salt '*' introspect.saltstate_list
    '''
    import salt.state
    hists = salt.state.HighState(__opts__)
    top = hists.get_top()
    return hists.top_matches(top)


def saltstate_in(checklist, env=None, **kwargs):
    '''
    Return True if all given pkg names in the checklist are in current state
    CLI Example::
        salt '*' introspect.saltstate_in 'checklist={"nginx", "collectd"}' env=master
    '''
    import salt.state
    from operator import add
    checklist = set(checklist)
    hists = salt.state.HighState(__opts__)
    top = hists.get_top()
    match = hists.top_matches(top)
    if env != None:
        if env in match:
            return checklist.issubset(set(match[env]))
    else:
        for env in match:
            if checklist.issubset(set(match[env])):
                return True
    return False


def public_ipv4(checkurl=None, timeout=1):
    '''
    Return public ipv4 of the given machines
    CLI Example::
        salt '*' introspect.public_ipv4
    '''
    from salt.utils.get_pubip import get_pubipv4 as _get_pubipv4
    ipv4=_get_pubipv4(checkurl,timeout)
    if ipv4:
        return ipv4
    else
        return 'Unknown'
