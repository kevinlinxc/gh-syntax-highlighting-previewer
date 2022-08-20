""" Script form of the pseudocode for this repo"""
import yaml

input_text = """\
line1:
    line2:
        line3\
"""


# read languages.yml file
with open('languages.yml', 'r') as f:
    languages = yaml.safe_load(f)
    schemes = languages.keys()
    for scheme in schemes:
        print(scheme)
        print(f"```{scheme}")
        print(input_text)
        print("```")

# copy the output, paste it into a markdown editor on GitHub, and click preview to see what the input text looks like
# in every scheme
