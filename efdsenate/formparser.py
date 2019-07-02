import json
from formparse.fdrform import fdr

if __name__ == '__main__':
    print(json.dumps(fdr.main(), indent=2))

