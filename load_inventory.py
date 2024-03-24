import ansible_runner

def run_ping_playbook(inventory_path, playbook_path):
    # Execute the playbook
    r = ansible_runner.run(private_data_dir='.', playbook=playbook_path, inventory=inventory_path)

    # Print execution stats
    print("Playbook Execution Stats:")
    for host, stats in r.stats.items():
        print(f"{host}: {stats}")

# Specify your inventory and playbook paths
inventory_path = './hosts.yml'  # Adjust this path to your inventory directory or file
playbook_path = './ping.yml'      # Make sure this playbook exists in the current directory

if __name__ == "__main__":
    run_ping_playbook(inventory_path, playbook_path)


