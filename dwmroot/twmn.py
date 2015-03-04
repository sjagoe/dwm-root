from __future__ import print_function, unicode_literals, absolute_import

import subprocess

import psutil


def _is_twmn(process):
    try:
        if 'twmnd' in process.name():
            return True
        return False
    except psutil.NoSuchProcess:
        return False


def _kill_twmn(process):
    try:
        process.terminate()
        process.wait()
    except psutil.NoSuchProcess:
        pass


def _start_twmn():
    return subprocess.Popen(['/usr/local/bin/twmnd'])


def _re_exec_twmnd(twmnd):
    if twmnd is not None:
        twmnd.terminate()
        twmnd.communicate()

    for process in psutil.process_iter():
        if _is_twmn(process):
            _kill_twmn(process)

    return _start_twmn()


def _needs_re_exec(processes):
    count = len(processes)
    if count == 1:
        process, = processes
        try:
            if 'session' in process.cmdline():
                return True
        except psutil.NoSuchProcess:
            return True
    elif count == 0 or count > 1:
        return True
    return False


def poll_twmn_processes(twmnd):
    procs = []
    for process in psutil.process_iter():
        if _is_twmn(process):
            procs.append(process)
    if _needs_re_exec(procs):
        return _re_exec_twmnd(twmnd)
    elif twmnd is None:
        return _re_exec_twmnd(twmnd)
    elif twmnd.poll() is not None:
        return _re_exec_twmnd(None)
    return twmnd
