import subprocess


def docker_cleanup():
    command = f"docker-compose down"
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    docker_cleanup()
    print(f"Success")
