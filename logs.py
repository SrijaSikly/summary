from pathlib import Path

def readlogs(fp):
    with open(fp, 'r') as file:
        return [line.rstrip('\n') for line in file.readlines()]


def writelogs(fp,group,cl=False) -> None:
    with open(fp, 'w' if cl else 'a', encoding='utf-8') as file:
        file.writelines(line.rstrip('\r\n')+'\n' for line in group)


def grouplogs(logs,types):
    groups={t:[] for t in types}
    for line in logs:
        for t in types:
            if t in line:
                groups[t].append(line)
                break
    return groups


# === TESTS ===

def getpath(rel):
    return str(Path(__file__).parent/rel)

def testgroups():
    fp = getpath('demo_logs.log')

    typs=('INFO','WARNING','DEBUG','ERROR')
    cats=tuple(map(lambda s: '['+s+']',typs))

    return grouplogs(readlogs(fp),cats)

def testwrites():
    folder=getpath('logsout/demo')
    groups=testgroups()
    Path(folder).mkdir(parents=True,exist_ok=True)
    for k in groups:
        writelogs(f"{folder}/demo_{k[1:-1]}.log",groups[k],True)

if __name__=='__main__':
    testwrites()
