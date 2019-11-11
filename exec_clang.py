import subprocess
from os.path import join
import time

def exec_clang(source):
    exec_file_name = "exec_file_name"
    c_file_name = exec_file_name + ".c"
    exec_dirname = "clang_sandbox"

    with open(join("..", exec_dirname, c_file_name), 'w') as f:
        f.write(source)

    process_of_compile = subprocess.run(["gcc", "-o", exec_file_name, c_file_name],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=join("..", exec_dirname), shell=True)
    if (process_of_compile.returncode == 1):
        return process_of_compile.stderr.decode("shiftjis")
    exec_cmd = ".\\" + exec_file_name + ".exe"
    proc_of_exec_file = subprocess.Popen(
        [exec_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=join("..", exec_dirname), shell=True)

    try:
        stdout_of_exec_file, stderr_of_exec_file = proc_of_exec_file.communicate(timeout=1)
        proc_of_exec_file.kill()
        if proc_of_exec_file.returncode == 1:
            return stderr_of_exec_file.decode("shiftjis")
        return stdout_of_exec_file.decode("shiftjis")
    except subprocess.TimeoutExpired:
        proc_of_exec_file.kill()
        retry_proc_of_exec_file = subprocess.Popen(
            [exec_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=join("..", exec_dirname), shell=True)
        # print(proc_of_exec_file.stdout.read())
        result_of_exec_file = []
        while retry_proc_of_exec_file.poll() is None:
            output = retry_proc_of_exec_file.stdout.readline()
            if (output != b''):
                result_of_exec_file.append(output.decode("shiftjis"))
            if len(result_of_exec_file) > 100:
                result_of_exec_file.append("出力結果が多すぎます\n")
                break
        retry_proc_of_exec_file.kill()
        retry_proc_of_exec_file.terminate()
        return ''.join(result_of_exec_file)
