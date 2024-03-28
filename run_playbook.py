import ansible_runner
import requests

def run_hello_playbook_and_verify(inventory_path, playbook_path):
    
    # Run the playbook
    r = ansible_runner.run(private_data_dir='.', playbook=playbook_path, inventory=inventory_path)
    print("Playbook run results:")
    print(r.stats)
    
    
    print("\nVerifying NodeJS server responses...")
    for port in [3000, 3001, 3002]:
        try:
            response = requests.get(f"http://localhost:{port}")
            print(f"Server on port {port} responded with: {response.text.strip()}")
        except requests.ConnectionError:
            print(f"Failed to connect to server on port {port}")

if __name__ == "__main__":
    run_hello_playbook_and_verify('./hosts.yml', './hello.yml')
