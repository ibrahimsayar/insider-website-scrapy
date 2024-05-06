import subprocess


def scale_selenium_nodes(node_count):
    command = f"docker-compose up --build --scale chrome={node_count}"
    subprocess.run(command, shell=True, check=True)


def end_program():
    command = "docker-compose down"
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    node_count = 1
    scale_selenium_nodes(node_count)
    end_program()
    print(f"Chrome nodes are scaled to {node_count}")
