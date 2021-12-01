def isBalanced(groups, maxSpread):
    for grp in groups:
        if max(grp) - min(grp) > maxSpread:
            return False
        
    return True
    
def getGroups(levels, nGroups):
    maxLevel = max(levels)
    minLevel = min(levels)
    diffLevel = maxLevel - minLevel
    rangeLevel = diffLevel / nGroups
    res = []
    res.append({level for level in levels if level >= minLevel and level <= minLevel + rangeLevel})
    for i in range(1, nGroups):
        res.append({level for level in levels if level > minLevel + rangeLevel * i and level <= minLevel + rangeLevel * (i + 1)})
        
    return res
    
def GroupDivision(levels, maxSpread):
    # Write your code here
    maxLevel = max(levels)
    minLevel = min(levels)
    diffLevel = maxLevel - minLevel
    for i in range(1, diffLevel + 2):
        groups = getGroups(levels, i)
        if isBalanced(groups, maxSpread):
            return i
    