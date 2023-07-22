#!/usr/bin/python3

import subprocess
import asyncio
import sys
import os


async def echo_name_1(input):
    # create a subprocess using create_subprocess_shell()
    process = await asyncio.create_subprocess_shell('echo Hello World my name is ' + input, stdout=asyncio.subprocess.PIPE)
    # read data from the subprocess
    data, _ = await process.communicate()
    # report the data
    print(data)


def echo_name_2(input):
    # create a subprocess using create_subprocess_shell()
    
    # NOT VULNERABLE
    # proc = subprocess.Popen(['echo',f'my name is {input}'],stdout=subprocess.PIPE)

    # Not vulnerable
    # subprocess.check_output('ls -l dir/')

    # VULNERABLE!
    # output = subprocess.call("echo my name is {}".format(input), shell=True, stdout=subprocess.PIPE)
    # print(output)

    # VULNERABLE!
    output = subprocess.run("echo my name is {}".format(input), shell=True, stdout=subprocess.PIPE)
    print(output)


def echo_name_3(input):
    # VULNERABLE
    # os.system('echo my name is ' + input)

    # VULNERABLE
    output = os.popen('echo my name is ' + input).read()
    print(output)


def echo_name_4(input):
    eval(f'print("{input}")')


def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <func> <input>")
        sys.exit(1)
    func = sys.argv[1]
    input = sys.argv[2]
    
    if func == 'echo_name_1':
        asyncio.run(echo_name_1(input))

    if func == 'echo_name_2':
        echo_name_2(input)

    if func == 'echo_name_3':
        echo_name_3(input)

    if func == 'echo_name_4':
        echo_name_4(input)



if __name__ == '__main__':
    main()


