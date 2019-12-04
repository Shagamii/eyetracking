import subprocess
from os.path import join
import time

from timeout import timeout

def kill_survived_process(process_name):
    subprocess.call(['taskkill', '/im', process_name, '/F'])

def read_line_from_stdio(stdio):
    return stdio.readline()

def exec_clang(source):
    exec_file_name = "exec_file_name"
    c_file_name = exec_file_name + ".c"
    exec_dirname = "clang_sandbox"

    with open(join("..", exec_dirname, c_file_name), 'w', newline="\n") as f:
        print(source)
        f.write(source)
    
    kill_survived_process(process_name=exec_file_name + ".exe")

    process_of_compile = subprocess.Popen(["gcc", "-o", exec_file_name, c_file_name],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=join("..", exec_dirname), shell=True)
    result_of_compile, error_of_compile = process_of_compile.communicate()
    if (process_of_compile.returncode == 1):
        process_of_compile.kill()
        return error_of_compile.decode("shiftjis")
    process_of_compile.kill()
    exec_cmd = ".\\" + exec_file_name + ".exe"
    proc_of_exec_file = subprocess.Popen(
        [exec_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=join("..", exec_dirname), shell=True,)
    try:
        stdout_of_exec_file, stderr_of_exec_file = proc_of_exec_file.communicate(timeout=1)
        proc_of_exec_file.kill()
        if proc_of_exec_file.returncode == 1:
            if (stderr_of_exec_file != b''):
                return stderr_of_exec_file.decode("shiftjis")
            return 'segmentation fault'
        return stdout_of_exec_file.decode("shiftjis")
    except subprocess.TimeoutExpired:
        proc_of_exec_file.kill()
        retry_proc_of_exec_file = subprocess.Popen(
            [exec_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=join("..", exec_dirname), shell=True,
        )
        result_of_exec_file = []
        start_time = time.time()
        while retry_proc_of_exec_file.poll() is None:
            read_retry_proc = timeout(timeout=3)(read_line_from_stdio)
            try:
                output = read_retry_proc(retry_proc_of_exec_file.stdout)
                if (output != b''):
                    result_of_exec_file.append(output.decode("shiftjis"))
            except:
                result_of_exec_file.append("タイムアウトしました\n")
                break

            if len(result_of_exec_file) > 100:
                result_of_exec_file.append("出力結果が多すぎます\n")
                break
            now = time.time()
            if int(now - start_time) > 10:
                result_of_exec_file.append("タイムアウトしました\n")
                break
        
        kill_survived_process(process_name=exec_file_name + ".exe")
        return ''.join(result_of_exec_file)
