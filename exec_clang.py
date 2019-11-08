import subprocess
from os.path import join

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
    process_of_exec_file = subprocess.run(
        [exec_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=join("..", exec_dirname), shell=True, timeout=3)
    if (process_of_exec_file.returncode == 1):
        return process_of_exec_file.stderr.decode("shiftjis")
    return process_of_exec_file.stdout.decode("shiftjis")
    # proc = subprocess.Popen(
    #     [exec_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=join("..", exec_dirname), shell=True)
    # try:
    #     process_of_exec_file = proc.communicate(timeout=3)
    #     print(process_of_compile)
    # except subprocess.TimeoutExpired:
    #     proc.kill()
    # if (proc.returncode == 1):
    #     return proc.stderr.decode("shiftjis")
    # return proc.stdout.read().decode("shift
