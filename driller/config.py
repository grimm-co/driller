### Redis Options
REDIS_HOST="localhost"
REDIS_PORT=6379
REDIS_DB=1

### Celery Options
BROKER_URL="amqp://guest@localhost//"

CELERY_ROUTES = {'driller.tasks.fuzz': {'queue': 'fuzzer'}, 'driller.tasks.drill': {'queue': 'driller'}}

### Environment Options

# directory contain driller-qemu versions, relative to the directoy node.py is invoked in
QEMU_DIR="driller-qemu"

# directory containing the binaries, used by the driller node to find binaries
BINARY_DIR="/cgc/binaries/"
# directory containing the pcap corpus
PCAP_DIR="/cgc/pcaps/"

### Driller options
# how long to drill before giving up in seconds
DRILL_TIMEOUT=60 * 40 # 60 minutes

MEM_LIMIT=8 * 1024 * 1024 * 1024

### Fuzzer options

# how often to check for crashes in seconds
CRASH_CHECK_INTERVAL=60

# how long to fuzz before giving up in seconds
FUZZ_TIMEOUT=60 * 60 * 24

# how long before we kill a dictionary creation process
DICTIONARY_TIMEOUT=60 * 60 # 1 hour

# how many fuzzers should be spun up when a fuzzing job is received
FUZZER_INSTANCES=4

# where the fuzzer should place it's results on the filesystem
FUZZER_WORK_DIR="/dev/shm/work"
