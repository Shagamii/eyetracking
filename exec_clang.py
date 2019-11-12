import subprocess
from os.path import join
import time

def kill_survived_process(process_name):
    subprocess.call(['taskkill', '/im', process_name, '/F'])

def exec_clang(source):
    exec_file_name = "exec_file_name"
    c_file_name = exec_file_name + ".c"
    exec_dirname = "clang_sandbox"

    with open(join("..", exec_dirname, c_file_name), 'w') as f:
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
            return stderr_of_exec_file.decode("shiftjis")
        return stdout_of_exec_file.decode("shiftjis")
    except subprocess.TimeoutExpired:
        proc_of_exec_file.kill()
        retry_proc_of_exec_file = subprocess.Popen(
            [exec_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=join("..", exec_dirname), shell=True,
        )
        result_of_exec_file = []
        start_time = time.time()
        while retry_proc_of_exec_file.poll() is None:
            output = retry_proc_of_exec_file.stdout.readline()
            if (output != b''):
                result_of_exec_file.append(output.decode("shiftjis"))
            if len(result_of_exec_file) > 100:
                result_of_exec_file.append("出力結果が多すぎます\n")
                break
            now = time.time()
            if int(now - start_time) > 2:
                result_of_exec_file.append("タイムアウトしました\n")
                break
        
        kill_survived_process(process_name=exec_file_name + ".exe")
        return ''.join(result_of_exec_file)
