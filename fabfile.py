from fabric.api import env, task, run, local, require, cd
from gitric.api import (  # noqa
    git_seed, git_reset, git_init, git_head_rev, allow_dirty, force_push
)
from fabvenv import virtualenv, make_virtualenv

env.use_ssh_config = True


@task
def prod():
    '''an example production deployment'''
    env.hosts = ['welt2000']
    env.repo_path = '/home/welt2000/src'
    env.venv_path = '/home/welt2000/venv'


@task
def test():
    """ run the unit test suite """
    local('py.test')


@task
def init():
    """ initialize the virtualenv and git repo on the server """

    require('repo_path', 'venv_path')

    # Create the virtualenv
    make_virtualenv(env.venv_path, system_site_packages=False)

    # Create the git repo
    git_init(env.repo_path)


@task
def deploy():
    """ deploy the app to the server """

    require('repo_path', 'venv_path')

    commit = git_head_rev()

    # Run the test suite first !
    test()

    # Update the new code
    git_seed(env.repo_path, commit=commit)

    # Activate the new code
    git_reset(env.repo_path, commit=commit)

    with cd(env.repo_path), virtualenv(env.venv_path):
        run('pip install -r requirements-prod.txt')
        restart()


@task
def clean():
    run('rm -rf /home/welt2000/src')
    run('rm -rf /home/welt2000/venv')


def supervisor_run(cmd):
    run("supervisorctl {}".format(cmd), shell=False)


@task
def restart():
    """ Restart supervisor service and view some output of log file """
    supervisor_run("restart welt2000")
    run("sleep 1")
    supervisor_run("tail welt2000")
