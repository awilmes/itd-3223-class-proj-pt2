# Loads the config once and only once
import tomlib


with open('conf/config.toml', mode='rb') as fp:
    cfg = tomlib.load(fp)