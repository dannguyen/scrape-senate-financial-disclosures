import json
from formparse.fdrform import fdr

def main():
    print(json.dumps(fdr.main(), indent=2))


if __name__ == '__main__':
    main()
