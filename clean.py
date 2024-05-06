import subprocess


def clean():
    command = f"docker-compose down"
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    clean()
