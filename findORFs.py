import regex as re

def inFrameOverlap(matchObj, orfs):
    for seq in orfs:
        if matchObj in seq:
            return True
    return False


def findORFs(dna, sizeMin):
    orfs = []
    startPositions = []
    lengths = []

    # Find all possible ORFS in direction
    find = re.finditer(r'ATG(...)*?(TAG|TAA|TGA)', dna, overlapped = True)
    for f in find:
        #weed out pseudo-orfs found within true orf
        if inFrameOverlap(f.group(0), orfs):
            continue
        else:
            orf = f.group(0)
            if len(orf) >= min_len:
                orfs.append(orf)
                startPositions.append(f.start() + 1)
                lengths.append(len(orf))

    return orfs, startPositions, lengths

def readFrame(startPosition):
    # Distinguish reading frame with start position
    remain = startPosition % 3
    if remain == 1:
        return 1
    elif remain == 2:
        return 2
    elif remain == 0:
        return 3