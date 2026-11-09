#! /usr/bin/python3

import subprocess
import sys
import tempfile

import render


def show_diff(data, file_name):
    t = tempfile.NamedTemporaryFile(mode="w+t")
    print(f"Temp file name is {t.name}")
    with open(t.name, "wt") as f:
        f.write(data)
    subprocess.call(["diff", "-u", file_name, t.name])


def check_rendering(input_file, generator_factory, in_situ_file_to_check):
        with open(in_situ_file_to_check, "r") as f:
            existing_body = f.read()
        output_generator = generator_factory(input_file)
        generated_body = render.get_file_body_from_generator(output_generator.Generate())
        if existing_body != generated_body:
            print(f"file {in_situ_file_to_check} is out-of-date.", file=sys.stderr)
            show_diff(generated_body, in_situ_file_to_check)
            return False
        else:
            return True

def main(args):
    del args
    exit_value = 0
    for base_name in ("sk", "sk2"):
        input_file = f"{base_name}.tx2as"
        in_situ_file_to_check = f"{base_name}.html"
        if not check_rendering(input_file, render.HTMLGenerator, in_situ_file_to_check):
            exit_value = 1
    return exit_value

        
if __name__ == "__main__":
    sys.exit(main(sys.argv))
