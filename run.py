import subprocess


def scale_selenium_nodes(node_count):
    command = f"docker-compose up --build -d --scale chrome={node_count}"
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    node_count = 1
    scale_selenium_nodes(node_count)
    print(f"Chrome nodes are scaled to {node_count}")

