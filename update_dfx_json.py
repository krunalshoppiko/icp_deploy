import json
import sys

# Load the existing dfx.json file
with open('dfx.json', 'r') as file:
    dfx_config = json.load(file)

# Define the new canister configuration
new_canister = {
    "type": "motoko",
    "main": "src/my_new_canister/main.mo",
    "source": ["src/my_new_canister"]
}

# Add the new canister to the dfx.json configuration
dfx_config['canisters']['my_new_canister'] = new_canister

# Save the modified dfx.json file
with open('dfx.json', 'w') as file:
    json.dump(dfx_config, file, indent=2)

print("dfx.json has been updated to include 'my_new_canister'.")
