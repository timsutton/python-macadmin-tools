#!/usr/bin/python

import re

def main():
    contents = open('README.md', 'r').read()
    after_toc = contents[contents.find('##'):]

    count = 0
    project_names = []
    for line in after_toc.splitlines():
        match = re.match(r'^\* \[(.*?)\].*$', line)
        if match:
            count += 1
            project_names.append(match.groups()[0])

    for proj in sorted(project_names, key=lambda s: s.lower()):
        print proj
    print
    print "Total: %s" % count

if __name__ == '__main__':
    main()
