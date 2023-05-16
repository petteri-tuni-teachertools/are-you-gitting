# Are you gitting - tool to fetch and keep selection of git repos updated

## Problem

The problem this project primarily and originally solved is as follows:
There are N  students in a course. They produce 1-M git projects during the course. I as instructor should evaluate their end products. Ad hoc default solution is to use browser based UI - TAMK GitLab server typically. This feels clumsy. Opening and viewing the source code is slow and awkward.

The situation begs for a better way.

## Solution

More user friendly could be to have all the projects readily available in a disk, easily viewable from file explorer and some code editor.

This is what is implemented here.

Suggestions for even better and more efficient solutions are warmly welcomed.


# How it works

1. Provide source of information that contains data in CSV format
- owner (name, email)
- clone url

2. Use the CSV data as input to this tool. It will clone and pull latest versions of the projects to local disk.

## Command
````
python3 gitclone.py
````

## Command line arguments

n/a

# Next steps

- Design and implement configuration.  
- Implement direct fetch from API - now supports using file only
- rethink configuration - should be easier than with Steon

