import ansible_runner

def run_ping_playbook(inventory_path, playbook_path):
    # Execute the playbook
    r = ansible_runner.run(private_data_dir='.', playbook=playbook_path, inventory=inventory_path)

    # Print execution stats
    print("Playbook Execution Stats:")
    for host, stats in r.stats.items():
        print(f"{host}: {stats}")

inventory_path = './hosts.yml' 
playbook_path = './ping.yml'  

if __name__ == "__main__":
    run_ping_playbook(inventory_path, playbook_path)


