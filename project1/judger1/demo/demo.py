import _judger
import os
import subprocess

dir_work = "./"


def compile(lang):
    build_cmd = {
        "c": "gcc main.c -o main -fno-asm -Wall -lm --static -std=c99 -DONLINE_JUDGE",
        "cpp": "g++ main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o main",
        "java": "javac -J-Xms32m -J-Xmx256m main.java",
        "py3": 'python -m py_compile main.py',
    }
    p = subprocess.Popen(build_cmd[lang], shell=True, cwd=dir_work, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()  # get compile err msg
    if p.returncode == 0:
        return True
    else:
        print("Compile Error\n----")
        print(err.decode("utf-8"), out.decode("utf-8"))
        return False


def compare() -> int:
    cur_res = os.path.join("./sample.out")
    usr_res = os.path.join("./run.out")
    try:
        curr = open(cur_res).read().replace('\r', '').rstrip()
        usrr = open(usr_res).read().replace('\r', '').rstrip()
    except:
        return -2

    if curr == usrr or curr.split() == usrr.split():
        return 0
    else:
        return -1  # WA


if __name__ == '__main__':
    language = input("Input language：")
    if compile(language):
        x = 1000
        ret = _judger.run(max_cpu_time=x,
                          max_real_time=2000,
                          max_memory=128 * 1024 * 1024,
                          max_process_number=200,
                          max_output_size=10000,
                          max_stack=32 * 1024 * 1024,
                          # five args above can be _judger.UNLIMITED
                          exe_path="main",
                          input_path="sample.in",
                          output_path="run.out",
                          error_path="run.out",
                          args=[],
                          # can be empty list
                          env=[],
                          log_path="judger.log",
                          # can be None
                          seccomp_rule_name="c_cpp",
                          uid=0,
                          gid=0)
        print('CPU time: ', ret['cpu_time'], ' ms')
        print('Memory: ', int(ret['memory']/1024), 'KB')

        result_code = int(ret['result'])
        error_code = int(ret['error'])
        compare_res = compare()

        if result_code == 5 or error_code != 0 or compare_res == -2:
            print("System Error")
        elif result_code == 4:
            print("Runtime Error")
        elif result_code == 1 or result_code == 2:
            print("Time Limit Exceeded")
        elif result_code == 3:
            print("Memory Limit Exceeded")
        elif compare_res == -1:
            print("Wrong Answer")
        elif compare_res == 0:
            print("Accepted!")
        else:
            print("System Error")
