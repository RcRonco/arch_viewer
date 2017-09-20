import ansible.runner
import sys

result = ansible.runner.Runner(pattern='*', forks=10, module_name='', module_args='').run
if result is None:
    print("No hosts found")
    sys.exit(1)

for (hostname, result)