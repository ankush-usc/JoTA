#!/usr/local/bin/python
import os
def whats():
    os.getcwd()
    print("entered")
    cmd = "scrapy crawl indeed"
    """cmd = "sudo scrapy crawl whats" """
    os.system(cmd)
    return

whats()